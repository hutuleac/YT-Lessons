NOTE = {
    "id": "ticket-scoping",
    "concept": "The ticket needs a visible finish line",
    "one_liner": "A vague prompt makes the agent guess what matters, and once it's guessing you're"
                 " no longer managing the work, you're cleaning it up — a real ticket names the"
                 " scope and the finish line."
                 ,

    "prerequisites": [],
    "related": ["grooming-skill", "slice-by-feature", "spec-driven-trap"],

    "skeleton": [
        "\"Make the app better\" forces the agent to guess. Guessing means you clean up later.",
        "A ticket needs: the job, the scope, the expected experience, the boundary.",
        "Plan mode first: inspect the repo, propose the approach, wait for approval.",
        "Then implement as one focused, reviewable change — not a pile of everything at once.",
    ],

    "mechanism": [
        "The failure mode isn't the agent's competence, it's the size and shape of what it was"
        " given. 'Make this pop' has no finish line, so the agent supplies one — its own guess"
        " at what matters — and a guess you didn't make is a guess you now have to check line by"
        " line. A ticket like 'add a waitlist form with name, email, company, and a success"
        " state, matching the current brand' has a scope an agent can actually finish and a"
        " reviewer can actually check against.",

        "Plan mode is the step before the ticket gets built: ask the agent to inspect the repo and"
        " its own context files first, then hand back the files it would touch, the smallest"
        " implementation, the user-facing risk, and what it's deliberately leaving out — before"
        " touching anything. This isn't a full upfront project plan (see [[spec-driven-trap]] for"
        " why that fails); it's sized to one ticket, and it exists so you have something concrete"
        " to react to instead of a blank diff.",

        "Ticket size is also what makes review possible. A tightly scoped ticket produces a diff"
        " you can actually read; a vague one produces a pile of changes that might look impressive"
        " but is hard to trust, because nothing bounded what got touched.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Write the ticket the way you'd brief a new hire: job, scope, expected experience, and"
        " what's off-limits — not \"make it better.\"",
        "Run plan mode before implementation on anything that isn't trivial — the ask is inspect"
        " first, propose second, wait for approval third.",
        "If a ticket is big enough that you can't review the diff in one sitting, it's not one"
        " ticket.",
    ],

    "diagrams": [
        {
            "title": "What the agent does with the gap",
            "caption": "A vague prompt leaves a gap the agent has to fill on its own — with its"
                       " guess, not yours.",
            "svg": '''<svg viewBox="0 0 460 170" role="img"
  aria-label="Two prompts. Vague prompt: make this pop, leads to the agent guessing what matters, producing a large unreviewable diff. Specific ticket: add a waitlist form with name, email, company and a success state, leads directly to a small reviewable diff.">
  <text x="0" y="14" class="d-label">VAGUE</text>
  <rect x="0" y="24" width="150" height="30" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="75" y="43" class="d-label" text-anchor="middle">"make this pop"</text>
  <path d="M75 54 V70" stroke="var(--interference)" stroke-width="1.4"/>
  <text x="75" y="86" class="d-fix" text-anchor="middle">agent guesses</text>
  <rect x="0" y="94" width="150" height="30" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="75" y="113" class="d-label" text-anchor="middle">big, unreviewable diff</text>

  <text x="250" y="14" class="d-label">SPECIFIC TICKET</text>
  <rect x="250" y="24" width="200" height="46" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="260" y="40" class="d-label">"waitlist form: name,</text>
  <text x="260" y="54" class="d-label">email, company, success</text>
  <text x="260" y="66" class="d-label">state, match brand"</text>
  <path d="M350 70 V86" stroke="var(--signal)" stroke-width="1.4"/>
  <text x="350" y="102" class="d-fix" text-anchor="middle">agent builds to spec</text>
  <rect x="270" y="110" width="160" height="30" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="350" y="129" class="d-label" text-anchor="middle">small, reviewable diff</text>
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
