# YT-Lessons — Project Notes

Teaching material built from short-form video (YouTube Shorts and similar). Static HTML, no build
step, no deps. `README.md` explains the architecture; this file is the agent-facing conventions.

Sibling repo: **YT-Knowledge** (`~/Projects/OpenCode/Youtube`) does research briefs from long-form
video. Different job — a brief is for recall, a lesson is for comprehension. Don't cross the
vocabularies: no conviction/badge/ticker language in a note, and never force a 300-word short
through the brief's theme structure.

## Repo
- **Remote:** https://github.com/hutuleac/YT-Lessons.git (`main`, no other branches)
- **Pages:** not enabled yet — no live URL. Enabling it is outward-facing, so ask first.
- Repo root should only ever gain built `<lesson-id>.html`, `<lesson-id>-deck.html` and the
  refreshed `index.html`.
  Transcripts live in `source-data/<lesson-id>/`.

## Creating notes and lessons
Use the **youtube-lessons** skill (`~/.claude/skills/youtube-lessons/SKILL.md`) for every new
short. Read it fresh each time. It handles batch ingestion (`ingest.py`), the note schema, when a
diagram earns its place, and the verification checklist.

Things that are easy to get wrong and are not obvious from the code:

- **Note ids are named after the concept, never the channel or video** — `dumb-zone`, not
  `pocock-3`. The library is cross-channel on purpose: a Charlie Automates short and a Pocock
  short on the same idea must be able to sit in one lesson. A later video that sharpens a concept
  **updates the existing note** rather than adding a second one.
- **`skeleton` and `mechanism` are the same content at two levels of detail**, not two drafts.
  A future deck renderer will use `skeleton` alone, so prose written into it breaks the deck.
- **`mechanism` explains why.** Restating the headline is not a mechanism. If the short doesn't
  give one, say so rather than inventing it.
- **Sponsor content never enters a note**, in any field. Same standing rule as the brief repo.
- **One short is one concept.** Don't manufacture a second to fill the schema; don't split one
  idea across two notes. If a short adds nothing to an existing note, write no note.

## Build
```bash
python3 build.py lessons/<id>.py   # one lesson + refresh index
python3 build.py --all             # everything
```
Every build writes two files per lesson: the scrollable page (`<id>.html`, from `mechanism`) and
the deck (`<id>-deck.html`, from `skeleton` alone — full-viewport scroll-snapped slides). A note
with an empty `skeleton` fails the build, because it would render a blank slide.

`build.py` is the renderer for every lesson and is **never edited per lesson** — per-video
changes go in notes. Same rule as `generate.py` in the brief repo.

The build enforces the concept graph rather than decorating it: it fails if a lesson lists a note
before one of its prerequisites, if a `prerequisites`/`related` id doesn't resolve to a real note,
or if a note's `id` doesn't match its filename. A failure on ordering means reorder the lesson,
not edit the note.

## Gotchas
- **`sys.dont_write_bytecode = True` in build.py is load-bearing.** Notes and lessons are data
  files loaded by path; a stale `.pyc` silently serves the previous version when an edit keeps the
  same byte size within the same second. Symptom: you edit a note, rebuild, nothing changes. If
  output ever looks stale: `find . -name __pycache__ -exec rm -rf {} +`.
- **SVG text scales with the plate.** Text is sized in user units, so a 340-wide viewBox stretched
  to 800px renders 10px text at 24px. `.plate svg` is capped at 560px for this reason. If diagram
  text looks wrong, check the viewBox, not the CSS.
- **Diagrams scroll, they don't shrink.** Below ~470px they'd compress until labels overflow their
  boxes, so `.plate` scrolls horizontally with `svg{min-width:420px}`. Page-level horizontal
  overflow must stay false.

## Design
Dark-first, light is a media-query override. Monospace display / serif body — the machine speaks
in mono, the teaching speaks in serif. Palette is a signal-degradation axis (teal signal, magenta
interference), deliberately not green-good/red-bad, because the subject is quality decaying across
a gradient. Signature element is the context rail that fills with scroll and crosses into the dumb
zone. Diagrams use CSS custom properties so they theme themselves; text uses `.d-label` `.d-num`
`.d-node` `.d-fix` and never hardcodes font-size.

Verify rendering with the **/browse** skill (never the Chrome MCP tools) — console errors, page
overflow at 390px, and both themes.

## Git conventions
- **Never add a `Co-Authored-By: Claude...` trailer** to commits in this repo.
- Commit and push after each lesson or batch of notes unless told otherwise.
- `__pycache__/`, `*.pyc`, `.DS_Store` are gitignored.
