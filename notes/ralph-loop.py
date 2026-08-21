NOTE = {
    "id": "ralph-loop",
    "concept": "The Ralph loop",
    "one_liner": "An unattended loop that works a plan feature by feature, testing each one before"
                 " moving to the next — but it only amplifies the plan you feed it, so running it"
                 " before you can build a feature by hand just burns tokens faster.",

    "prerequisites": ["grooming-skill"],
    "related": ["deterministic-gauntlet", "review-checkpoints"],

    "skeleton": [
        "A Ralph loop works a plan task by task, unattended, until the list is done.",
        "Each feature gets built, tested, and logged before the next one starts.",
        "A failing test sends the loop back to the same feature, not forward.",
        "It amplifies the plan's quality — a bad plan just fails faster and unsupervised.",
        "Build features by hand first; only automate once you can already do the work yourself.",
    ],

    "mechanism": [
        "A Ralph loop takes a PRD or task list and works through it without a human in the middle"
        " of each step: the agent picks up the next task, builds it, writes and runs a test for"
        " it, records progress to a file, and moves to the next task — repeating until the list"
        " is empty. Left running, it can finish a small plan in minutes while you do something"
        " else. The name comes from the community's own joke about how unsophisticated the"
        " technique actually is — a dumb loop, not a clever agent.",

        "The gate is the test, not the agent's own judgement of done. If the test for a feature"
        " fails, the loop does not move on to the next feature — it goes back and keeps working"
        " the one that's broken. This is what makes the loop trustworthy enough to leave"
        " unattended: it cannot silently build feature three on top of a broken feature two,"
        " because feature two has to pass before three starts. See [[deterministic-gauntlet]] for"
        " why a check outside the prompt holds up where a written rule doesn't.",

        "But the loop has no opinion of its own — it only executes what the plan says, faster and"
        " without supervision. A great plan run through the loop produces a working product in"
        " minutes. A vague plan run through the same loop produces vague software just as fast,"
        " because every gap in the plan becomes an assumption the agent fills in without asking."
        " Ross Mike's summary: if your plan is bad, running Ralph is just donating tokens.",

        "The stronger claim in the source is about sequencing, not the loop itself: don't reach"
        " for it until you've built features by hand first. Doing the plan-build-test cycle"
        " yourself, one feature at a time, is what builds the judgement to tell whether an"
        " agent's output is actually right — what he calls developing a sense for 'vibe QA.'"
        " Turning on full automation before you have that sense means you can't evaluate what"
        " the loop hands back, so mistakes compound for however long you left it running instead"
        " of getting caught on the first feature.",
    ],

    "numbers": [],

    "analogy": {
        "text": "Imagine not knowing how to drive, but then buying a Tesla for the"
                " self-driving stuff.",
        "note": "Full automation before you've done the manual version means you can't tell when"
                " it's steering you wrong.",
    },

    "practice": [
        "Build and test features one at a time by hand before turning on an autonomous loop.",
        "Only automate once you have something built and deployed you can actually point to.",
        "Feed the loop a plan that's been interviewed out — see [[grooming-skill]] — since the"
        " loop cannot fix a bad plan, only execute it faster.",
        "Have every feature write and pass its own test before the loop is allowed to move on.",
    ],

    "diagrams": [
        {
            "title": "Gated on the test, not on the agent's word",
            "caption": "Each feature must pass its own test before the loop advances — a failure"
                       " sends it back to the same feature instead of compounding forward.",
            "svg": '''<svg viewBox="0 0 460 200" role="img"
  aria-label="A loop diagram: build feature, run test, on pass advance to the next feature, on fail return to building the same feature.">
  <defs>
    <marker id="rl-arrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L8 4 L0 8 z" fill="var(--muted)"/>
    </marker>
  </defs>

  <rect x="0" y="20" width="110" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="55" y="41" class="d-node" text-anchor="middle">build feature</text>

  <line x1="110" y1="37" x2="150" y2="37" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#rl-arrow)"/>

  <rect x="150" y="20" width="90" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="195" y="41" class="d-node" text-anchor="middle">run test</text>

  <line x1="240" y1="37" x2="280" y2="37" stroke="var(--signal)" stroke-width="1.5" marker-end="url(#rl-arrow)"/>
  <text x="260" y="27" class="d-label" text-anchor="middle">pass</text>

  <rect x="280" y="20" width="110" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="335" y="41" class="d-node" text-anchor="middle">next feature</text>

  <path d="M195 54 C 195 100, 55 100, 55 54" fill="none" stroke="var(--interference)" stroke-width="1.5" marker-end="url(#rl-arrow)"/>
  <text x="125" y="90" class="d-fix" text-anchor="middle">fail — back to this feature</text>

  <text x="0" y="140" class="d-label">no test failure passes silently forward</text>
  <text x="0" y="160" class="d-label">the loop repeats one feature until its own test says stop</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=zxMjOqM7DFs",
        "channel": "Greg Isenberg",
        "title": "Claude Code Clearly Explained (and how to use it)",
        "duration": "31:28",
    },
}
