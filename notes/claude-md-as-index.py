NOTE = {
    "id": "claude-md-as-index",
    "concept": "CLAUDE.md is a contents page",
    "one_liner": "CLAUDE.md should hold only what's always true and Claude can't work out —"
                 " everything else becomes a pointer to a file Claude opens when it needs it.",

    "prerequisites": ["context-hierarchy"],
    "related": ["harness-bloat", "docs-drift", "skill-from-corrections"],

    "skeleton": [
        "Anthropic cut over 80% of Claude Code's own instructions for Opus 5.",
        "Most of them fixed mistakes older models made.",
        "Keep four things: unguessable commands, your differences, repeat gotchas, boundaries.",
        "Everything else is a pointer: a path, and when to open it.",
        "Point to every file directly. Nested files get partial reads.",
    ],

    "mechanism": [
        "Most instructions in an old CLAUDE.md were written to correct a model that no longer"
        " ships. Per the video, when Opus 5 shipped Anthropic deleted over 80% of Claude"
        " Code's own instructions for exactly that reason. The same audit applies to yours: a line that"
        " tells Claude to do what it already does is paid for on every request and makes the"
        " lines that matter easier to miss. Anthropic's docs, as the speaker cites them, already say to keep"
        " the file under 200 lines, because longer files cost more and get followed less.",

        "The reframe is to treat CLAUDE.md the way SKILL.md works inside a skill folder: a"
        " contents page, not the content. Four kinds of line still earn a place — the tools and"
        " commands Claude can't guess, anything you do differently from how Claude would by"
        " default, gotchas it has got wrong more than once, and boundaries (\"only write the"
        " email draft\"). Everything else becomes a pointer to a file Claude opens only when the"
        " work calls for it — progressive disclosure, with CLAUDE.md holding only what's always"
        " true.",

        "How the pointer is written decides whether that disclosure actually happens. An"
        " @-import loads the whole file into every session, which defeats the point; a path in"
        " backticks plus when to open it (\"read `docs/client-brief.md` before any client work\")"
        " lets Claude load it at the right moment. And per the speaker's reading of Anthropic's"
        " docs, a file reached only through another file gets its first 100 lines previewed, not"
        " read — so a chain of pointers silently truncates the detail at the end of it. Pointing"
        " to every file straight from CLAUDE.md, and putting a contents list at the top of"
        " anything over 100 lines, keeps a partial read from losing what matters. (Anthropic"
        " sets the contents-list rule for skill files; extending it to every file the index"
        " points at is the speaker's own practice.)",
    ],

    "numbers": [
        {"value": "80%+", "unit": "", "label": "of Claude Code's own instructions Anthropic"
                                               " deleted when Opus 5 shipped"},
        {"value": "200", "unit": "lines", "label": "Anthropic's ceiling for a CLAUDE.md"},
        {"value": "100", "unit": "lines", "label": "previewed from a file reached only through"
                                                   " another file — and the length past which a"
                                                   " file gets a contents list"},
        {"value": "4", "unit": "kinds of line", "label": "that still belong in CLAUDE.md itself"},
    ],

    "analogy": {
        "text": "Claude.md to me now is the contents page for your workspace. It's the same job"
                " that skill.md does inside a skill folder.",
        "note": "It turns \"what should CLAUDE.md say?\" into \"where does this live, and when"
                " should Claude go and get it?\" — a placement question instead of a writing one.",
    },

    "practice": [
        "Delete every line Claude follows without being told.",
        "Keep: commands it can't guess, your deviations, repeat gotchas, boundaries.",
        "Write pointers as a backticked path plus when to open it — never an @-import.",
        "Link every reference file straight from CLAUDE.md, not through another file.",
        "Put a contents list at the top of any referenced file over 100 lines.",
        "Run a prompt audit for stale-model instructions, dead paths and contradictions, and"
        " approve its cuts before it changes anything.",
    ],

    "diagrams": [
        {
            "title": "Three ways to point, three different reads",
            "caption": "An @-import is paid for every session; a nested pointer is read only in"
                       " part. A direct path, opened when needed, is the only one that gets the"
                       " whole file at the right time.",
            "svg": '''<svg viewBox="0 0 500 236" role="img"
  aria-label="CLAUDE.md as an index with three pointers. An at-import loads the whole file into every session. A backticked path with when to open it is opened on demand and read in full. A file reached only through another file gets only its first 100 lines previewed.">
  <rect x="0" y="86" width="120" height="48" rx="5" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="60" y="108" class="d-fix" text-anchor="middle">CLAUDE.md</text>
  <text x="60" y="124" class="d-label" text-anchor="middle">the index</text>

  <path d="M120 98 H140 V34 H170" fill="none" stroke="var(--interference)" stroke-width="1.4"/>
  <rect x="170" y="16" width="150" height="36" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="245" y="38" class="d-node" text-anchor="middle">@import file</text>
  <text x="332" y="31" class="d-label">loaded every</text>
  <text x="332" y="45" class="d-label">session &#8212; always paid</text>

  <path d="M120 110 H170" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="170" y="92" width="150" height="36" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="245" y="114" class="d-node" text-anchor="middle">`brief.md` + when</text>
  <text x="332" y="107" class="d-fix">opened on demand,</text>
  <text x="332" y="121" class="d-fix">read in full</text>

  <path d="M120 122 H140 V186 H170" fill="none" stroke="var(--line)" stroke-width="1.4"/>
  <rect x="170" y="168" width="70" height="36" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="205" y="190" class="d-node" text-anchor="middle">a.md</text>
  <path d="M240 186 H260" stroke="var(--line)" stroke-width="1.4"/>
  <rect x="260" y="168" width="60" height="36" rx="5" fill="none" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="290" y="190" class="d-node" text-anchor="middle">b.md</text>
  <text x="332" y="183" class="d-num">first 100 lines</text>
  <text x="332" y="197" class="d-label">previewed only</text>

  <text x="0" y="230" class="d-fix">every arrow starts at the index</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=J9NQTYUP6k0",
        "channel": "Simon Scrapes",
        "title": "How the Top 1% Use Claude Code Differently",
        "duration": "18:09",
    },
}
