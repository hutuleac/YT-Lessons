# YT-Lessons

Teaching material built from short-form video. Static HTML, no build step, no dependencies.

Companion to [YT-Knowledge](https://github.com/hutuleac/YT-Knowledge), which does research briefs
from long-form video. Different job: a brief is for recall, a lesson is for comprehension.

## The two units

**A note** (`notes/<id>.py`) is one short video, one concept. It is the durable thing — it owns its
own diagrams, numbers and sources, and it never changes when a lesson changes.

**A lesson** (`lessons/<id>.py`) is a manifest naming notes in teaching order, plus the connective
tissue between them.

A note can appear in any number of lessons. That is the whole point of the split: publish a
one-note lesson today, and when four more shorts on the same topic accumulate, recompile into a
bigger lesson without touching the original note.

## Build

```bash
python3 build.py lessons/context-engineering.py   # one lesson, plus refresh the index
python3 build.py --all                            # every lesson, plus the index
```

Writes `<lesson-id>.html` and `index.html` to the repo root.

## The concept graph is enforced

Notes declare `prerequisites`. A lesson that lists a note before one of its prerequisites fails
the build:

```
context-engineering.py: 'tool-overload' needs 'dumb-zone' first — reorder 'notes' in the lesson
```

The `builds on …` line under each section heading is rendered from that same field, so the
dependency shown to the reader is the one the build checked.

## Notes on the notes

- `skeleton` is deck-ready: short lines, no sub-clauses. `mechanism` is the page prose. Same
  content at two levels of detail, so a future deck renderer doesn't need the schema to change.
- Diagrams are inline SVG stored on the note, using CSS custom properties for colour so they
  theme themselves in light and dark. `notes/_svg.py` generates the ones not worth hand-writing.
- Sponsor segments never make it into a note.

## Design

Dark-first, light supported. Monospace display and serif body — the machine speaks in mono, the
teaching speaks in serif. The palette is a signal-degradation axis (teal signal, magenta
interference) rather than green-good/red-bad, because the subject is quality decaying across a
gradient rather than a pass/fail.

The signature element is the context rail down the left edge: it fills as you scroll and crosses
into the dumb zone near the end, so the page enacts the thing it explains.

## Gotcha

`build.py` sets `sys.dont_write_bytecode = True`. Notes and lessons are data files loaded by path,
and a stale `.pyc` will silently serve the previous version whenever an edit keeps the same byte
size within the same second — you edit a note, rebuild, and the page doesn't change. Don't remove
that line.
