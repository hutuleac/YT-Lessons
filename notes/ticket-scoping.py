NOTE = {
    "id": "ticket-scoping",
    "concept": "The ticket needs a visible finish line",
    "one_liner": "A vague prompt makes the agent guess what matters, and once it's guessing you're"
                 " no longer managing the work, you're cleaning it up — a real ticket names the"
                 " scope and the finish line."
                 ,

    "prerequisites": [],
    "related": ["grooming-skill", "slice-by-feature", "spec-driven-trap", "checkable-oracle",
                "goal-judge"],

    "skeleton": [
        "\"Make the app better\" forces the agent to guess. Guessing means you clean up later.",
        "Brief it in three parts: the task, the guardrails, what done looks like.",
        "Newer models plan as they work. Check what it did, not what it planned.",
        "Then implement as one focused, reviewable change — not a pile of everything at once.",
    ],

    "mechanism": [
        "The failure mode isn't the agent's competence, it's the size and shape of what it was"
        " given. 'Make this pop' has no finish line, so the agent supplies one — its own guess"
        " at what matters — and a guess you didn't make is a guess you now have to check line by"
        " line. A ticket like 'add a waitlist form with name, email, company, and a success"
        " state, matching the current brand' has a scope an agent can actually finish and a"
        " reviewer can actually check against.",

        "Greg Isenberg's version puts plan mode before the build: the agent inspects the repo,"
        " hands back the files it would touch, the smallest implementation, the risk, and what it"
        " is leaving out, and waits. Sized to one ticket, not a project plan (see"
        " [[spec-driven-trap]]), so you have something concrete to react to.",

        "That step has since been dropped by the person who invented it. Boris Cherny, who built"
        " Claude Code, said in January that most of his sessions started in plan mode; by"
        " autumn 2026 he said on Hacker News it is no longer useful. Plan mode never changed"
        " what Claude could do — it appended a reminder not to start coding yet, a fix for older"
        " models (Sonnet 4.6, early Opus) that jumped straight in. Newer models plan while they"
        " work, so his brief became three parts: the task, the guardrails around it, and what"
        " done looks like — then let the model work it out and check the result afterwards. For"
        " bigger changes he asks for a diagram or an interactive demo of what changed. Plan mode"
        " still exists and still earns its place on a model that dives in too early; it is no"
        " longer the default.",

        "The definition of done is the part that compounds. It is the finish line the agent works"
        " toward, the thing you check the output against, and — written precisely enough — the"
        " check the agent can run on itself ([[checkable-oracle]]).",

        "Ticket size is also what makes review possible. A tightly scoped ticket produces a diff"
        " you can actually read; a vague one produces a pile of changes that might look impressive"
        " but is hard to trust, because nothing bounded what got touched.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Write the ticket the way you'd brief a new hire: job, scope, expected experience, and"
        " what's off-limits — not \"make it better.\"",
        "Brief in three lines — task: this week's report from the CRM export; guardrails: don't"
        " amend the template, don't email anyone; done: every figure matches the export.",
        "Reach for plan mode only when the model starts building before it understands the job.",
        "When it finishes, ask for a one-page visual of what it did and what it assumed.",
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

    "also": [
        {
            "url": "https://www.youtube.com/watch?v=J9NQTYUP6k0",
            "channel": "Simon Scrapes",
            "title": "How the Top 1% Use Claude Code Differently",
            "duration": "18:09",
        },
    ],
}
