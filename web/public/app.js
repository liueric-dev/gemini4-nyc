/* Tenard: the app's front end. Design, icons and views from the team's prototype (github.com/hey-niia/tenard,
   commit 03fb082); live logic below. Served as-is; no build step. */
const ICON = {
  arrowNE: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>',
  house: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10.5L12 4l8 6.5V19a1 1 0 0 1-1 1h-4.5v-5.5h-5V20H5a1 1 0 0 1-1-1z"/></svg>',
  mic: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
  arrowUp: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
  compose: '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-6"/><path d="M17.5 3.5a2.1 2.1 0 0 1 3 3L12 15l-4 1 1-4z"/></svg>',
  back: '<svg width="13" height="22" viewBox="0 0 13 22" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 2L2 11l9 9"/></svg>',
  doc: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></svg>',
  menu: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
  chev: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>',
  up: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg>',
  x: '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  cam: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>',
  send: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  check: '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>',
  plus: (s) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>`,
  xph: (w, h) => `<svg width="100%" height="100%" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0L${w} ${h}M${w} 0L0 ${h}" stroke="#DDDDDD" stroke-width="1"/></svg>`
};
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const HPD = "from HPD's violation";

const TI = (d) => `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
const TYPE_ICON = {
  mould: TI('<circle cx="8" cy="9" r="2.5"/><circle cx="15.5" cy="7.5" r="1.5"/><circle cx="14" cy="15" r="3"/><circle cx="7" cy="16.5" r="1.2"/>'),
  leak: TI('<path d="M12 3.5s6 6.4 6 10.5a6 6 0 0 1-12 0c0-4.1 6-10.5 6-10.5z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>'),
  paint: TI('<rect x="4" y="4" width="13" height="5" rx="1.5"/><path d="M17 6.5h2.5V12H11v3"/><rect x="9.5" y="15" width="3" height="5.5" rx="1"/>'),
  window: TI('<rect x="5" y="3.5" width="14" height="17" rx="1.5"/><path d="M12 3.5v17M5 12h14M8 15.5v5M16 15.5v5"/>'),
  detector: TI('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 4v1.5M12 18.5V20"/>')
};
const STATUS_BAR = `<div class="statusbar" aria-hidden="true"><span class="time">9:41</span><span class="sb-icons">
  <svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1" fill="currentColor"/><rect x="5" y="5.5" width="3" height="6.5" rx="1" fill="currentColor"/><rect x="10" y="3" width="3" height="9" rx="1" fill="currentColor"/><rect x="15" y="0" width="3" height="12" rx="1" fill="currentColor"/></svg>
  <svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 2.4c2.3 0 4.4.9 6 2.4l1.2-1.3A10.4 10.4 0 0 0 8 .6 10.4 10.4 0 0 0 .8 3.5L2 4.8a8.6 8.6 0 0 1 6-2.4zm0 3.5c1.3 0 2.5.5 3.5 1.3l1.2-1.3A7 7 0 0 0 8 4.1 7 7 0 0 0 3.3 5.9l1.2 1.3A5.2 5.2 0 0 1 8 5.9zm0 3.4c.4 0 .8.1 1.1.4L8 11.4 6.9 9.7c.3-.3.7-.4 1.1-.4z" fill="currentColor"/></svg>
  <svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="23" height="12" rx="3.5" fill="none" stroke="currentColor" opacity=".4"/><rect x="2" y="2" width="20" height="9" rx="2" fill="currentColor"/><path d="M25 4.5v4c.8-.3 1.3-1.1 1.3-2s-.5-1.7-1.3-2z" fill="currentColor" opacity=".45"/></svg>
</span></div>`;

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
  address: null, building: null, addrError: null, addrSkipped: false,
  analysis: null, answers: {}, qa: [], explained: false, error: null, busy: null,
  asked: false, letter: null, diyChoice: null, kit: null, owned: {}, packet: null,
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
function reset() { run++; if (pollTimer) clearInterval(pollTimer); set(Object.assign({ view: 'chat' }, FRESH, { answers: {}, qa: [], owned: {} })); }

/* ---------- backend ---------- */
async function jfetch(url, opts) {
  const r = await fetch(url, opts);
  if (!r.ok) {
    let d = 'error ' + r.status;
    try { d = (await r.json()).detail || d; } catch (e) { /* keep the status */ }
    throw new Error(d);
  }
  return r.json();
}
const postJSON = (url, body) => jfetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });

async function lookupAddress(text) {
  const mine = run;
  Object.assign(S, { typing: true, busy: 'Looking up your building' }); render();
  let patch;
  try { patch = { building: await jfetch('/api/building?address=' + encodeURIComponent(text)), address: text, addrError: null }; }
  catch (e) { patch = { addrError: text }; }
  if (mine !== run) return;
  Object.assign(S, patch, { typing: false, busy: null }); render();
}

async function analyse() {
  const mine = run;
  Object.assign(S, { typing: true, error: null, busy: S.isVideo ? 'Watching your video' : 'Looking at your photo', showKit: false }); render();
  const f = new FormData();
  if (S.photoId) f.append('photo_id', S.photoId); else f.append('photo', S.file);
  if (S.building) f.append('address', S.address);
  f.append('answers', JSON.stringify(S.answers));
  f.append('explain', 'false');
  try {
    const a = await jfetch('/api/analyze', { method: 'POST', body: f });
    if (mine !== run) return;
    if (a.photo && !S.isVideo) S.photoId = a.photo.id; // follow-up answers reuse the saved upload
    Object.assign(S, { analysis: a, explained: false, letter: null, typing: false, busy: null, step: Math.max(S.step, 4) }); render();
    if (a.findings.some((x) => x.rule_id)) {
      const full = await postJSON('/api/explain', { analysis: a });
      if (mine === run && S.analysis === a) { Object.assign(S, { analysis: full, explained: true }); render(); }
    } else S.explained = true;
  } catch (e) {
    if (mine !== run) return;
    Object.assign(S, { typing: false, busy: null, error: String(e.message || e), photo: null, file: null, photoId: null, analysis: null }); render();
  }
}

function answer(fact, value, label, question) {
  S.answers[fact] = value;
  S.qa.push({ q: question, a: label });
  analyse();
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
  if (!S.building) { S.packet = { error: "I need your address to pull your building's record. Start a new case and add it." }; render(); return; }
  S.packet = { status: 'starting', started: Date.now() }; render();
  try {
    const r = await postJSON('/api/case-file', { analysis: S.analysis, apartment: null });
    if (mine !== run) return;
    S.packet = { status: 'in_progress', caseId: r.case_id, started: Date.now() }; render();
    pollTimer = setInterval(async () => {
      try {
        const s = await jfetch('/api/case-file/' + r.case_id);
        if (mine !== run) { clearInterval(pollTimer); return; }
        if (s.markdown) { clearInterval(pollTimer); S.packet = { status: 'done', markdown: s.markdown, seconds: s.seconds }; render(); }
        else if (!/progress|queued|running/i.test(s.status)) { clearInterval(pollTimer); S.packet = { error: 'The agent stopped (' + s.status + '). Try again.' }; render(); }
        else if (S.view === 'chat') render();
      } catch (e) { /* a dropped poll is fine; the next one retries */ }
    }, 5000);
  } catch (e) { if (mine === run) { S.packet = { error: String(e.message || e) }; render(); } }
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
  const done = () => {
    chips.push({ label: 'Start over', go: reset });
    return { m, chips, kase: { title, status, res, diy, T: { where }, sent: S.step >= 6, hasEvidence: !!S.photo, stage: stageOf() } };
  };

  user(S.typedFirst ? S.desc : '+ ' + T.label);
  m.push({ t: 'system', text: T.title });

  /* address */
  bot("Case started. First, what's your address? I'll check your building's public record. You can skip this.");
  if (S.addrError) { user(S.addrError); bot("I couldn't find that address in New York City. Try it with the borough, like “122 West 167th Street, Bronx”."); }
  if (S.building) { user(S.address); bot(buildingLine(S.building)); }
  else if (S.addrSkipped) user('Skip');
  else { chips = [{ label: 'Skip', go: go({ addrSkipped: true }) }]; return done(); }

  /* evidence */
  bot(T.ask);
  if (S.error) bot("I couldn't reach the model just now (" + S.error + '). Add the photo again.');
  if (!S.photo) { chips = [{ label: 'Add photo or video', attach: true }, { label: 'Pick a test photo', go: openSamples }]; return done(); }
  m.push({ t: 'photo', tag: S.isVideo ? 'Your video' : 'Your photo' });
  status = 'Checking';
  if (!S.analysis) return done();

  const a = S.analysis;
  if (a.from_cache) bot(a.cache_note);
  if (a.media_type === 'video') bot('I looked at ' + a.video.frames_analysed + ' moments across your ' + Math.round(a.video.duration_s) + '-second video.');
  const more = [{ label: 'Add another photo', attach: true }, { label: 'Pick a test photo', go: openSamples }];

  if (a.nothing_found) {
    if (a.unclear.length) a.unclear.forEach((u) => bot("I might be seeing something here, but I can't confirm it from this photo: " + u.what_was_seen + '\n\n' + u.request));
    else if (a.out_of_scope) bot(a.out_of_scope.description + "\n\nThat isn't one of the housing problems I check yet." + (a.out_of_scope.tenant_responsibility ? ' It looks like something a tenant would usually take care of themselves.' : ''));
    else bot("I don't see a housing problem in this " + (S.isVideo ? 'video' : 'photo') + '. If there is one, try a closer shot in good light.');
    status = 'Nothing found'; chips = more; return done();
  }

  a.findings.forEach((f) => bot(f.description || f.title));
  S.qa.forEach((x) => { bot(x.q); user(x.a); });

  /* a question that changes the answer comes first */
  const askF = a.findings.find((f) => f.outcome === 'needs_answer' && f.questions.length);
  if (askF) {
    const q = askF.questions[0];
    bot(q.question);
    if (q.type === 'bool') chips = [['Yes', true], ['No', false]].map(([l, v]) => ({ label: l, go: () => answer(q.fact, v, l, q.question) }));
    else if (q.type === 'enum') chips = (q.options || []).map((o) => ({ label: o, go: () => answer(q.fact, o, o, q.question) }));
    else if (q.fact === 'mold_area_sqft') chips = MOULD_SIZES.map(([l, v]) => ({ label: l, go: () => answer(q.fact, v, l, q.question) }));
    else S.awaitFact = { fact: q.fact, question: q.question };
    if (askF.retake_request) chips.push({ label: 'Add a clearer photo', attach: true });
    title = askF.title; status = 'One question to answer';
    return done();
  }
  S.awaitFact = null;

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
    chips = [{ label: 'Film it again', attach: true }];
    return done();
  }

  /* nothing the landlord has to fix, and nothing to ask */
  if (!violations.length) {
    a.findings.forEach((f) => bot(f.outcome === 'no_violation'
      ? "From what I can see and what you've told me, this isn't a violation" + (f.scenario ? ': ' + f.scenario.toLowerCase() + '.' : '.')
      : "I can see the problem, but the sources I have don't settle how HPD would class it. The steps are the same: tell your landlord in writing, then file with 311 so HPD inspects."));
    title = a.findings[0].title; status = 'Checked'; chips = more; return done();
  }

  /* possible violation(s) */
  const all = violations.map(resFrom);
  res = all[0]; title = res.title + (all.length > 1 ? ' + ' + (all.length - 1) + ' more' : ''); where = res.f.where; status = res.cls + ' · new';
  all.forEach((r) => m.push({ t: 'finding', res: r }));
  if (S.explained) all.forEach((r) => { if (r.f.explanation) bot(r.f.explanation.summary); });
  else m.push({ t: 'thinking', text: 'Reading the law for this' });
  const q = res.f.photo_quality || a.photo_quality;
  if (q && !q.good_for_evidence) bot('For your records, a better ' + (S.isVideo ? 'shot' : 'photo') + ' would make stronger evidence:\n' + q.retake_requests.map((r) => '• ' + r).join('\n'));
  a.unclear.forEach((u) => bot("I may also be seeing something else, but I can't confirm it: " + u.what_was_seen + '\n\n' + u.request));
  if (S.asked) {
    user('Will I get in trouble for complaining?');
    bot("It's illegal for your landlord to punish you for complaining. If they try to evict you or raise your rent within a year of a complaint or inspection, the law presumes it's retaliation (NY Real Property Law § 223-b).\n\nThis doesn't apply if the owner lives in a building with fewer than 4 units.");
  }
  if (S.packet) m.push({ t: 'packet' });
  if (S.step === 4) {
    chips = [{ label: 'What do I do now?', go: () => { set({ step: 5 }, 500); fetchLetter(); } }];
    if (!S.asked) chips.push({ label: 'Will I get in trouble?', go: go({ asked: true }) });
    if (!S.packet) chips.push({ label: 'Build my case file', dark: true, go: buildPacket });
    if (q && !q.good_for_evidence) chips.push({ label: 'Add a better photo', attach: true });
  }
  if (S.step >= 5) {
    user('What do I do now?');
    bot('Step 1: tell your landlord in writing. HPD and Housing Court both expect that first. I drafted it for you. Keep a copy and proof it was delivered.');
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
  vClass = res.label === 'Inspector decides' ? 'Class B' : res.cls;
  const vDays = res.label === 'Inspector decides' ? '30 days' : res.days;
  dueDate = { '21 days': 'Jan 8', '30 days': 'Jan 17', '90 days': 'Mar 18' }[vDays] || 'Jan 17';
  const verify = (when) => {
    fixedOn = when;
    user('Fixed');
    bot('Good news. Send a photo of the repaired spot so your case has proof it was done.');
    if (!S.verified) chips = [{ label: 'Add photo of the repair', attach: true, verify: true }];
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
    bot('HPD issued a ' + vClass + " violation. It's now public on HPDONLINE, and your landlord's deadline starts today: fix by " + dueDate + '.\n\nThis is the official record a court will look at.');
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
    chips = S.packet ? [{ label: 'Open my case', dark: true, go: () => set({ view: 'case' }) }] : [{ label: 'Build my case file', dark: true, go: buildPacket }];
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
      const law = c ? esc(c.citation) : (f.hpd_order ? 'HPD order ' + esc(f.hpd_order) : 'NYC Housing Maintenance Code');
      const frame = f.frame ? `<div class="ph" style="height:120px"><img src="${esc(f.frame.url)}" alt=""><span class="tag">Clearest at ${fmtTime(f.frame.time_s)}${f.seen_at_s && f.seen_at_s.length > 1 ? ' · seen ' + f.seen_at_s.length + ' times' : ''}</span></div>` : '';
      return `<div class="row"><div class="card"><div class="pad">
        <div style="display:flex;justify-content:space-between;align-items:center;gap:8px"><span class="eyebrow">Possible violation · ${esc(f.title)}</span><span class="chip-lbl">${esc(x.res.label)}</span></div>
        ${frame}
        <div class="grid2"><div class="tile"><span class="big">${esc(x.res.cls)}</span><span class="sub">${esc(x.res.sub)}</span></div><div class="tile"><span class="big">${esc(x.res.days)}</span><span class="sub">${esc(x.res.daysSub)}</span></div></div>
        <span style="font-size:13px">${law} · <a href="#" data-act="rule" style="font-weight:600">See the rule</a></span>
        <span class="sub" style="line-height:1.4">Not an official finding. Only an HPD inspector can issue a violation.</span></div></div></div>`;
    }
    case 'draft': {
      const l = S.letter, owner = S.building && S.building.owner ? S.building.owner : '[Landlord / management]';
      const body = !l ? '<span class="typing"><i></i><i></i><i></i></span>' : l.error ? esc("I couldn't draft the letter: " + l.error) : esc(l.letter);
      return `<div class="row"><div class="card">
        <div style="padding:10px 12px;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:2px;font-size:12px"><span><span style="color:var(--muted)">To: </span>${esc(owner)}</span><span><span style="color:var(--muted)">Subject: </span>Repair request: ${esc(x.title)}</span></div>
        <div class="letter">${body}</div>
        <div class="btnrow"><button data-act="copy-letter">Copy</button><button class="primary" data-act="mail">Open in email</button></div></div></div>`;
    }
    case 'complaint': {
      const l = S.letter;
      return `<div class="row"><div class="card">
        <div style="padding:10px 12px;border-bottom:1px solid var(--line)"><span class="eyebrow">311 complaint · ready to file</span></div>
        <div class="letter" style="max-height:160px">${l && l.complaint_311 ? esc(l.complaint_311) : esc(x.title)}</div>
        <div class="btnrow"><button data-act="copy-311">Copy text</button><a class="primary-link" href="https://portal.311.nyc.gov/" target="_blank" rel="noopener noreferrer">Open 311 online</a></div></div></div>`;
    }
    case 'checklist': {
      const items = [['Dated photos and video', true], ['Written notice to landlord · Nov 21', S.step >= 6], ['311 service request number', S.step >= 9],
        ['HPD violation number (HPDONLINE)', S.insp === 'violation'], ["Your building's HPD record", !!(S.packet && S.packet.markdown)], ['Proof the notice was delivered', false],
        ['Lease and rent receipts', false], ['How it affects you, in your words', false]];
      const n = items.filter((i) => i[1]).length;
      return `<div class="row"><div class="card">
        <div style="padding:10px 12px;display:flex;justify-content:space-between;align-items:center"><span class="eyebrow">Evidence for court</span><span class="sub">${n} of ${items.length} ready</span></div>
        ${items.map(([label, ok]) => `<div style="display:flex;gap:10px;align-items:center;padding:9px 12px;border-top:1px solid #EEEEEE;font-size:14px"><span style="width:20px;height:20px;border-radius:5px;flex-shrink:0;display:flex;align-items:center;justify-content:center;${ok ? 'background:#111111;color:var(--cream)' : 'border:1.5px solid #111111'}">${ok ? ICON.check : ''}</span><span style="flex:1${ok ? '' : ';color:var(--soft)'}">${esc(label)}</span></div>`).join('')}
      </div></div>`;
    }
    case 'packet': {
      const p = S.packet;
      const secs = p.started ? Math.round((Date.now() - p.started) / 1000) : 0;
      const sub = p.error ? esc(p.error) : p.markdown ? 'From HPD’s public record · built in ' + Math.round(p.seconds) + ' s' : 'An agent is reading your building’s HPD record · ' + secs + ' s';
      return `<div class="row"><div class="card" style="display:flex;gap:12px;align-items:center;padding:12px">
        <span style="width:40px;height:48px;border:1.5px solid #111111;border-radius:4px;flex-shrink:0;display:flex;align-items:center;justify-content:center">${ICON.doc}</span>
        <span style="flex:1;display:flex;flex-direction:column;gap:2px;min-width:0"><b style="font-size:14px">Case file${p.markdown ? ' ready' : p.error ? '' : ' in progress'}</b><span class="sub">${sub}</span></span>
        ${p.markdown ? '<button class="chip" style="min-height:36px" data-act="packet">Open</button>' : p.error ? '' : '<span class="typing"><i></i><i></i><i></i></span>'}</div></div>`;
    }
    case 'kit': return kitHTML();
  }
  return '';
}

/* ---------- views ---------- */
function chatView(conv) {
  const { m, chips, kase } = conv;
  const pin = kase ? `<button class="pin" data-act="case"><span class="ic">${ICON.doc}</span><span style="flex:1;min-width:0"><b>${esc(kase.title)}</b><small>${esc(kase.status)}</small></span>${ICON.chev}</button>` : '';
  const typing = S.typing ? `<div class="row"><div class="bot">${S.busy ? `<span style="color:var(--muted)">${esc(S.busy)} </span>` : ''}<span class="typing"><i></i><i></i><i></i></span></div></div>` : '';
  const needAddr = S.type && !S.building && !S.addrSkipped;
  const attachLabel = S.type && !needAddr && !S.photo ? 'Add photo or video' : (S.fixed && !S.verified) ? 'Add photo of the repair' : null;
  const placeholder = conv.empty ? "Tell us what's wrong at home" : needAddr ? 'Your address, like 122 W 167th St, Bronx' : S.awaitFact ? 'Type a number' : 'Add a photo or video with +';
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
    <div class="chips">${S.typing ? '' : chips.map((c, i) => `<button class="chip${c.dark ? ' dark' : ''}" data-chip="${i}"><span>${esc(c.label)}</span>${ICON.arrowNE}</button>`).join('')}</div>`}
    <form class="composer" id="composer">
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

let lastChips = [];
function render() {
  const app = document.getElementById('app');
  const conv = conversation();
  lastChips = conv.chips;
  const base = S.view === 'cases' ? sheetView(conv.kase)
    : S.view === 'samples' ? samplesView()
    : S.view === 'rule' ? ruleView(conv.kase)
    : S.view === 'packet' ? packetView()
    : S.view === 'case' && conv.kase ? caseView(conv.kase) : chatView(conv);
  app.innerHTML = STATUS_BAR + base + '<div class="homebar" aria-hidden="true"></div>';
  const sc = document.getElementById('scroll');
  if (sc) {
    const kit = S.showKit && sc.querySelector('.kit');
    if (kit) { sc.scrollTop = Math.max(0, kit.offsetTop - 70); } else sc.scrollTop = sc.scrollHeight;
  }
}

/* ---------- events ---------- */
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
    Object.assign(S, { view: 'chat', photo: '/api/photos/' + id, photoId: id, file: null, isVideo: false, analysis: null, answers: {}, qa: [], diyChoice: null, kit: null, owned: {}, step: 2 });
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
  else if (act === 'attach') { S.awaitVerify = !!(S.fixed && !S.verified); document.getElementById('file').click(); }
  else if (act === 'copy-letter') { if (S.letter && S.letter.letter) copyText(S.letter.letter, a); }
  else if (act === 'copy-311') { if (S.letter && S.letter.complaint_311) copyText(S.letter.complaint_311, a); }
  else if (act === 'mail') { if (S.letter && S.letter.letter) window.location.href = 'mailto:?subject=' + encodeURIComponent('Repair request') + '&body=' + encodeURIComponent(S.letter.letter); }
});

document.addEventListener('submit', (e) => {
  if (e.target.id !== 'composer') return;
  e.preventDefault();
  const v = document.getElementById('msg').value.trim();
  if (!v) return;
  if (!S.type) { startCase(guessType(v), v); return; }
  if (!S.building && !S.addrSkipped) { lookupAddress(v); return; }
  if (S.awaitFact) {
    const n = Number(v.replace(/[^0-9.]/g, ''));
    if (v.replace(/[^0-9.]/g, '') !== '' && Number.isFinite(n)) { const q = S.awaitFact; S.awaitFact = null; answer(q.fact, n, v, q.question); }
  }
});

document.getElementById('file').addEventListener('change', (e) => {
  const f = e.target.files && e.target.files[0];
  if (!f) return;
  const url = URL.createObjectURL(f);
  e.target.value = '';
  if (S.awaitVerify) { set({ verified: true, afterPhoto: url, awaitVerify: false }, 500); return; }
  if (!S.type) { run++; Object.assign(S, { type: 'other', typedFirst: false, addrSkipped: true }); }
  if (!S.building && !S.addrSkipped) S.addrSkipped = true;
  Object.assign(S, { photo: url, file: f, isVideo: (f.type || '').startsWith('video/'), photoId: null, analysis: null, answers: {}, qa: [], diyChoice: null, kit: null, owned: {}, step: 2, view: 'chat' });
  analyse();
});

render();
