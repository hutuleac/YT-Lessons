NOTE = {
    "id": "single-job-agents",
    "concept": "One job per agent",
    "one_liner": "A single agent trying to spec, implement, review and harden a feature at once"
                 " drags every unrelated topic into one context; splitting the work into narrow,"
                 " single-purpose agents keeps each one's context small enough to actually follow"
                 " instructions.",

    "prerequisites": ["deterministic-gauntlet"],
    "related": ["agents-vs-workflows", "dumb-zone"],

    "skeleton": [
        "Give one agent one narrow job, not the whole feature.",
        "Specifier writes tests. Coder implements. Cleaner tidies. Hardener stress-tests. QA verifies.",
        "Each agent starts clean and dies when its job is done.",
        "You can run several in parallel — the cost is coordination and startup time.",
    ],

    "mechanism": [
        "A single agent asked to spec a feature, build it, review it and harden it in one session"
        " is holding four different jobs in one context window, and every one of them pulls the"
        " window toward the dumb zone faster than a narrowly scoped task would. Uncle Bob's"
        " answer is a pipeline: five agents, each with exactly one job, handing off to the next.",

        "The Specifier takes a human-written document and turns it into a Gherkin acceptance test"
        " (given/when/then) plus a QA procedure written from a human's point of view — \"you are a"
        " human operating this system at the UI.\" The Coder writes unit tests and the"
        " implementation to make the story and the Gherkin test pass. The Cleaner runs CRAP"
        " analysis and general review to clean up the mess the coder inevitably leaves. The"
        " Hardener runs"
        " mutation testing, \"absolutely merciless,\" chasing full coverage across every flipped"
        " operator. The QA agent converts the procedure into an executable script that drives the"
        " system and returns a deterministic pass or fail.",

        "The payoff is twofold. Focused context means each agent can hold more of its few rules"
        " in the priority zone and actually follow them, and several agents can run in parallel —"
        " his laptop comfortably runs three or more coders at once. Each one is also \"born, does"
        " the task, and dies,\" so the next stage starts with a clean, uncontaminated context"
        " instead of one dragging along everything the last stage was thinking about.",

        "It isn't free: there's real coordination overhead between stages, and each agent costs"
        " 10-15 seconds just to start up and re-establish its context. But the net numbers still"
        " favor the pipeline — a single unconstrained agent finishes a task in about five minutes"
        " with questionable results; the full pipeline takes about an hour for a much"
        " higher-quality result; a human doing the same work by hand takes roughly half a day.",
    ],

    "numbers": [
        {"value": "~5 min", "unit": "time", "label": "a single unconstrained agent takes on a task, with questionable results"},
        {"value": "~1 hr", "unit": "time", "label": "the same task through the full five-stage pipeline, much higher quality"},
        {"value": "~half a day", "unit": "time", "label": "the same task done by a human by hand"},
        {"value": "10-15", "unit": "seconds", "label": "startup cost per agent, before it even re-establishes context"},
    ],

    "analogy": None,

    "practice": [
        "Split a feature into stages instead of asking one agent to spec, code, review and harden"
        " it in one session.",
        "Let a stage's agent die when it's done — start the next one with a clean context, not a"
        " carried-over one.",
        "Run independent stages in parallel where you can; budget for per-agent startup time.",
        "Feed a reviewer or hardener the diff, not the whole codebase, so it doesn't need to"
        " re-explore what already happened.",
    ],

    "diagrams": [
        {
            "title": "One feature, five single-job agents",
            "caption": "Each stage does exactly one thing and hands off a concrete artifact —"
                       " a test, code, a clean diff, coverage, a verified result.",
            "svg": '''<svg viewBox="0 0 540 190" role="img"
  aria-label="A five-stage pipeline: Specifier produces Gherkin tests, Coder produces implementation, Cleaner produces clean code, Hardener produces full mutation coverage, QA produces a verified pass or fail.">
  <defs>
    <marker id="sj-arrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L8 4 L0 8 z" fill="var(--muted)"/>
    </marker>
  </defs>
  <g>
    <rect x="0" y="20" width="92" height="44" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="46" y="38" class="d-node" text-anchor="middle">Specifier</text>
    <text x="46" y="54" class="d-label" text-anchor="middle">gherkin + QA doc</text>
  </g>
  <line x1="92" y1="42" x2="112" y2="42" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#sj-arrow)"/>
  <g>
    <rect x="112" y="20" width="92" height="44" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="158" y="38" class="d-node" text-anchor="middle">Coder</text>
    <text x="158" y="54" class="d-label" text-anchor="middle">tests + code</text>
  </g>
  <line x1="204" y1="42" x2="224" y2="42" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#sj-arrow)"/>
  <g>
    <rect x="224" y="20" width="92" height="44" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="270" y="38" class="d-node" text-anchor="middle">Cleaner</text>
    <text x="270" y="54" class="d-label" text-anchor="middle">low crap score</text>
  </g>
  <line x1="316" y1="42" x2="336" y2="42" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#sj-arrow)"/>
  <g>
    <rect x="336" y="20" width="92" height="44" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
    <text x="382" y="38" class="d-node" text-anchor="middle">Hardener</text>
    <text x="382" y="54" class="d-label" text-anchor="middle">mutation coverage</text>
  </g>
  <line x1="428" y1="42" x2="448" y2="42" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#sj-arrow)"/>
  <g>
    <rect x="448" y="20" width="92" height="44" rx="5" fill="var(--signal)" opacity="0.16" stroke="var(--signal)"/>
    <text x="494" y="38" class="d-node" text-anchor="middle">QA agent</text>
    <text x="494" y="54" class="d-label" text-anchor="middle">pass / fail</text>
  </g>
  <text x="0" y="100" class="d-label">Each box is born, does its one job, and dies —</text>
  <text x="0" y="118" class="d-label">the next one starts with a clean context.</text>
  <text x="0" y="146" class="d-fix">single agent: ~5 min, questionable</text>
  <text x="0" y="164" class="d-fix">full pipeline: ~1 hr, high quality  &#183;  human: ~half a day</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
