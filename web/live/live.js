
/* ====================================================================================================
   Live logic. The look, the icons and the chat, case and cases views come from the team's prototype
   (github.com/hey-niia/tenard). Here the scripted answers are replaced with calls to the backend:
   /api/building, /api/analyze, /api/explain, /api/letter, /api/diy, /api/case-file (see docs/api.md).
   ==================================================================================================== */
const TYPES = {
  mould: { label: 'Mould', hint: 'Class depends on the size', title: 'Mould', ask: 'Add a photo or a short video of the mould, with something for scale in the frame (a door, a sheet of paper).' },
  leak: { label: 'Leak or water damage', hint: 'An inspector decides the class', title: 'Leak', ask: 'Add a photo or video of where the water comes in and any stains.' },
  paint: { label: 'Peeling paint', hint: 'Lead risk with young kids', title: 'Peeling paint', ask: 'Add a close photo of the peeling paint and one of the whole wall.' },
  window: { label: 'Window or window guard', hint: 'Kids 10 or under', title: 'Window', ask: 'Add a photo of the whole window so the problem shows.' },
  detector: { label: 'Smoke or CO detector', hint: 'Missing or not working', title: 'Detector', ask: 'Add a photo of the detector, or of the ceiling or wall where one should be.' },
  other: { label: 'Something else', hint: 'Pests, heat, walls', title: 'New case', ask: 'Add a photo or a short video of the problem.' }
};
const SUGGEST = ['mould', 'leak', 'paint', 'window', 'detector'];
const SURE = { settled: 'Settled', 'class-from-data': "From HPD's records", 'class-unsettled': 'Inspector decides', unsettled: 'Not settled' };

function guessType(text) {
  const t = text.toLowerCase();
  if (/mou?ld|mildew/.test(t)) return 'mould';
  if (/paint|plaster|lead/.test(t)) return 'paint';
  if (/window|guard/.test(t)) return 'window';
  if (/smoke|detector|carbon|alarm/.test(t)) return 'detector';
  if (/leak|water|drip|stain|flood/.test(t)) return 'leak';
  return 'other';
}

/* ---------- state ---------- */
const FRESH = { type: null, step: 0, desc: null, typedFirst: false,
  photo: null, isVideo: false, file: null, photoId: null,
  address: null, building: null, addrError: null, addrDown: false, addrSkipped: false, addrLate: false,
  analysis: null, answers: {}, qa: [], skipped: {}, explained: false, explainFailed: false, error: null, errorKind: null, busy: null, attachMenu: false,
  asked: false, letter: null, chat: [], notes: [], diyChoice: null, kit: null, owned: {}, packet: null,
  fixed: false, verified: false, awaitVerify: false, afterPhoto: null, insp: null, missed: false, exported: false };
const S = Object.assign({ view: 'chat', typing: false, samples: null, showKit: false }, FRESH);
let run = 0; // bumps on every new case, so a slow answer for an old case is dropped

function set(patch, botDelay) {
  if (botDelay) {
    S.typing = true; render();
    setTimeout(() => { Object.assign(S, patch, { typing: false }); render(); }, botDelay);
  } else { Object.assign(S, patch); render(); }
}
const go = (patch) => () => set(patch, 500);
function reset() { run++; if (pollTimer) clearInterval(pollTimer); set(Object.assign({ view: 'chat', typing: false }, FRESH, { answers: {}, qa: [], skipped: {}, owned: {}, chat: [], notes: [] })); }

/* ---------- backend ---------- */
async function jfetch(url, opts) {
  const r = await fetch(url, opts);
  if (!r.ok) {
    let d = 'error ' + r.status;
    try { const detail = (await r.json()).detail; if (typeof detail === 'string') d = detail; } catch (e) { /* keep the status */ }
    const err = new Error(d); err.status = r.status; // callers tell "not found" and "can't read that file" from "the service is down"
    throw err;
  }
  return r.json();
}
const postJSON = (url, body) => jfetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });

const NO_ADDRESS = "I couldn't find that address in New York City. Try it with the borough, like “122 West 167th Street, Bronx”.";
const RECORDS_DOWN = "I couldn't reach the city's building records just now. Try the address again in a moment.";

// late: the address was typed after the case had moved on (skipped earlier, or a photo came first). It is then
// shown where it was typed, and the photo is checked again with the building's facts.
async function lookupAddress(text, late) {
  const mine = run;
  Object.assign(S, { typing: true, busy: 'Looking up your building' }); render();
  let b = null, down = false;
  try { b = await jfetch('/api/building?address=' + encodeURIComponent(text)); } catch (e) { down = e.status !== 404; }
  if (mine !== run) return;
  Object.assign(S, { typing: false, busy: null });
  if (late) {
    S.chat.push({ q: text, a: b ? buildingLine(b) : down ? RECORDS_DOWN : NO_ADDRESS, sources: [], at: lastBase, aside: true });
    if (b) Object.assign(S, { building: b, address: text, addrLate: true });
    render();
    if (b && S.analysis && (S.photoId || S.file)) analyse();
    return;
  }
  Object.assign(S, b ? { building: b, address: text, addrError: null } : { addrError: text, addrDown: down }); render();
}

// A phone photo is 3 to 12 MB and the app needs 1600 pixels of it. Sending the small copy is what gets a photo
// through on a weak connection. A format this browser can't draw (HEIC outside Safari) goes up as it is, and
// the server converts it.
async function shrink(file) {
  if (!(file.type || '').startsWith('image/') || file.size < 1500000 || !window.createImageBitmap) return file;
  try {
    const bmp = await createImageBitmap(file);
    const k = Math.min(1, 1600 / Math.max(bmp.width, bmp.height));
    const c = document.createElement('canvas'); c.width = Math.round(bmp.width * k); c.height = Math.round(bmp.height * k);
    c.getContext('2d').drawImage(bmp, 0, 0, c.width, c.height);
    const blob = await new Promise((done) => c.toBlob(done, 'image/jpeg', 0.88));
    return blob ? new File([blob], 'photo.jpg', { type: 'image/jpeg' }) : file;
  } catch (e) { return file; }
}

// What the tenant reads while a video is checked, as [seconds waited, line]. A video takes longer than a
// photo, so the line changes to show the app is still working.
const VIDEO_WAIT = [[0, 'Watching your video'], [4, 'Looking for problems in it'], [10, 'Checking what I found'],
  [20, 'Still working. Longer videos take a little more time']];

async function analyse() {
  const mine = run;
  Object.assign(S, { typing: true, error: null, busy: S.isVideo ? VIDEO_WAIT[0][1] : 'Looking at your photo', showKit: false }); render();
  const started = Date.now();
  const waitTimer = S.isVideo ? setInterval(() => {
    if (mine !== run) return;
    const waited = (Date.now() - started) / 1000;
    const line = VIDEO_WAIT.filter((w) => waited >= w[0]).pop()[1];
    if (line === S.busy) return;
    S.busy = line;
    const el = document.getElementById('busy'); // changed in place: a full render would restart the video preview
    if (el) el.textContent = line + ' ';
  }, 500) : null;
  const f = new FormData();
  if (S.photoId) f.append('photo_id', S.photoId);
  else { const up = await shrink(S.file); f.append('photo', up, up.name); }
  if (S.building) f.append('address', S.address);
  f.append('answers', JSON.stringify(S.answers));
  f.append('explain', 'false');
  const note = [S.typedFirst ? S.desc : null].concat(S.notes).filter(Boolean).join(' ');
  if (note) f.append('note', note);
  let a;
  try { a = await jfetch('/api/analyze', { method: 'POST', body: f }).finally(() => clearInterval(waitTimer)); }
  catch (e) {
    if (mine !== run) return;
    const file = e.status === 413 || e.status === 415; // too big, or not a photo or video: asking again won't help
    Object.assign(S, { typing: false, busy: null, error: String(e.message || e), errorKind: file ? 'file' : 'model', photo: null, file: null, photoId: null, analysis: null }); render();
    return;
  }
  if (mine !== run) return;
  if (a.photo) S.photoId = a.photo.id; // follow-up answers send the id, for a photo or a video, not the file again
  if (a.photo && a.photo.url && S.file && !/^image\/(jpeg|png|webp|gif)$/.test(S.file.type)) S.photo = a.photo.url; // a format the browser can't show
  Object.assign(S, { analysis: a, explained: false, explainFailed: false, letter: null, typing: false, busy: null, step: Math.max(S.step, 4) }); render();
  explain(a);
}

// The written explanation arrives after the class and deadline. If it fails, the findings stay: they came from
// the rules, and only the plain-language part is missing.
async function explain(a) {
  const mine = run;
  if (!a.findings.some((x) => x.rule_id)) { S.explained = true; return; }
  try {
    const full = await postJSON('/api/explain', { analysis: a });
    if (mine === run && S.analysis === a) { Object.assign(S, { analysis: full, explained: true, explainFailed: false }); render(); }
  } catch (e) {
    if (mine === run && S.analysis === a) { Object.assign(S, { explained: true, explainFailed: true }); render(); }
  }
}

function answer(fact, value, label, question) {
  S.answers[fact] = value;
  S.qa.push({ q: question, a: label });
  analyse();
}

// The question the app is waiting on, if any: the first one the tenant hasn't said "not sure" to.
function pendingQuestion() {
  if (!S.analysis) return null;
  for (const f of S.analysis.findings) {
    const q = f.outcome === 'needs_answer' && f.questions.find((x) => !S.skipped[x.fact]);
    if (q) return { f, q };
  }
  return null;
}
function notSure(q) { S.skipped[q.fact] = true; S.qa.push({ q: q.question, a: 'Not sure' }); render(); }

// What a typed reply means as an answer to the app's own question, as [value, label]; undefined if it isn't one.
function oneNumber(v) { const n = v.match(/\d+(?:\.\d+)?/g); return n && n.length === 1 && v.length <= 40 ? Number(n[0]) : null; }
function typedAnswer(q, v) {
  const t = v.trim().toLowerCase().replace(/[.!]+$/, '');
  if (q.type === 'bool') return /^(y|yes|yeah|yep|yup|true|correct)\b/.test(t) ? [true, 'Yes'] : /^(n|no|nope|nah|false|none)\b/.test(t) ? [false, 'No'] : undefined;
  if (q.type === 'enum') { const o = (q.options || []).find((x) => t === String(x).toLowerCase().replace(/_/g, ' ')); return o === undefined ? undefined : [o, o]; }
  const n = oneNumber(v);
  if (n === null || (q.fact === 'year_built' && (n < 1700 || n > new Date().getFullYear()))) return undefined;
  return [n, v];
}

// opts.silent: the tenant's words are already on screen (their first message), so only the reply is added.
// opts.at: where in the conversation the exchange belongs; by default, where it is now.
async function ask(question, opts) {
  const o = opts || {};
  const mine = run, entry = { q: o.silent ? null : question, a: null, sources: [], at: o.at === undefined ? lastBase : o.at };
  const history = S.chat.filter((c) => c.q && c.a && !c.aside).slice(-3).map((c) => ({ q: c.q, a: c.a }));
  S.chat.push(entry); render();
  try {
    const r = await postJSON('/api/ask', { question, analysis: S.analysis, history });
    if (mine !== run) return;
    entry.a = r.answer; entry.sources = [...new Set((r.citations || []).map((c) => c.citation))];
  } catch (e) { if (mine !== run) return; entry.a = "I couldn't reach the model just now. Try asking again."; }
  render();
}

async function fetchLetter() {
  const mine = run;
  try {
    const l = await postJSON('/api/letter', { analysis: S.analysis, tenant_name: null, apartment: null });
    if (mine === run) { S.letter = l; render(); }
  } catch (e) { if (mine === run) { S.letter = { error: String(e.message || e) }; render(); } }
}

async function fetchKit(ruleId) {
  const mine = run;
  Object.assign(S, { diyChoice: 'yes', typing: true, busy: 'Finding what you need' }); render();
  let kit;
  try { kit = await jfetch('/api/diy/' + encodeURIComponent(ruleId)); } catch (e) { kit = { error: true }; }
  if (mine !== run) return;
  Object.assign(S, { kit, typing: false, busy: null, showKit: true }); render();
}

let pollTimer = null;
async function buildPacket() {
  const mine = run;
  const place = { at: lastBase, after: S.chat.length }; // where in the conversation the card belongs
  if (!S.building) { S.packet = Object.assign({ error: "I need your address to pull your building's record. Type it here and I'll look it up." }, place); render(); return; }
  S.packet = Object.assign({ status: 'starting', started: Date.now() }, place); render();
  try {
    const r = await postJSON('/api/case-file', { analysis: S.analysis, apartment: null });
    if (mine !== run) return;
    S.packet = Object.assign({ status: 'in_progress', caseId: r.case_id, started: Date.now() }, place); render();
    pollTimer = setInterval(async () => {
      try {
        const s = await jfetch('/api/case-file/' + r.case_id);
        if (mine !== run) { clearInterval(pollTimer); return; }
        if (s.markdown) { clearInterval(pollTimer); S.packet = Object.assign({ status: 'done', markdown: s.markdown, seconds: s.seconds }, place); render(); }
        else if (!/progress|queued|running/i.test(s.status)) { clearInterval(pollTimer); S.packet = Object.assign({ error: 'The agent stopped (' + s.status + '). Try again.' }, place); render(); }
        else { const el = document.getElementById('packet-sub'); if (el) el.textContent = packetSub(S.packet); } // only the seconds change: no full render, which would reset the page under the tenant
      } catch (e) { /* a dropped poll is fine; the next one retries */ }
    }, 5000);
  } catch (e) { if (mine === run) { S.packet = Object.assign({ error: "I couldn't start the case file just now. Try again." }, place); render(); } }
}

function showAttachMenu(open) {
  const box = document.getElementById('msg'), typed = box ? box.value : '';
  S.attachMenu = open; render();
  if (typed && document.getElementById('msg')) document.getElementById('msg').value = typed; // keep what was being typed
}

async function openSamples() {
  set({ view: 'samples' });
  if (!S.samples) {
    try { S.samples = (await jfetch('/api/test-items')).items; } catch (e) { S.samples = []; }
    render();
  }
}

/* ---------- from a finding to the card the design shows ---------- */
function resFrom(f) {
  if (f.outcome === 'violation') {
    const d = f.deadline || {};
    const days = d.unit === 'none' ? 'No grace period' : d.value ? d.value + ' ' + d.unit : 'Not set';
    return { title: f.title, cls: 'Class ' + f.class, sub: f.class_meaning || '', days, daysSub: d.unit === 'none' ? 'penalties start at once' : HPD, label: SURE[f.certainty] || 'Settled', f };
  }
  if (f.outcome === 'inspector_decides') {
    const o = f.class_options || [];
    const cls = o.length > 1 ? o.slice(0, -1).join(', ') + ' or ' + o[o.length - 1] : (o[0] || 'Class');
    return { title: f.title, cls, sub: 'Depends on how bad it is', days: 'Inspector', daysSub: 'sets the deadline', label: 'Inspector decides', f };
  }
  return null;
}
function buildingLine(b) {
  const bits = [];
  if (b.year_built) bits.push('built ' + b.year_built);
  if (b.units_res) bits.push(b.units_res + (b.units_res === 1 ? ' home' : ' homes'));
  if (b.building_kind === 'nycha') bits.push('NYCHA public housing');
  if (b.rent_stabilized) bits.push('rent-stabilized');
  const v = b.open_violations || { total: 0, by_class: {} };
  const cls = Object.entries(v.by_class || {}).filter(([k]) => 'ABC'.includes(k)).map(([k, n]) => n + ' Class ' + k).join(', ');
  return 'Found it: ' + b.address.replace(', USA', '') + '.\n' + (bits.length ? bits.join(' · ') + '.\n' : '') +
    (v.total ? 'HPD has ' + v.total + ' open violation' + (v.total === 1 ? '' : 's') + ' on record for this building' + (cls ? ' (' + cls + ')' : '') + '.' : 'HPD has no open violations on record for this building.');
}
const MOULD_SIZES = [['Under 10 sq ft', 5], ['10 to 30 sq ft', 15], ['30 sq ft or more', 35]];

/* ---------- the conversation ---------- */
const RETALIATION = "It's illegal for your landlord to punish you for complaining. If they try to evict you or raise your rent within a year of a complaint or inspection, the law presumes it's retaliation (NY Real Property Law § 223-b).\n\nThis doesn't apply if the owner lives in a building with fewer than 4 units.";
let lastBase = 0; // how many messages the conversation had, before typed exchanges are placed in it

function conversation() {
  const m = [];
  const bot = (t) => m.push({ t: 'bot', text: t });
  const user = (t) => m.push({ t: 'user', text: t });
  let chips = [];
  if (!S.type) return { m, chips, kase: null, empty: true };

  const T = TYPES[S.type];
  let res = null, title = T.title, status = 'New · add evidence', diy = false, where = '';
  const stageOf = () => ({ filed: !!res && S.step >= 9, violation: !!res && S.step >= 11 && S.insp === 'violation', noViolation: !!res && S.step >= 11 && S.insp === 'none',
    court: !!res && S.step >= 13, resolved: !!res && S.verified, fixedOn, vClass, dueDate, filing: !!res && S.step === 8 });
  let fixedOn = null, vClass = '', dueDate = '';
  // Everything above is rebuilt from the case's state each time. What the tenant typed, the replies, and the
  // case-file card are placed back where they happened (each remembers how long the conversation was then),
  // so a pill tapped after a typed question shows its answer below the question, not above it.
  const done = () => {
    lastBase = m.length;
    const extras = S.chat.slice();
    if (S.packet) extras.splice(Math.min(S.packet.after || 0, extras.length), 0, { packet: true, at: S.packet.at || 0 });
    const order = extras.map((x, i) => [x, i]).sort((p, q) => (p[0].at - q[0].at) || (p[1] - q[1]));
    const out = []; let i = 0;
    order.forEach(([x]) => {
      while (i < Math.min(x.at, m.length)) out.push(m[i++]);
      if (x.packet) { out.push({ t: 'packet' }); return; }
      if (x.q) out.push({ t: 'user', text: x.q });
      out.push(x.a ? { t: 'bot', text: x.a + (x.sources.length ? '\n\nSource: ' + x.sources.join('; ') : '') } : { t: 'thinking', text: 'Checking the law' });
    });
    while (i < m.length) out.push(m[i++]);
    return { m: out, chips, kase: { title, status, res, diy, T: { where }, sent: S.step >= 6, hasEvidence: !!S.photo, stage: stageOf() } };
  };

  user(S.typedFirst ? S.desc : '+ ' + T.label);
  m.push({ t: 'system', text: T.title });

  /* address */
  bot("Case started. First, what's your address? I'll check your building's public record. You can skip this.");
  if (S.addrError) { user(S.addrError); bot(S.addrDown ? RECORDS_DOWN + ' Or skip this.' : NO_ADDRESS); }
  if (S.building && !S.addrLate) { user(S.address); bot(buildingLine(S.building)); }
  else if (S.addrSkipped === 'tapped') user('Skip');
  else if (!S.addrSkipped) { chips = [{ label: 'Skip', go: go({ addrSkipped: 'tapped' }) }]; return done(); }

  /* evidence */
  bot(T.ask);
  if (S.error) bot(S.errorKind === 'file' ? S.error : "I couldn't reach the model just now (" + S.error + '). Add the photo again.');
  if (!S.photo) { chips = [{ label: 'Pick a test photo', go: openSamples }]; return done(); }
  m.push({ t: 'photo', tag: S.isVideo ? 'Your video' : 'Your photo' });
  status = 'Checking';
  if (!S.analysis) return done();

  const a = S.analysis;
  if (a.from_cache) bot(a.cache_note);
  if (a.media_type === 'video') bot('I looked at ' + a.video.frames_analysed + ' moments across your ' + Math.round(a.video.duration_s) + '-second video.');
  const more = [{ label: 'Pick a test photo', go: openSamples }];

  if (a.nothing_found) {
    if (a.unclear.length) a.unclear.forEach((u) => bot("I might be seeing something here, but I can't confirm it from this photo: " + u.what_was_seen + '\n\n' + u.request));
    else if (a.out_of_scope) bot(a.out_of_scope.description + "\n\nThat isn't one of the housing problems I check yet." + (a.out_of_scope.tenant_responsibility ? ' It looks like something a tenant would usually take care of themselves.' : ''));
    else bot("I don't see a housing problem in this " + (S.isVideo ? 'video' : 'photo') + '. If there is one, try a closer shot in good light.');
    status = 'Nothing found'; chips = more; return done();
  }

  a.findings.forEach((f) => bot(f.description || f.title));
  const said = Object.entries(a.facts_from_description || {});
  if (said.length) bot('From what you wrote, I noted: ' + said.map(([k, v]) => k.replace(/_/g, ' ') + ' — ' + (v === true ? 'yes' : v === false ? 'no' : v)).join('; ') + '.');
  S.qa.forEach((x) => { bot(x.q); user(x.a); });

  /* a question that changes the answer comes first */
  const pend = pendingQuestion();
  if (pend) {
    const askF = pend.f, q = pend.q;
    bot(q.question + (q.type === 'number' && q.fact !== 'mold_area_sqft' ? ' Type the number.' : ''));
    if (q.type === 'bool') chips = [['Yes', true], ['No', false]].map(([l, v]) => ({ label: l, go: () => answer(q.fact, v, l, q.question) }));
    else if (q.type === 'enum') chips = (q.options || []).map((o) => ({ label: o, go: () => answer(q.fact, o, o, q.question) }));
    else if (q.fact === 'mold_area_sqft') chips = MOULD_SIZES.map(([l, v]) => ({ label: l, go: () => answer(q.fact, v, l, q.question) }));
    chips.push({ label: 'Not sure', go: () => notSure(q) }); // every question can be passed, so no case is left stuck on one
    if (askF.retake_request) bot('Or add a clearer photo. ' + askF.retake_request);
    if (q.fact === 'year_built' && !S.building) bot("Or type your address and I'll look it up.");
    title = askF.title; status = 'One question to answer';
    return done();
  }
  // a finding whose questions were all passed: say what it could be, and that the steps don't change
  const unsettled = (f) => {
    const cls = [...new Set((f.possible_outcomes || []).map((o) => o.class).filter(Boolean))].sort();
    return "Without that, I can't say which class this would be" + (cls.length ? ' (it could be Class ' + (cls.length > 1 ? cls.slice(0, -1).join(', ') + ' or ' : '') + cls[cls.length - 1] + ')' : '') +
      '. The steps are the same either way: tell your landlord in writing, then file with 311 so HPD inspects.';
  };

  /* tenant's own duty: offer the fix-it-yourself kit */
  const diyF = a.findings.find((f) => f.outcome === 'not_landlord_responsibility');
  const violations = a.findings.filter((f) => f.outcome === 'violation' || f.outcome === 'inspector_decides');
  if (diyF && !violations.length) {
    title = diyF.title; status = 'Not a violation · yours to fix'; diy = true; where = diyF.where;
    bot("Then it's not a violation. " + (diyF.scenario ? diyF.scenario + ': t' : 'T') + "hat is usually the tenant's to clean.");
    bot('Would you like to fix it yourself?');
    const again = diyF.rule_id === 'EO-015' ? "If it comes back fast or spreads past the tile, film it again. That can mean a leak behind the wall, and that's your landlord's job." : null;
    if (!S.diyChoice) { chips = [{ label: 'Fix it myself', go: () => fetchKit(diyF.rule_id) }, { label: 'No thanks', go: go({ diyChoice: 'no' }) }]; return done(); }
    user(S.diyChoice === 'yes' ? 'Fix it myself' : 'No thanks');
    if (S.diyChoice === 'yes' && S.kit) {
      if (S.kit.error) bot("I couldn't load the product list just now.");
      else {
        bot("Here's what you need. Tap “I have this” on anything you already own.");
        m.push({ t: 'kit' });
        if (S.kit.steps && S.kit.steps.length) bot('How to do it\n' + S.kit.steps.map((s, i) => (i + 1) + '. ' + s).join('\n'));
      }
    }
    if (again && (S.diyChoice === 'no' || S.kit)) bot(again);
    chips = [];
    return done();
  }

  /* nothing the landlord has to fix, and nothing to ask */
  if (!violations.length) {
    a.findings.forEach((f) => bot(f.outcome === 'no_violation'
      ? "From what I can see and what you've told me, this isn't a violation" + (f.scenario ? ': ' + f.scenario.toLowerCase() + '.' : '.')
      : f.outcome === 'needs_answer' ? unsettled(f)
      : "I can see the problem, but the sources I have don't settle how HPD would class it. The steps are the same: tell your landlord in writing, then file with 311 so HPD inspects."));
    title = a.findings[0].title; status = 'Checked'; chips = more; return done();
  }

  /* possible violation(s) */
  const all = violations.map(resFrom);
  res = all[0]; title = res.title + (all.length > 1 ? ' + ' + (all.length - 1) + ' more' : ''); where = res.f.where; status = res.cls + ' · new';
  all.forEach((r) => m.push({ t: 'finding', res: r }));
  if (S.explained) all.forEach((r) => { if (r.f.explanation) bot(r.f.explanation.summary); });
  else m.push({ t: 'thinking', text: 'Reading the law for this' });
  if (S.explainFailed) bot("I couldn't load the plain-language explanation just now. The class and deadline above come from the rules, so they still stand.");
  const q = res.f.photo_quality || a.photo_quality;
  if (q && !q.good_for_evidence) bot('For your records, a better ' + (S.isVideo ? 'shot' : 'photo') + ' would make stronger evidence:\n' + q.retake_requests.map((r) => '• ' + r).join('\n'));
  a.unclear.forEach((u) => bot("I may also be seeing something else, but I can't confirm it: " + u.what_was_seen + '\n\n' + u.request));
  a.findings.filter((f) => f.outcome === 'needs_answer').forEach((f) => bot(f.title + ': ' + unsettled(f)));
  if (!S.building && S.addrSkipped === 'auto') bot("If you type your address, I'll add your building's public record to this case.");
  if (S.step === 4) {
    chips = [{ label: 'What do I do now?', go: () => { set({ step: 5 }, 500); fetchLetter(); } }];
    if (S.explainFailed) chips.push({ label: 'Explain the law again', go: () => { set({ explained: false, explainFailed: false }); explain(S.analysis); } });
    if (!S.asked) chips.push({ label: 'Will I get in trouble?', go: () => { S.chat.push({ q: 'Will I get in trouble for complaining?', a: RETALIATION, sources: [], at: lastBase }); set({ asked: true }); } });
    if (!S.packet || S.packet.error) chips.push({ label: 'Build my case file', dark: true, go: buildPacket });
  }
  if (S.step >= 5) {
    user('What do I do now?');
    if ((res.f.next_steps || []).some((s) => s.path === 'Get it fixed')) { bot('Here is the path for this problem, in order:'); m.push({ t: 'steps', f: res.f }); }
    bot('Start with step 1: tell your landlord in writing. HPD and Housing Court both expect that first. I drafted it for you. Keep a copy and proof it was delivered.');
    m.push({ t: 'draft', title });
    status = res.cls + ' · notice ready';
    if (S.step === 5) chips = [{ label: 'I sent it', go: go({ step: 6 }) }];
  }
  if (S.step >= 6) {
    user('I sent it');
    bot("Saved to your case. I'll check in on Dec 5. If it isn't fixed by then, we'll file a 311 complaint together so HPD inspects.");
    status = res.cls + ' · waiting on landlord';
    if (S.step === 6) chips = [{ label: 'Skip to Dec 5', dark: true, go: go({ step: 7 }) }, { label: 'Open my case', go: () => set({ view: 'case' }) }];
  }

  /* ---------- escalation walk-through: notice → 311 → HPD inspection → violation → HP action ---------- */
  const inspector = res.label === 'Inspector decides';
  vClass = inspector ? 'Class B' : res.cls;
  // The walk-through's inspection is on Dec 18. The deadline runs from there for as long as this finding's own
  // rule gives (a Class C can be 24 hours, 14 or 21 days), not a fixed 30 days.
  const dl = inspector ? { value: 30, unit: 'days' } : (res.f.deadline || {});
  const noGrace = dl.unit === 'none';
  const dueIn = dl.unit === 'days' && dl.value ? dl.value : dl.unit === 'hours' ? Math.ceil((dl.value || 24) / 24) : noGrace ? 1 : 30;
  dueDate = new Date(2026, 11, 18 + dueIn).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  const verify = (when) => {
    fixedOn = when;
    user('Fixed');
    bot('Good news. Send a photo of the repaired spot so your case has proof it was done.');
    if (!S.verified) chips = [];
    else {
      m.push({ t: 'photo', tag: 'Photo · after the repair', after: true });
      bot('Case closed. It stays in your record, so if the problem comes back you can reopen it with the full history.');
      m.push({ t: 'system', text: title, closed: true });
      status = 'Resolved · ' + when; chips = [];
    }
  };
  if (S.step >= 7) {
    m.push({ t: 'date', text: 'Dec 5 · check-in (a preview of what comes next)' });
    bot("It's Dec 5. Did your landlord fix it?");
    if (S.step === 7 && !S.fixed) chips = [{ label: 'Not fixed', go: go({ step: 8 }) }, { label: 'Fixed', go: go({ fixed: true }) }];
    if (S.step === 7 && S.fixed) verify('Dec 5');
  }
  if (S.step >= 8) {
    user('Not fixed');
    bot("Then it's time to file with 311, so HPD sends an inspector. Here's your complaint. Paste it into 311 online, or read it out on the phone.");
    m.push({ t: 'complaint', title });
    bot("When you file, you'll get a service request number. Keep it: it's how the inspection is tracked.");
    status = res.cls + ' · file with 311';
    if (S.step === 8) chips = [{ label: 'I filed it', go: go({ step: 9 }) }];
  }
  if (S.step >= 9) {
    user('Filed');
    bot("Saved to your case. HPD aims to inspect within 30 days. If the inspector can't get in, call 311 within 10 days to reschedule.\n\nYour landlord can't punish you for this complaint.");
    status = res.cls + ' · waiting for inspection';
    if (S.step === 9) chips = [{ label: 'Skip to the inspection', dark: true, go: go({ step: 10 }) }];
  }
  if (S.step >= 10) {
    m.push({ t: 'date', text: 'Dec 18 · inspection' });
    bot('How did the HPD inspection go?');
    if (S.missed) { user("The inspector couldn't get in"); bot('Call 311 within 10 days to reschedule, and give them your service request number.'); }
    if (S.step === 10) {
      chips = [{ label: 'Violation issued', go: go({ step: 11, insp: 'violation' }) }, { label: 'No violation', go: go({ step: 11, insp: 'none' }) }];
      if (!S.missed) chips.push({ label: "Couldn't get in", go: go({ missed: true }) });
    }
  }
  if (S.step >= 11 && S.insp === 'violation') {
    user('They issued a violation');
    if (inspector) bot("HPD issued a violation, and the inspector set its class. It's now public on HPDONLINE, and your landlord's deadline starts today: 90 days for Class A, 30 days for Class B, 24 hours for Class C. For this walk-through, say it was Class B: fix by " + dueDate + '.\n\nThis is the official record a court will look at.');
    else bot('HPD issued a ' + vClass + " violation. It's now public on HPDONLINE, and " + (noGrace ? 'there is no grace period for this one: penalties run from today' : "your landlord's deadline starts today: fix by " + dueDate) + '.\n\nThis is the official record a court will look at.');
    status = vClass + ' violation · fix by ' + dueDate;
    if (S.step === 11) chips = [{ label: 'Skip to ' + dueDate, dark: true, go: go({ step: 12 }) }];
  }
  if (S.step >= 11 && S.insp === 'none') {
    user('No violation');
    bot("That happens. If the problem is still there, you don't have to stop. When HPD hasn't issued a violation within 30 days of your complaint, you can ask Housing Court to order the repair. That's called an HP action.");
    status = res.cls + ' · no violation issued';
    if (S.step === 11) chips = [{ label: 'Go to Housing Court', go: go({ step: 13 }) }];
  }
  if (S.step >= 12 && S.insp === 'violation') {
    m.push({ t: 'date', text: dueDate + ' · deadline' });
    bot("Today was your landlord's deadline. Did they fix it?");
    if (S.step === 12 && !S.fixed) chips = [{ label: 'Not fixed', go: go({ step: 13 }) }, { label: 'Fixed', go: go({ fixed: true }) }];
    if (S.step === 12 && S.fixed) verify(dueDate);
  }
  if (S.step >= 13) {
    user(S.insp === 'none' ? 'Go to Housing Court' : 'Not fixed');
    bot("Then you can ask Housing Court to order the repair. That's an HP action. The court clerk gives you the forms, and your case already has most of what the judge will want to see:");
    m.push({ t: 'checklist' });
    bot('You also have the right to talk to a free tenant lawyer before you go.' + (S.building && S.building.rent_stabilized ? "\n\nBecause your building is rent-stabilized, you can also ask DHCR to lower your rent until it's fixed." : ''));
    status = 'HP action · Housing Court';
    chips = S.packet && !S.packet.error ? [{ label: 'Open my case', dark: true, go: () => set({ view: 'case' }) }] : [{ label: 'Build my case file', dark: true, go: buildPacket }];
  }
  return done();
}

/* ---------- message rendering ---------- */
const safeUrl = (u) => (typeof u === 'string' && /^https:\/\//.test(u) ? u : null);
function fmtTime(s) { return Math.floor(s / 60) + ':' + String(Math.round(s % 60)).padStart(2, '0'); }

function kitHTML() {
  const k = S.kit;
  return `<div class="prodwrap kit"><span class="prodcap">Fix it yourself · from Shopify stores</span>
    <div class="prodrow" role="list">${k.items.map((it, i) => {
      const p = it.product, owned = !!S.owned[i], buy = p && (safeUrl(p.checkout_url) || safeUrl(p.url)), img = p && safeUrl(p.image);
      return `<div class="prod${owned ? ' owned' : ''}" role="listitem">
        <span class="prodimg">${img ? `<img src="${esc(img)}" alt="" loading="lazy">` : ''}</span>
        <b class="prodname">${esc(it.name)}</b>
        ${p ? `<span class="prodsub ttl">${esc(p.title)}</span><span class="prodsub">${esc(p.seller || '')}</span><span class="prodprice">$${Number(p.price).toFixed(2)}</span>` : '<span class="prodsub">Not found right now</span>'}
        <span class="prodact">${buy ? `<a class="buy" href="${esc(buy)}" target="_blank" rel="noopener noreferrer">${owned ? 'Not needed' : 'Buy'}</a>` : ''}<button class="have" data-have="${i}">${owned ? 'Add it back' : 'I have this'}</button></span></div>`;
    }).join('')}</div></div>`;
}

function packetSub(p) {
  const secs = p.started ? Math.round((Date.now() - p.started) / 1000) : 0;
  return p.error ? p.error : p.markdown ? 'From HPD’s public record · built in ' + Math.round(p.seconds) + ' s' : 'An agent is reading your building’s HPD record · ' + secs + ' s';
}

function msgHTML(x) {
  switch (x.t) {
    case 'bot': return `<div class="row"><div class="bot">${esc(x.text)}</div></div>`;
    case 'user': return `<div class="row me"><div class="user">${esc(x.text)}</div></div>`;
    case 'thinking': return `<div class="row"><div class="bot"><span style="color:var(--muted)">${esc(x.text)} </span><span class="typing"><i></i><i></i><i></i></span></div></div>`;
    case 'photo': {
      const src = x.after ? S.afterPhoto : S.photo;
      const media = !src ? ICON.xph(220, 170) : (S.isVideo && !x.after) ? `<video src="${esc(src)}" muted playsinline controls style="width:100%;height:auto;max-height:290px;display:block"></video>` : `<img src="${esc(src)}" alt="Your photo" style="height:auto;max-height:290px">`;
      return `<div class="row me"><div class="ph" style="width:220px;${src ? '' : 'height:170px'}">${media}<span class="tag">${esc(x.tag)}</span></div></div>`;
    }
    case 'system': return `<button class="sys" data-act="case"><span style="text-align:center;max-width:75%">${x.closed ? 'Case resolved' : 'Case started'}: <b style="color:#111111">${esc(x.text)}</b> · Open</span></button>`;
    case 'date': return `<div style="text-align:center;padding:10px 0 2px"><span style="font-size:12px;font-weight:600;color:var(--muted);border:1px solid var(--line2);border-radius:999px;padding:3px 10px">${esc(x.text)}</span></div>`;
    case 'finding': {
      const f = x.res.f, c = (f.citations || [])[0];
      const law = c ? c.citation : (f.hpd_order ? 'HPD order ' + f.hpd_order : 'NYC Housing Maintenance Code');
      const lc = { 'Settled': 'green', 'Inspector decides': 'blue', "From HPD's records": 'grey', 'Not settled': 'orange' }[x.res.label] || 'grey';
      const frame = f.frame ? `<div class="ph" style="height:120px"><img src="${esc(f.frame.url)}" alt=""><span class="tag">Clearest at ${fmtTime(f.frame.time_s)}${f.seen_at_s && f.seen_at_s.length > 1 ? ' · seen ' + f.seen_at_s.length + ' times' : ''}</span></div>` : '';
      return `<div class="row"><div class="card fcard">
        <div class="fhead"><span class="sugic">${ICON.scale}</span><span class="sugtxt" style="flex:1"><b>Possible violation</b><span>${esc(f.title)}</span></span></div>
        ${frame}
        <div class="grid2"><div class="ftile"><span class="big">${esc(x.res.cls)}</span><span class="sub">${esc(x.res.sub)}</span></div><div class="ftile"><span class="big">${esc(x.res.days)}</span><span class="sub">${esc(x.res.daysSub)}</span></div></div>
        <span class="stage ${lc}" style="margin-top:0">${esc(x.res.label)}</span>
        <button class="frule" data-act="rule"><span>${esc(law)} · See the rule</span>${ICON.arrowNE}</button>
        <span class="sub" style="line-height:1.4">Not an official finding. Only an HPD inspector can issue a violation.</span></div></div>`;
    }
    case 'draft': {
      const l = S.letter, owner = S.building && S.building.owner ? S.building.owner : '[Landlord / management]';
      const body = !l ? '<span class="typing"><i></i><i></i><i></i></span>' : l.error ? esc("I couldn't draft the letter: " + l.error) : esc(l.letter);
      const thumb = !S.isVideo && S.photo;
      return `<div class="row"><div class="card fcard">
        <div class="fhead"><span class="sugic">${ICON.mail}</span><span class="sugtxt" style="flex:1"><b>Letter to your landlord</b><span>Draft · you send it</span></span></div>
        <div class="ftile fmeta"><span><span class="sub">To</span>${esc(owner)}</span><span><span class="sub">Subject</span>Repair request: ${esc(x.title)}</span></div>
        <div class="letter fbody">${body}</div>
        ${thumb ? `<div class="fattach"><img src="${esc(thumb)}" alt=""><span class="sub">Photo attached</span></div>` : ''}
        <div class="factions"><button class="fbtn" data-act="copy-letter">Copy</button><button class="fbtn primary" data-act="mail">Open in email</button></div></div></div>`;
    }
    case 'complaint': {
      const l = S.letter;
      return `<div class="row"><div class="card fcard">
        <div class="fhead"><span class="sugic">${ICON.megaphone}</span><span class="sugtxt" style="flex:1"><b>311 complaint</b><span>Ready to file · goes to HPD</span></span></div>
        <div class="letter fbody" style="max-height:160px">${l && l.complaint_311 ? esc(l.complaint_311) : esc(x.title)}</div>
        <div class="factions"><button class="fbtn" data-act="copy-311">Copy text</button><a class="fbtn primary" href="https://portal.311.nyc.gov/" target="_blank" rel="noopener noreferrer">Open 311 online</a></div></div></div>`;
    }
    case 'checklist': {
      const items = [['Dated photos and video', true], ['Written notice to landlord · Nov 21', S.step >= 6], ['311 service request number', S.step >= 9],
        ['HPD violation number (HPDONLINE)', S.insp === 'violation'], ["Your building's HPD record", !!(S.packet && S.packet.markdown)], ['Proof the notice was delivered', false],
        ['Lease and rent receipts', false], ['How it affects you, in your words', false]];
      const n = items.filter((i) => i[1]).length;
      return `<div class="row"><div class="card fcard">
        <div class="fhead"><span class="sugic">${ICON.list}</span><span class="sugtxt" style="flex:1"><b>Evidence for court</b><span>${n} of ${items.length} ready</span></span></div>
        <div class="progress"><div style="width:${Math.round(n / items.length * 100)}%;background:var(--yellow)"></div></div>
        <div class="flist">${items.map(([label, ok]) => `<div class="fitem"><span class="fcheck${ok ? ' ok' : ''}">${ok ? ICON.check : ''}</span><span style="flex:1${ok ? '' : ';color:var(--soft)'}">${esc(label)}</span></div>`).join('')}</div>
      </div></div>`;
    }
    case 'packet': {
      const p = S.packet, sub = packetSub(p);
      return `<div class="row"><div class="card fcard">
        <div class="fhead"><span class="sugic">${ICON.doc}</span><span class="sugtxt" style="flex:1;min-width:0"><b>Case file${p.markdown ? ' ready' : p.error ? '' : ' in progress'}</b><span id="packet-sub" style="white-space:normal">${esc(sub)}</span></span>${p.markdown || p.error ? '' : '<span class="typing"><i></i><i></i><i></i></span>'}</div>
        ${p.markdown ? '<div class="factions"><button class="fbtn primary" data-act="packet">Open the case file</button></div>' : ''}</div></div>`;
    }
    case 'steps': {
      const steps = (x.f.next_steps || []).filter((s) => s.path === 'Get it fixed');
      return `<div class="row"><div class="card fcard">
        <div class="fhead"><span class="sugic">${ICON.list}</span><span class="sugtxt" style="flex:1"><b>What to do, in order</b><span>From the rules for this problem</span></span></div>
        <div class="flist">${steps.map((s, i) => `<div class="fitem" style="align-items:flex-start;padding:9px 0"><span class="fcheck ok" style="font-size:12px;font-weight:700">${i + 1}</span><span style="flex:1"><b style="display:block">${esc(s.title)}</b>${s.when ? `<span class="sub" style="display:block;font-size:12px;line-height:1.35">${esc(s.when)}</span>` : ''}</span></div>`).join('')}</div>
      </div></div>`;
    }
    case 'kit': return kitHTML();
  }
  return '';
}

/* ---------- views ---------- */
function chatView(conv) {
  const { m, chips, kase } = conv;
  const pin = kase ? `<button class="pin" data-act="case"><span class="ic">${ICON.doc}</span><span style="flex:1;min-width:0"><b>${esc(kase.title)}</b><small>${esc(kase.status)}</small></span>${ICON.chev}</button>` : '';
  const typing = S.typing ? `<div class="row"><div class="bot">${S.busy ? `<span id="busy" style="color:var(--muted)">${esc(S.busy)} </span>` : ''}<span class="typing"><i></i><i></i><i></i></span></div></div>` : '';
  const needAddr = S.type && !S.building && !S.addrSkipped;
  const a0 = S.analysis, q0 = a0 && (((a0.findings[0] || {}).photo_quality) || a0.photo_quality);
  const wantsRetake = a0 && (a0.nothing_found || a0.unclear.length || a0.findings.some((f) => f.retake_request || f.outcome === 'not_landlord_responsibility') || (q0 && !q0.good_for_evidence));
  const attachLabel = (S.fixed && !S.verified) ? 'Add photo of the repair' : S.type && !needAddr && !S.photo ? 'Add photo or video' : wantsRetake && S.step <= 4 ? 'Add another photo' : null;
  const pend = pendingQuestion();
  const placeholder = conv.empty ? "Tell us what's wrong at home" : needAddr ? 'Your address, like 122 W 167th St, Bronx' : pend && pend.q.type === 'number' ? 'Type a number' : S.analysis ? (S.building ? 'Ask a question about your case' : 'Ask a question, or type your address') : 'Add a photo, or ask a question';
  return `
    <div class="nav">
      <button class="navbtn" aria-label="Your cases" data-act="cases">${ICON.doc}${kase ? '<span class="count" aria-hidden="true">1</span>' : ''}</button>
      <span class="navtitle"></span>
      ${kase ? `<button class="navbtn" aria-label="Start a new case" data-act="new">${ICON.compose}</button>` : '<span></span>'}
    </div>
    ${conv.empty ? `
    <div class="hero"><h1>Your rights as a tenant, made simple.</h1></div>
    <div class="sugrow" role="list" aria-label="Start a case">
      ${SUGGEST.map((k) => `<button class="sugcard" role="listitem" data-type="${k}"><span class="sugic">${TYPE_ICON[k]}</span><span class="sugtxt"><b>${esc(TYPES[k].label)}</b><span>${esc(TYPES[k].hint)}</span></span></button>`).join('')}
    </div>`
    : `<div class="chatarea">
      ${pin ? `<div class="pinwrap">${pin}</div>` : ''}
      <div class="scroll${pin ? ' haspin' : ''}" id="scroll">${m.map(msgHTML).join('')}${typing}</div>
    </div>
    <div class="chips${chips.every((c) => c.label.length <= 18) ? ' inline' : ''}">${S.typing ? '' : chips.map((c, i) => `<button class="chip${c.dark ? ' dark' : ''}" data-chip="${i}"><span>${esc(c.label)}</span>${ICON.arrowNE}</button>`).join('')}</div>`}
    <form class="composer" id="composer">
      ${S.attachMenu ? `<div role="menu" aria-label="Add a photo or video" style="display:flex;flex-direction:column;align-items:flex-start;gap:8px;margin-left:-8px">
        <button type="button" class="cbtn wide" role="menuitem" data-act="pick-file">${ICON.cam}<span>Take or upload a photo or video</span></button>
        <button type="button" class="cbtn wide" role="menuitem" data-act="pick-sample">${ICON.plus(20)}<span>Use a sample photo</span></button>
      </div>` : ''}
      <input type="text" id="msg" aria-label="Message" placeholder="${esc(placeholder)}" autocomplete="off">
      <div class="composer-row">
        ${attachLabel
          ? `<button type="button" class="cbtn wide" data-act="attach">${ICON.cam}<span>${attachLabel}</span></button>`
          : `<button type="button" class="cbtn" aria-label="Add photo or video" data-act="attach">${ICON.plus(20)}</button>`}
        <span style="flex:1"></span>
        <button type="submit" class="csend" aria-label="Send">${ICON.arrowUp}</button>
      </div>
    </form>`;
}

function homeLine() {
  const b = S.building;
  if (!b) return ['No address added', 'Add your address when you start a case'];
  const bits = [];
  if (b.rent_stabilized) bits.push('Rent-stabilized');
  if (b.building_kind === 'nycha') bits.push('NYCHA');
  if (b.year_built) bits.push('built ' + b.year_built);
  if (b.units_res) bits.push(b.units_res + ' homes');
  return [b.address.replace(', USA', ''), bits.join(' · ')];
}

function caseView(kase) {
  if (!kase) return '';
  const r = kase.res, g = kase.stage;
  const [statusMain, statusSub] =
    g.resolved ? ['Resolved', 'Repair confirmed with a photo · ' + g.fixedOn]
    : g.court ? ['HP action · Housing Court', S.packet && S.packet.markdown ? 'Case file ready' : 'Build the case file in the chat']
    : g.violation ? ['HPD ' + g.vClass + ' violation', 'Landlord must fix by ' + g.dueDate]
    : g.noViolation ? ['No violation issued', 'You can still start an HP action']
    : g.filed ? ['Waiting for HPD inspection', '311 filed Dec 5 · HPD aims to inspect within 30 days']
    : g.filing ? ['File with 311', 'Complaint text ready in the chat']
    : kase.sent ? ['Waiting on landlord', 'Notice sent Nov 21 · follow up Dec 5']
    : kase.diy ? ['Yours to fix', 'Not a violation']
    : r ? ['Notice not sent yet', 'Ask “What do I do now?” in the chat']
    : kase.hasEvidence ? ['Checking', 'Answer the question in the chat']
    : ['Add evidence', 'Photos or a short video'];
  const stepNow = g.court ? 4 : (g.violation || g.noViolation) ? 3 : g.filed || g.filing ? 2 : 1;
  const c = r && (r.f.citations || [])[0];
  const finding = r ? `<div class="boxed">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:8px"><span class="eyebrow">Possible violation</span><span class="chip-lbl">${esc(r.label)}</span></div>
      <div class="grid2"><div><span class="big">${esc(r.cls)}</span><div class="sub">${esc(r.sub)}</div></div><div><span class="big">${esc(r.days)}</span><div class="sub">${esc(r.daysSub)}</div></div></div>
      <span style="font-size:13px">${c ? esc(c.citation) : 'NYC Housing Maintenance Code'} · <a href="#" data-act="rule" style="font-weight:600">See the rule</a></span>
    </div>` : kase.diy ? '<div class="boxed"><span class="eyebrow">Result</span><b style="font-size:15px">Not a violation</b><span class="sub" style="font-size:13px">This is usually the tenant’s to clean. Film it again if it spreads.</span></div>'
    : `<div class="boxed"><span class="eyebrow">Not checked yet</span><span class="sub" style="font-size:13px">${kase.hasEvidence ? 'Answer the question in the chat to finish the check.' : 'Add a photo in the chat. Tenard will check it against the rules.'}</span></div>`;
  const steps = r ? `<div class="section" style="gap:0"><span class="eyebrow" style="padding-bottom:10px">Steps</span>
      <div class="step"><div class="rail"><span class="dot${kase.sent ? ' done' : ''}">${kase.sent ? ICON.check : '1'}</span><span class="ln"></span></div><div class="txt"><b>Written notice to landlord</b><span>${kase.sent ? 'Sent Nov 21' : 'Draft it in the chat'}</span></div></div>
      <div class="step"><div class="rail"><span class="dot${g.filed ? ' done' : ''}">${g.filed ? ICON.check : '2'}</span><span class="ln"></span></div><div class="txt"><b>311 complaint → HPD inspection</b><span>${g.filed ? 'Filed Dec 5' : 'If it isn’t fixed · HPD aims to inspect within 30 days'}</span></div></div>
      <div class="step"><div class="rail"><span class="dot${g.violation ? ' done' : ''}">${g.violation ? ICON.check : '3'}</span><span class="ln"></span></div><div class="txt"><b>HPD issues a violation</b><span>${g.violation ? g.vClass + ' · issued Dec 18 · fix by ' + g.dueDate : g.noViolation ? 'Inspected Dec 18 · no violation issued' : 'The landlord’s deadline starts'}</span></div></div>
      <div class="step"><div class="rail"><span class="dot${g.court ? ' done' : ''}">${g.court ? ICON.check : '4'}</span></div><div class="txt"><b>HP action in Housing Court</b><span>${g.court ? 'Started' : 'If the violation isn’t fixed'}</span></div></div>
    </div>` : '';
  const home = homeLine();
  return `
    <div class="nav">
      <button class="back" data-act="chat">${ICON.back}Chat</button>
      <span class="navtitle">Case</span>
      <button class="navbtn" aria-label="Your cases" data-act="cases">${ICON.doc}</button>
    </div>
    <div class="page">
      <div class="section" style="gap:4px"><h1 style="margin:0;font-size:24px">${esc(kase.title)}</h1><span class="sub" style="font-size:13px">${esc(home[0])} · started Nov 21</span></div>
      <div class="boxed strong" style="flex-direction:row;justify-content:space-between;align-items:center;padding:12px 14px">
        <span style="display:flex;flex-direction:column;gap:2px"><b style="font-size:15px">${esc(statusMain)}</b><span class="sub" style="font-size:13px">${esc(statusSub)}</span></span>
        ${g.resolved ? '<span class="badge">Closed</span>' : r ? `<span class="badge">Step ${stepNow} of 4</span>` : ''}</div>
      ${kase.hasEvidence && !S.isVideo ? `<div class="ph" style="margin:14px 20px 0;height:150px"><img src="${esc(S.photo)}" alt="Evidence photo"><span class="tag">Evidence · Nov 21</span></div>` : ''}
      ${finding}
      ${steps}
      ${S.packet && S.packet.markdown ? '<button class="boxed" data-act="packet" style="background:#fff;text-align:left;margin-top:8px"><b style="font-size:14px">Case file</b><span class="sub" style="font-size:13px">Your building’s HPD record, matched to this case · Open</span></button>' : ''}
      <div class="section"><span class="eyebrow">Timeline</span>
        ${g.resolved ? `<div class="tl"><span>Repair confirmed with a photo</span><span>${g.fixedOn}</span></div>` : ''}
        ${g.court ? `<div class="tl"><span>HP action started</span><span>${g.noViolation ? 'Jan 5' : g.dueDate}</span></div>` : ''}
        ${g.violation ? `<div class="tl"><span>HPD ${g.vClass} violation issued</span><span>Dec 18</span></div>` : ''}
        ${g.noViolation ? '<div class="tl"><span>HPD inspection: no violation</span><span>Dec 18</span></div>' : ''}
        ${g.filed ? '<div class="tl"><span>311 complaint filed</span><span>Dec 5</span></div>' : ''}
        ${kase.sent ? '<div class="tl"><span>Notice sent to landlord</span><span>Nov 21</span></div>' : ''}
        ${kase.hasEvidence ? '<div class="tl"><span>Photo added and checked</span><span>Nov 21</span></div>' : ''}
        <div class="tl"><span>Case started</span><span>Nov 21</span></div>
      </div>
    </div>
    <div class="foot"><button class="primary-btn" data-act="chat">Continue in chat</button></div>`;
}

function sheetView(kase) {
  const card = (title, sub, stage, color, act) => `<${act ? `button data-act="${act}"` : 'div'} class="casecard"><b style="font-size:16px">${esc(title)}</b><span class="sub" style="font-size:13px">${esc(sub)}</span><span class="stage ${color}">${esc(stage)}</span></${act ? 'button' : 'div'}>`;
  const g = kase && kase.stage;
  const [stage, color] = !kase ? [] : g.resolved ? ['Fixed', 'green'] : g.court ? ['Housing Court', 'red'] : g.violation ? ['HPD violation', 'orange']
    : g.noViolation ? ['No violation issued', 'orange'] : g.filed ? ['Inspection pending', 'blue'] : g.filing ? ['File with 311', 'yellow']
    : kase.sent ? ['Waiting on landlord', 'yellow'] : kase.diy ? ['Yours to fix', 'grey'] : kase.res ? ['Possible violation', 'yellow'] : ['New', 'grey'];
  const sub = kase ? (kase.res ? kase.res.cls + ' · started Nov 21' : 'Started Nov 21') : '';
  const currentCard = kase ? card(kase.title, sub, stage, color, 'open-case') : '';
  const home = homeLine();
  return `
    <div class="nav">
      <button class="back" data-act="close-sheet">${ICON.back}${S.prevView === 'case' ? 'Case' : 'Chat'}</button>
      <h1 class="navtitle" style="margin:0">Your cases</h1>
      <span></span>
    </div>
    <div class="cases-page">
      <div class="sheet-body">
        <div class="home"><span class="sugic">${ICON.house}</span><span class="sugtxt" style="flex:1"><b>${esc(home[0])}</b><span>${esc(home[1])}</span></span></div>
        <span class="eyebrow" style="padding-top:6px">${kase && g.resolved ? 'Closed' : 'Open'}</span>
        ${currentCard || '<span class="sub" style="font-size:14px">No cases yet.</span>'}
        <a class="casecard" href="/proof.html" style="text-decoration:none;margin-top:8px"><b style="font-size:15px">How we tested Tenard</b><span class="sub" style="font-size:13px">175 photos and 22 videos, against a single model call</span></a>
      </div>
      <div class="sheet-foot"><button class="primary-btn" data-act="new">${ICON.plus(20)} New case</button></div>
    </div>`;
}

function samplesView() {
  const items = S.samples;
  return `
    <div class="nav"><button class="back" data-act="chat">${ICON.back}Chat</button><h1 class="navtitle" style="margin:0">Test photos</h1><span></span></div>
    <div class="page" style="padding:0 16px 16px">
      <p class="sub" style="font-size:13px;margin:4px 4px 12px">These are the held-out test photos. Some show a problem, some show nothing, and some only look like one. Pick any.</p>
      ${!items ? '<span class="typing"><i></i><i></i><i></i></span>' : !items.length ? '<span class="sub">The test photos aren’t on this machine. Add your own with +.</span>'
        : `<div class="samples">${items.map((it) => `<button data-sample="${esc(it.id)}" aria-label="Test photo"><img src="${esc(it.url)}" alt="" loading="lazy"></button>`).join('')}</div>`}
    </div>`;
}

function ruleView(kase) {
  const fs = (S.analysis ? S.analysis.findings : []).filter((f) => f.rule_id);
  const body = fs.map((f) => {
    const e = f.explanation;
    const quotes = (f.citations || []).map((c) => `<blockquote class="quote">“${esc(c.quote)}”<footer>${safeUrl(c.source_url) ? `<a href="${esc(c.source_url)}" target="_blank" rel="noopener noreferrer">${esc(c.citation)}</a>` : esc(c.citation)}<span class="checked">${ICON.check} checked word for word</span></footer></blockquote>`).join('');
    return `<div class="section"><span class="eyebrow">${esc(f.title)}</span>
      ${e ? `<p class="rulep">${esc(e.summary)}</p>` : '<p class="rulep sub">Reading the law for this… <span class="typing"><i></i><i></i><i></i></span></p>'}
      ${quotes}
      ${e ? `<b class="ruleh">What the landlord must do</b><p class="rulep">${esc(e.landlord_duties)}</p><b class="ruleh">Your rights</b><p class="rulep">${esc(e.tenant_rights)}</p><b class="ruleh">Your part</b><p class="rulep">${esc(e.tenant_responsibilities)}</p>` : ''}
      ${f.scenario ? `<span class="sub" style="font-size:12px">Matched situation: ${esc(f.scenario)}${f.hpd_order ? ' · HPD order ' + esc(f.hpd_order) : ''}</span>` : ''}</div>`;
  }).join('');
  return `
    <div class="nav"><button class="back" data-act="chat">${ICON.back}Chat</button><h1 class="navtitle" style="margin:0">The rule</h1><span></span></div>
    <div class="page">${body || '<div class="section"><span class="sub">No rule to show yet.</span></div>'}
      <div class="section"><span class="sub" style="font-size:12px;line-height:1.4">Every quote is copied from the law and checked against the section it cites. This explains the law; it is not legal advice.</span></div></div>`;
}

/* a small Markdown reader for the case file: headings, lists, tables, bold. Everything is escaped first. */
function md(src) {
  const inline = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/`([^`]+)`/g, '<code>$1</code>');
  const out = []; const lines = src.split('\n'); let i = 0;
  while (i < lines.length) {
    const l = lines[i];
    if (/^\s*$/.test(l)) { i++; continue; }
    const h = l.match(/^(#{1,4})\s+(.*)$/);
    if (h) { out.push(`<h${h[1].length + 1}>${inline(h[2])}</h${h[1].length + 1}>`); i++; continue; }
    if (/^\s*---+\s*$/.test(l)) { out.push('<hr>'); i++; continue; }
    if (/^\s*\|/.test(l)) {
      const rows = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) { rows.push(lines[i].trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim())); i++; }
      const body = rows.filter((r) => !r.every((c) => /^:?-+:?$/.test(c)));
      out.push('<div class="mdtable"><table>' + body.map((r, n) => '<tr>' + r.map((c) => (n === 0 ? '<th>' + inline(c) + '</th>' : '<td>' + inline(c) + '</td>')).join('') + '</tr>').join('') + '</table></div>');
      continue;
    }
    if (/^\s*([-*]|\d+\.)\s+/.test(l)) {
      const ordered = /^\s*\d+\./.test(l); const items = [];
      while (i < lines.length && /^\s*([-*]|\d+\.)\s+/.test(lines[i])) { items.push('<li>' + inline(lines[i].replace(/^\s*([-*]|\d+\.)\s+/, '')) + '</li>'); i++; }
      out.push((ordered ? '<ol>' : '<ul>') + items.join('') + (ordered ? '</ol>' : '</ul>'));
      continue;
    }
    out.push('<p>' + inline(l) + '</p>'); i++;
  }
  return out.join('');
}
function packetView() {
  const p = S.packet;
  return `
    <div class="nav"><button class="back" data-act="chat">${ICON.back}Chat</button><h1 class="navtitle" style="margin:0">Case file</h1><span></span></div>
    <div class="page"><div class="md">${p && p.markdown ? md(p.markdown) : '<p>Not ready yet.</p>'}</div></div>`;
}

let lastChips = [], lastCount = -1, lastView = null;
function render() {
  const app = document.getElementById('app');
  const conv = conversation();
  lastChips = conv.chips;
  // The page is rebuilt whole, and replies arrive while the tenant is typing or reading. Carry over the
  // half-typed message and the cursor; and if nothing new was said and they had scrolled up, stay there.
  const box = document.getElementById('msg'), was = document.getElementById('scroll');
  const typed = box ? { text: box.value, focus: document.activeElement === box, from: box.selectionStart, to: box.selectionEnd } : null;
  const count = conv.m.length + (S.typing ? 1 : 0);
  const stay = was && S.view === lastView && count === lastCount && was.scrollHeight - was.scrollTop - was.clientHeight > 60 ? was.scrollTop : null;
  lastCount = count; lastView = S.view;
  const base = S.view === 'cases' ? sheetView(conv.kase)
    : S.view === 'samples' ? samplesView()
    : S.view === 'rule' ? ruleView(conv.kase)
    : S.view === 'packet' ? packetView()
    : S.view === 'case' && conv.kase ? caseView(conv.kase) : chatView(conv);
  app.innerHTML = STATUS_BAR + base + '<div class="homebar" aria-hidden="true"></div>';
  const now = document.getElementById('msg');
  if (now && typed) {
    now.value = typed.text;
    if (typed.focus) { now.focus(); try { now.setSelectionRange(typed.from, typed.to); } catch (e) { /* not every input type has a selection */ } }
  }
  const sc = document.getElementById('scroll');
  if (sc) {
    const kit = S.showKit && sc.querySelector('.kit');
    if (kit) { sc.scrollTop = Math.max(0, kit.offsetTop - 70); } else sc.scrollTop = stay === null ? sc.scrollHeight : stay;
  }
}

/* ---------- events ---------- */
const SKIP_WORDS = /^(skip|no|nope|no thanks?|no thank you|not now|pass|i'?d rather not)[.!]?$/i;
const UNSURE = /^(not sure|unsure|i'?m not sure|i (don'?t|do not) know|don'?t know|no idea|idk|skip)[.!]?$/i;
const STREET = /\b(st|street|ave|avenue|rd|road|blvd|boulevard|pl|place|pkwy|parkway|dr|drive|ct|court|ln|lane|ter|terrace|broadway|bowery|concourse|tpke|turnpike|hwy|highway|bronx|brooklyn|queens|manhattan|staten island)\b/i;
function startCase(type, typedDesc) { run++; set({ type, step: 1, desc: typedDesc || null, typedFirst: !!typedDesc }, 400); }
function copyText(text, el) {
  const done = () => { el.textContent = 'Copied'; };
  if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, done); else done();
}

document.addEventListener('click', (e) => {
  const sug = e.target.closest('[data-type]');
  if (sug) { startCase(sug.dataset.type); return; }
  const sample = e.target.closest('[data-sample]');
  if (sample) {
    const id = sample.dataset.sample;
    if (!S.type) { run++; Object.assign(S, { type: 'other', typedFirst: false }); }
    if (!S.building && !S.addrSkipped) S.addrSkipped = 'auto'; // moved on without an address; it can still be typed later
    Object.assign(S, { view: 'chat', photo: '/api/photos/' + id, photoId: id, file: null, isVideo: false, analysis: null, answers: {}, qa: [], skipped: {}, error: null, diyChoice: null, kit: null, owned: {}, step: 2 });
    analyse(); return;
  }
  const have = e.target.closest('[data-have]');
  if (have) { const i = have.dataset.have; S.owned[i] = !S.owned[i]; S.showKit = true; render(); return; }
  const chip = e.target.closest('[data-chip]');
  if (chip) {
    const c = lastChips[+chip.dataset.chip];
    if (!c) return;
    S.showKit = false;
    if (c.attach) { S.awaitVerify = !!c.verify; document.getElementById('file').click(); } else c.go();
    return;
  }
  const a = e.target.closest('[data-act]');
  if (!a) return;
  e.preventDefault();
  const act = a.dataset.act;
  if (act === 'case') { if (S.type) set({ view: 'case' }); else set({ prevView: S.view, view: 'cases' }); }
  else if (act === 'cases') set({ prevView: S.view, view: 'cases' });
  else if (act === 'close-sheet') set({ view: S.prevView || 'chat' });
  else if (act === 'open-case') set({ view: 'case' });
  else if (act === 'chat') set({ view: 'chat' });
  else if (act === 'rule') set({ view: 'rule' });
  else if (act === 'packet') set({ view: 'packet' });
  else if (act === 'new') reset();
  else if (act === 'attach') {
    // a photo of the finished repair goes straight to the camera; otherwise offer a sample as well
    if (S.fixed && !S.verified) { S.awaitVerify = true; document.getElementById('file').click(); } else showAttachMenu(!S.attachMenu);
  }
  else if (act === 'pick-file') { S.awaitVerify = false; document.getElementById('file').click(); showAttachMenu(false); }
  else if (act === 'pick-sample') { S.attachMenu = false; openSamples(); }
  else if (act === 'copy-letter') { if (S.letter && S.letter.letter) copyText(S.letter.letter, a); }
  else if (act === 'copy-311') { if (S.letter && S.letter.complaint_311) copyText(S.letter.complaint_311, a); }
  else if (act === 'mail') { if (S.letter && S.letter.letter) window.location.href = 'mailto:?subject=' + encodeURIComponent('Repair request') + '&body=' + encodeURIComponent(S.letter.letter); }
});

document.addEventListener('submit', (e) => {
  if (e.target.id !== 'composer') return;
  e.preventDefault();
  const box = document.getElementById('msg'), v = box.value.trim();
  if (!v) return;
  box.value = ''; // render() now keeps what is in the box, so a sent message has to be cleared here
  const isQuestion = /\?\s*$/.test(v), houseNumberFirst = /^\s*\d/.test(v);
  // 1. The first message opens the case, and is answered: it is usually a description or a question.
  if (!S.type) { startCase(guessType(v), v); ask(v, { silent: true, at: 2 }); return; }
  // 2. The app has just asked for the address. An address starts with a house number; "skip" skips; anything
  //    else is a question and is answered as one (it used to be sent to the geocoder, which always finds something).
  if (!S.building && !S.addrSkipped) {
    if (SKIP_WORDS.test(v)) { set({ addrSkipped: 'tapped' }, 400); return; }
    if (houseNumberFirst && !isQuestion) { lookupAddress(v); return; }
    ask(v); return;
  }
  // 3. The app is waiting on one of its own questions: "yes", "no", a number or "not sure" answers it.
  const pend = pendingQuestion();
  if (pend) {
    if (UNSURE.test(v)) { notSure(pend.q); return; }
    const reply = typedAnswer(pend.q, v);
    if (reply) { answer(pend.q.fact, reply[0], v, pend.q.question); return; }
  }
  // 4. An address typed later, when it was skipped at the start or a photo came first.
  if (!S.building && houseNumberFirst && !isQuestion && STREET.test(v)) { lookupAddress(v, true); return; }
  // 5. Everything else is a question.
  if (!S.analysis) S.notes.push(v); // said before the photo: sent along with it, and read for facts
  ask(v);
});

document.getElementById('file').addEventListener('change', (e) => {
  const f = e.target.files && e.target.files[0];
  if (!f) return;
  const url = URL.createObjectURL(f);
  e.target.value = '';
  if (S.awaitVerify) { set({ verified: true, afterPhoto: url, awaitVerify: false }, 500); return; }
  if (!S.type) { run++; Object.assign(S, { type: 'other', typedFirst: false }); }
  if (!S.building && !S.addrSkipped) S.addrSkipped = 'auto'; // moved on without an address; it can still be typed later
  const isVideo = (f.type || '').startsWith('video/') || (!f.type && /\.(mp4|mov|webm|m4v|3gp|mkv|avi)$/i.test(f.name));
  Object.assign(S, { photo: url, file: f, isVideo, photoId: null, analysis: null, answers: {}, qa: [], skipped: {}, error: null, diyChoice: null, kit: null, owned: {}, step: 2, view: 'chat' });
  analyse();
});

render();
