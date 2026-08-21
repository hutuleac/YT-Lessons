# YT-Lessons — Project Notes

Teaching material built from short-form video (YouTube Shorts and similar). Static HTML, no build
step, no deps. `README.md` explains the architecture; this file is the agent-facing conventions.

Sibling repo: **YT-Knowledge** (`~/Projects/OpenCode/Youtube`) does research briefs from long-form
video. Different job — a brief is for recall, a lesson is for comprehension. Don't cross the
vocabularies: no conviction/badge/ticker language in a note, and never force a 300-word short
through the brief's theme structure.

## Repo
- **Remote:** https://github.com/hutuleac/YT-Lessons.git (`main`, no other branches)
- **Pages:** live at https://hutuleac.github.io/YT-Lessons/, serving off `main`.
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
Every build writes two files per lesson: the scrollable page (`<id>.html`) and the deck
(`<id>-deck.html`, full-viewport scroll-snapped slides).

The deck reads the slide-shaped fields — `skeleton`, `numbers`, `analogy`, `practice`,
`diagrams` — and **never `mechanism`**, whose paragraphs are exactly what makes a page a page.
One note becomes a divider, a bullets slide, a slide per diagram, and a slide per non-empty
field. A note with an empty `skeleton` fails the build, because it would render a blank slide.

`build.py` is the renderer for every lesson and is **never edited per lesson** — per-video
changes go in notes. Same rule as `generate.py` in the brief repo.

The build enforces the concept graph rather than decorating it: it fails if a lesson lists a note
before one of its prerequisites, if a `prerequisites`/`related` id doesn't resolve to a real note,
or if a note's `id` doesn't match its filename. A failure on ordering means reorder the lesson,
not edit the note.

A prerequisite **taught by a different lesson** is fine — the `builds on` line links out to that
lesson instead. Only a prerequisite no lesson covers fails the build. Don't pull a chain of
prerequisites into a lesson to satisfy the heading: that is how two lessons end up making the
same argument out of the same notes.

## Gotchas
- **`sys.dont_write_bytecode = True` in build.py is load-bearing.** Notes and lessons are data
  files loaded by path; a stale `.pyc` silently serves the previous version when an edit keeps the
  same byte size within the same second. Symptom: you edit a note, rebuild, nothing changes. If
  output ever looks stale: `find . -name __pycache__ -exec rm -rf {} +`.
- **SVG text scales with the plate.** Text is sized in user units, so a 340-wide viewBox stretched
  to 800px renders 10px text at 24px. `.plate svg` is capped at 820px (page) / a `clamp()` up to
  ~1400px (deck) for this reason — since it's vector, pushing the cap higher only makes labels
  more readable, never blurry. If diagram text looks wrong, check the viewBox, not the CSS.
- **Every size in `DECK_CSS` must be `clamp()`-based, no bare px.** `.slide h1`/`.bul li`/etc. all
  scale with `vw`; a plain `max-width:1040px` (as `.slide .plate svg` once had) freezes the moment
  the window passes that width while everything around it keeps growing. Symptom: diagrams look
  fine at 1440px but stay a fixed size past that while headings keep scaling — check windows
  2000px+, not just 1440px, when touching deck sizing.
- **Diagrams scroll, they don't shrink.** Below ~470px they'd compress until labels overflow their
  boxes, so `.plate` scrolls horizontally with `svg{min-width:420px}`. Page-level horizontal
  overflow must stay false.
- **Page width is `clamp()`-based, not a fixed max-width.** `--measure` (prose) and `--wide`
  (boxes/plates/lists) both scale with `vw` up to a cap (900px / 1360px), so the page keeps using
  more of a wide monitor instead of stranding content in a narrow column on anything past a
  laptop. A regression here only shows up at 1920px+ — checking 390px and 1440px won't catch it.
- **The deck (`<id>-deck.html`) has F/D/O/←→ controls, built once in `DECK_JS`/`DECK_CSS` in
  `build.py` — never per-lesson.** F toggles fullscreen, D toggles `data-theme` (persisted in
  `localStorage`), O toggles a keyboard-only overview grid (click a thumbnail to jump), ←/→ step
  one slide. If a feature request wants any of this changed, it's a `build.py` edit, not a note
  edit — same rule as `sys.dont_write_bytecode`, rebuild `--all` and re-verify with `/browse`
  before trusting it.
- **`.k-section`'s two-column layout (`grid-column`/`grid-row`, ≥1000px media query) corrupts
  flex siblings in overview mode — a real Chromium bug, not a spec violation.** Overview forces
  `display:flex` on `.slide` (via `html.overview .slide`) to override `.k-section`'s
  `display:grid`, which should make the leftover `grid-column`/`grid-row` on its children inert.
  Instead a preceding sibling collapses the next element's box to 0 height. Confirmed by isolating
  it to exactly `.k-section` + any 2+ children + `display:flex` — none of grid-column, grid-row,
  align-items, or align-content individually fixed it; only forcing `display:block` on
  `.k-section` in overview (`html.overview .k-section{display:block}`) did. If overview ever
  looks broken again (blank/overlapping cards) for section-divider slides specifically, this is
  the first thing to check — don't assume the new CSS is wrong before checking whether it's this.

## Design
Dark-first, light is a media-query override. Monospace display / serif body — the machine speaks
in mono, the teaching speaks in serif. Palette is a signal-degradation axis (teal signal, magenta
interference), deliberately not green-good/red-bad, because the subject is quality decaying across
a gradient. Signature element is the context rail that fills with scroll and crosses into the dumb
zone. Diagrams use CSS custom properties so they theme themselves; text uses `.d-label` `.d-num`
`.d-node` `.d-fix` and never hardcodes font-size.

Verify rendering with the **/browse** skill (never the Chrome MCP tools) — console errors, page
overflow at 390px, wide-monitor space usage at 1920px+, and both themes.

To screenshot one diagram among several: `nth-of-type` on `<figure>` breaks when they sit in
different parent sections (it resets per parent). Tag them first —
`$B js "document.querySelectorAll('figure').forEach((f,i)=>f.id='fig-'+i)"` — then
`$B screenshot out.png --selector "#fig-N"`.

## Git conventions
- **Never add a `Co-Authored-By: Claude...` trailer** to commits in this repo.
- Commit and push after each lesson or batch of notes unless told otherwise.
- `__pycache__/`, `*.pyc`, `.DS_Store` are gitignored.
