NOTE = {
    "id": "scheduled-routines",
    "concept": "Scheduled routines",
    "one_liner": "Give an agent recurring, low-stakes responsibilities on a schedule — a morning"
                 " brief, a weekly review — before ever letting it ship unsupervised, so the"
                 " boring-but-essential work happens without you remembering to ask for it."
                 ,

    "prerequisites": [],
    "related": ["repo-as-onboarding-packet", "permission-tiers"],

    "skeleton": [
        "Every business has boring, recurring work: read notes, spot patterns, flag risks.",
        "Start there, not with unsupervised production code.",
        "Morning brief: read customer notes and issues, write one page, don't touch code.",
        "Weekly review: group issues, name the week's highest-leverage fix, don't touch code.",
    ],

    "mechanism": [
        "The instinct once an agent can run on a schedule is to reach for the most dramatic"
        " version — shipping code while you sleep. The safer and more useful starting point is"
        " the opposite: hand it the kind of recurring work that's low-stakes precisely because it"
        " doesn't touch production, but that a business quietly depends on someone doing —"
        " reading customer notes, noticing which issues keep coming up, deciding what's worth"
        " working on next.",

        "A routine is that task, scoped and scheduled: read the customer and context folders,"
        " check open issues, write a summary to a specific file, with an explicit word cap and an"
        " explicit 'don't edit code, don't open a pull request.' The constraints are as load-"
        " bearing as the task — they're what makes a recurring agent safe to leave running"
        " unattended before you've built up trust in its judgment.",

        "The payoff compounds because the routine's output feeds the rest of the system: a morning"
        " brief surfaces the day's highest-priority item before you've opened the repo, and a"
        " weekly review can catch a pattern — the same onboarding complaint from three different"
        " customers — that no single note would have surfaced on its own.",
    ],

    "numbers": [
        {"value": "7:00am weekdays", "unit": "", "label": "morning brief schedule"},
        {"value": "500", "unit": "words", "label": "morning brief length cap"},
        {"value": "Fridays 3:00pm", "unit": "", "label": "weekly ops review schedule"},
    ],

    "analogy": None,

    "practice": [
        "Start scheduled work with a read-only routine — no code edits, no pull requests — before"
        " trusting an agent with anything that ships.",
        "Give every routine an explicit word or scope cap so it stays a brief, not a report.",
        "Point routines at the same context folders the rest of the system already reads and"
        " writes to, so their output compounds instead of living in isolation.",
    ],

    "diagrams": [
        {
            "title": "Two routines, same shape",
            "caption": "Read, summarize, write to a file — never touch code. The safety is in what"
                       " the routine is *not* allowed to do.",
            "svg": '''<svg viewBox="0 0 460 160" role="img"
  aria-label="Two scheduled routines. Morning brief, every weekday 7am, reads customer notes and issues, writes context slash morning-brief.md, under 500 words, no code edits. Weekly ops review, every Friday 3pm, groups issues and notes, writes context slash weekly-ops.md, no code edits.">
  <text x="0" y="14" class="d-label">MON&#8211;FRI 7AM</text>
  <rect x="0" y="22" width="200" height="80" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="10" y="40" class="d-label">read /customers, /context,</text>
  <text x="10" y="54" class="d-label">open issues</text>
  <text x="10" y="72" class="d-node">&#8594; morning-brief.md</text>
  <text x="10" y="90" class="d-fix">under 500 words, no code</text>

  <text x="250" y="14" class="d-label">FRI 3PM</text>
  <rect x="250" y="22" width="200" height="80" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="260" y="40" class="d-label">group issues, find</text>
  <text x="260" y="54" class="d-label">duplicates, notes</text>
  <text x="260" y="72" class="d-node">&#8594; weekly-ops.md</text>
  <text x="260" y="90" class="d-fix">no code, no PR</text>

  <text x="0" y="134" class="d-label">Both write to a file. Neither touches production.</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=SkY-tR9kf-k",
        "channel": "Greg Isenberg",
        "title": "Claude Code New Features, Explained",
        "duration": "48:10",
    },
}
