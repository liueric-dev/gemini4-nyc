# What the backend returns

For whoever designs or builds the screens. The backend runs on port 8000; the web page in `web/` reaches it through `/api/...`.

A filled-in example of the main response is in [sample-response.json](sample-response.json). Design against that file: every field in it is one the backend will send.

## Endpoints

| Call | Status | What it does |
|---|---|---|
| `GET /api/health` | Working | Says whether the API, the keys and the database are ready |
| `GET /api/building?address=...` | Working | Address to building facts: year built, units, building type, rent-stabilized, open HPD violations |
| `POST /api/analyze` | Working | Photo (plus optional address and answers) to findings. This is the main one |
| `POST /api/explain` | Working | Adds the written explanation and checked quotes to an analysis made with `explain=false`. Takes `{"analysis": ...}` and returns it filled in |
| `POST /api/ask` | Working | Answers a question typed into the chat, using only the case, the rules and law for the kind of problem the question mentions, and the escalation steps. Takes `{"question": ..., "analysis": <optional /api/analyze response>, "history": <optional earlier exchange, [{"q": ..., "a": ...}]>}`; returns `answer`, `citations` and `covered` (false when there is no source, and the answer says so) |
| `GET /api/test-items` | Working | The held-out test photos, for the "pick a photo" grid. No labels are included |
| `GET /api/photos/{id}` | Working | The image for a test photo or an upload |
| `POST /api/case-file` | Working | Starts the case file agent. Returns a `case_id` at once |
| `GET /api/case-file/{case_id}` | Working | `status` is `in_progress` until the agent finishes (about 1 to 2 minutes); then `markdown` holds the case file |
| `POST /api/letter` | Working | Drafts the letter to the landlord and the 311 complaint text. Takes `{"analysis": <the /api/analyze response>, "tenant_name": ..., "apartment": ...}`; returns `letter`, `complaint_311` and `notes`. Instant: code fills it in, no model call |
| `GET /api/results` | Working | The evaluation numbers for the proof screen |

`POST /api/analyze` takes a form with `photo` (a file) or `photo_id` (a test photo's id), and optionally `address` and `answers` (a JSON object such as `{"child_under_6_resides": true}`).

**Photos.** Any format a phone sends is accepted, including HEIC. A photo wider than 1600 pixels is made smaller before the models see it, and a sideways one is turned upright. A file that isn't a photo or a video gets a 415 with a sentence to show the tenant.

**Follow-ups.** The response's `photo.id` identifies the upload (a photo or a video). To send answers or an address for the same picture, send `photo_id` with that id and no file. For half an hour the models' reading of the picture is reused, so a follow-up takes under a second and the findings can't change between an answer and the next.

`POST /api/analyze` also takes `note`: what the tenant typed. It is read for facts the rules use (a child's age, the year built) and returned as `facts_from_description`. It is never used to decide what the photo shows.

Each item in a finding's `next_steps` has `title` (what to do, in plain words), `who`, `how`, `when`, `path` (which goal it serves, such as "Get it fixed") and `code`. Show `title`; the code is only an id.

`POST /api/case-file` takes JSON: `{"analysis": <the whole /api/analyze response>, "apartment": "4B"}`. The analysis must include a building, so the photo has to be analysed with an address first.

## `POST /api/analyze`

Send a photo (or the id of a test photo), and optionally an address and answers to earlier questions. The response is the shape in `sample-response.json`.

A finding is one problem the app sees in the photo. Each finding has an `outcome`, and the screen should look different for each:

| `outcome` | Meaning | What to show |
|---|---|---|
| `violation` | The class and deadline are known | Class, deadline, the quoted law, next steps |
| `inspector_decides` | A violation, but HPD's inspector picks the class | The possible classes, the quoted law, next steps. No single deadline |
| `not_landlord_responsibility` | The rule says this is the tenant's own duty | A plain explanation. No class or deadline |
| `no_violation` | The facts mean it isn't a violation (for example, low indoor temperature outside heat season) | A plain explanation |
| `not_settled` | The sources don't settle the outcome | The next steps only, said honestly |
| `needs_answer` | The app needs a fact from the tenant first | The `questions` as a short form, and `possible_outcomes` (what it could turn out to be); send the answers back |

Other states the screens need:
- **Nothing found:** `nothing_found` is true and `findings` is empty.
- **Unclear, another photo needed:** `unclear` lists problems the app thought it saw but couldn't confirm. Each has `what_was_seen` and a `request` saying what photo to take next (for mould: closer, in good light, with something of known size in frame). These are not reported as problems. Show the request and let the tenant add a photo. A finding can also carry a `retake_request` next to its `questions`, when a clearer photo could answer the question (mould size is the main case).
- **Outside the decision tree:** `out_of_scope` describes what the photo shows and whether it looks like the tenant's responsibility. A product suggestion would attach here.
- **A weak photo:** `photo_quality` is present whenever a problem is reported. `good_for_evidence` is false when the photo is blurry or dark, too far away, shows no surroundings, or (for mould) has nothing to show scale. `retake_requests` lists what to fix, in plain words. The problem is still reported; this is advice for the tenant's own records.
- **Address not found:** the building call returns a 404 with a message. The geocoder's match is kept only if its house number is the one that was typed. A 503 means the city's records didn't answer, which is not the same thing; inside `/api/analyze` that case sets `building_error` and the photo is still answered.
- **Facts the app looks up itself:** the year built (from the building record; asked of the tenant when there is no address) and, for heat, the outdoor temperature (National Weather Service, Central Park).

## Video

`POST /api/analyze` also takes a video in the `photo` field (mp4, mov, webm and the other common formats, up to 100 MB). The app samples a still frame about every 3 seconds (at most 16), runs each through the photo pipeline, and reports a problem only if at least two frames confirm it. Sound is ignored.

The response has the same shape, with these additions:
- `media_type` is `"video"`, and `video` gives the duration, the frame times, and how many frames saw each problem.
- Each finding has `time_s` (its clearest moment), `seen_at_s` (every time it was seen), `time_range_s`, and `frame`, a saved still with a `url` you can show beside the finding.
- `photo_quality` is on each finding, for its clearest frame.

A video takes longer than a photo: roughly 15 to 40 seconds before the explanation, depending on length.

## Things the backend can't give you

- **Boxes on the photo.** The models describe where a problem is in words. They don't return coordinates.
- **A deadline date before HPD acts.** The deadline is a length of time (30 days), and the clock starts when HPD issues a violation notice. Don't show a calendar date as if it were already running.
- **One overall confidence.** There is a probability for each problem type.

## Timing

**To show the answer in two stages:** call `POST /api/analyze` with the form field `explain=false`. It returns the findings with class, deadline, questions and next steps, but no written explanation or quotes. Show that, then send the whole response to `POST /api/explain` and fill in each finding's `explanation` and `citations` when it returns.

**If the network fails:** for test photos, `/api/analyze` returns the last good answer for that photo with `from_cache: true` and a `cache_note`. Show the note when it's present.

Each citation has a `support` score (0 to 1) from a second check that the quote supports the statement. Quotes that fail it are removed before you see them.

A full answer takes about 10 to 15 seconds. The parts arrive at different times: detection in about 1 second, the description in about 6, the building facts in 1 to 5, and the law explanation last. Design each part to appear when it is ready.

## `GET /api/building`

Try it with one of the demo buildings:

| Address | What it shows |
|---|---|
| 122 West 167th Street, Bronx | Built 1929, 4 units |
| 39-06 114th Street, Queens | Rent-stabilized, 70 units |
| 466 Columbia Street, Brooklyn | NYCHA public housing |
| 1180 Mace Avenue, Bronx | A two-family house |
| 1048 Washington Avenue, Bronx | Built 1899, under a vacate order |

The rent-stabilized answer comes from a file that exists only on Eric's machine. Anywhere else it comes back as unknown (`null`).
