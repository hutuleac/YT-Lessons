NOTE = {
    "id": "review-triage",
    "concept": "Must-fix, should-fix, okay-to-ship",
    "one_liner": "Reviewing an agent's work against a written standard and sorting findings into"
                 " three buckets turns review from a binary judgment call into a checklist you can"
                 " actually act on."
                 ,

    "prerequisites": ["review-checkpoints"],
    "related": ["repo-as-onboarding-packet"],

    "skeleton": [
        "Once the agent builds fast, the bottleneck moves to judgment, not output.",
        "Layer one: your own read of the diff. Does it match the ticket? Anything surprising?",
        "Layer two: the agent reviews itself against review.md, a written standard.",
        "Sort findings into must-fix, should-fix, okay-to-ship — not just \"looks good.\"",
    ],

    "mechanism": [
        "Once an agent can produce changes quickly, the constraint stops being speed and becomes"
        " judgment: did it solve the right problem, touch the right files, avoid a weird edge"
        " case. That judgment happens in two layers. The first is a human skim of the diff itself"
        " — the same before/after view used for [[review-checkpoints]] — checking whether"
        " anything changed that the ticket didn't ask for. A scoped ticket that suddenly touches"
        " auth or the database is the signal to stop and look closer, before reading a single"
        " line in detail.",

        "The second layer hands the same diff back to the agent with an explicit standard: review"
        " it against review.md for production issues, broken edge cases, and confusing user"
        " flows, and separate the findings into three buckets — must fix, should fix, and okay to"
        " ship — rather than a single yes or no. That three-way split is the mechanism: a binary"
        " pass/fail either blocks on cosmetic issues or waves through real ones, while a triage"
        " lets you ship the okay-to-ship items now and schedule the rest.",

        "For higher-stakes changes — authentication, payments — the same review can run deeper,"
        " as a dedicated review pass in a fresh context rather than the session that wrote the"
        " code, for the same reason a same-session self-check misses its own blind spots.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Write review.md once, as the explicit standard changes get judged against — not a"
        " one-off instruction typed into each review prompt.",
        "Sort every review pass into must-fix / should-fix / okay-to-ship rather than a single"
        " verdict.",
        "Treat an unexpected file in the diff as the review's first question, before reading"
        " anything else.",
        "Run a deeper, fresh-context review pass on high-stakes changes — auth, payments, data.",
    ],

    "diagrams": [
        {
            "title": "One diff, three buckets",
            "caption": "Sorting findings by urgency instead of a single pass/fail lets you ship"
                       " what's ready and schedule the rest.",
            "svg": '''<svg viewBox="0 0 460 150" role="img"
  aria-label="A diff feeds into review against review.md, which sorts findings into three buckets: must fix, should fix, and okay to ship.">
  <rect x="0" y="52" width="90" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="45" y="73" class="d-node" text-anchor="middle">diff</text>
  <path d="M94 69 H136" stroke="var(--line)" stroke-width="1.4"/>
  <rect x="140" y="52" width="110" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="195" y="73" class="d-label" text-anchor="middle">review.md</text>
  <path d="M250 69 H270" stroke="var(--line)" stroke-width="1.2"/>

  <rect x="290" y="6" width="150" height="30" rx="4" fill="var(--interference)" opacity="0.45"/>
  <text x="365" y="26" class="d-label" text-anchor="middle">must fix</text>
  <rect x="290" y="54" width="150" height="30" rx="4" fill="var(--sand)" opacity="0.5"/>
  <text x="365" y="74" class="d-label" text-anchor="middle">should fix</text>
  <rect x="290" y="102" width="150" height="30" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="365" y="122" class="d-label" text-anchor="middle">okay to ship</text>

  <path d="M270 69 H280 V21 H290" fill="none" stroke="var(--line)" stroke-width="1"/>
  <path d="M270 69 H290" fill="none" stroke="var(--line)" stroke-width="1"/>
  <path d="M270 69 H280 V117 H290" fill="none" stroke="var(--line)" stroke-width="1"/>
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
