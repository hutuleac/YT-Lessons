NOTE = {
    "id": "single-job-agents",
    "concept": "One job per agent",
    "one_liner": "One agent that does the spec, the code, the review, and the checks all at once"
                 " must hold too many topics in one context. Split the work into small, one-job"
                 " agents. Then each one keeps a context small enough to follow its own"
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
        "One agent that must spec a feature, build it, review it, and check it in one session"
        " holds four jobs in one context window. Each job pulls that window toward the dumb"
        " zone faster than a small task would. Uncle Bob's answer is a pipeline. Five agents"
        " work on the task. Each agent has one job. Each agent passes its work to the next.",

        "The Specifier reads a document written by a human. It turns the document into a Gherkin"
        " test (given/when/then) and a QA procedure. The QA procedure is written from a human's"
        " point of view: \"you are a human operating this system at the UI.\" The Coder writes"
        " unit tests and the code. This code must make the story and the Gherkin test pass. The"
        " Cleaner runs a CRAP check and a general review. This cleans up the mess the coder"
        " leaves behind. The Hardener runs mutation testing. Uncle Bob calls this stage"
        " \"absolutely merciless\": it aims for full coverage across every changed operator. The"
        " QA agent turns the procedure into a script. This script runs the system and returns a"
        " clear pass or fail.",

        "This method has two gains. First, each agent keeps a small context, so it can hold its"
        " few rules and follow them. Second, several agents can run at the same time. Uncle Bob's"
        " laptop runs three or more coders at once, with no trouble. Each agent starts, does its"
        " one job, and then stops. So the next stage starts with a clean context. It does not"
        " carry the last stage's problems forward.",

        "This method also costs something. Agents need real coordination between stages. Each"
        " agent takes 10 to 15 seconds just to start and load its context. But the numbers still"
        " favor the pipeline. One agent alone finishes a task in about five minutes, with weak"
        " results. The full pipeline takes about an hour, with much better results. A human doing"
        " the same work by hand takes about half a day.",
    ],

    "numbers": [
        {"value": "~5 min", "unit": "time", "label": "a single unconstrained agent takes on a task, with questionable results"},
        {"value": "~1 hr", "unit": "time", "label": "the same task through the full five-stage pipeline, much higher quality"},
        {"value": "~half a day", "unit": "time", "label": "the same task done by a human by hand"},
        {"value": "10-15", "unit": "seconds", "label": "startup cost per agent, before it even re-establishes context"},
    ],

    "analogy": None,

    "practice": [
        "Split a feature into stages. Do not ask one agent to spec, code, review, and check it"
        " in one session.",
        "Stop a stage's agent when its job is done. Start the next stage with a clean context.",
        "Run stages that do not depend on each other at the same time. Plan for startup time on"
        " each agent.",
        "Give a reviewer or checker the diff, not the whole codebase. It will not need to explore"
        " what already happened.",
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
