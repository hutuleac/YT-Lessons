NOTE = {
    "id": "agents-vs-workflows",
    "concept": "Agents vs workflows",
    "one_liner": "Both orchestrate several LLM calls; the only real difference is who decides when"
                 " to stop — your code in a workflow, the model itself in an agent.",
    "prerequisites": ["tool-loop"],
    "related": ["message-anatomy"],

    "skeleton": [
        "Both are ways of chaining multiple LLM calls.",
        "A workflow follows predetermined steps written in code.",
        "An agent is given tools and decides its own next step — and when to stop.",
        "The dividing question is who ends the program.",
    ],

    "mechanism": [
        "Agents and workflows are both ways of building something more capable than a single"
        " call, and both involve orchestrating several calls. One call is neither of them.",

        "A workflow runs predetermined steps: this call feeds that call feeds the next. The steps"
        " are written by the developer, so the code decides when to call the model again and when"
        " to stop. An agent is handed tools instead of steps. It picks a tool, reacts to the"
        " result, picks again, and decides for itself when the job is done.",

        "So the crucial difference is control of termination. In a workflow it is the code; in an"
        " agent it is the model making it up as it goes. That hands the model much more power and"
        " makes the system much less predictable — the same trade in both directions.",

        "Which is better depends entirely on how well specified the task is. Agents suit problems"
        " where the steps aren't clear and improvisation is required. Workflows suit anything that"
        " must be done the same way repeatedly, and Pocock argues they are unfairly maligned for"
        " being less exciting: for a clearly specified task you will often get better results from"
        " a workflow. Parallel summarisation is his example — split the text, summarise each part,"
        " then summarise the summaries.",
    ],

    "numbers": [],

    "analogy": {
        "text": "With the agent it's the LLM that decides when to stop. With the workflow it's"
                " just following a set of predetermined steps.",
        "note": "Every other difference people cite — autonomy, unpredictability, cost — follows"
                " from that one question, which makes it the useful test when you are choosing.",
    },

    "practice": [
        "Ask who should decide when the job is done. That answer picks the architecture.",
        "Specify the task well enough for a workflow before reaching for an agent.",
        "Use workflows for repeated, well-defined work — they are more predictable and usually better.",
        "Parallelise inside a workflow — split, process independently, then merge.",
    ],

    "diagrams": [
        {
            "title": "Predetermined steps vs the model choosing",
            "caption": "The shapes differ, but the decision that matters is the terminator: code"
                       " ends a workflow, the model ends an agent.",
            "svg": '''<svg viewBox="0 0 520 224" role="img"
  aria-label="Top: a workflow drawn as a fixed chain of three LLM calls ending in code. Bottom: an agent drawn as a single LLM call looping through a choice of tools until it decides to stop.">
  <text x="0" y="12" class="d-label">WORKFLOW &#183; the code stops it</text>
  <rect x="0" y="24" width="86" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="43" y="48" class="d-node" text-anchor="middle">call 1</text>
  <text x="94" y="48" class="d-label">&#8594;</text>
  <rect x="116" y="24" width="86" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="159" y="48" class="d-node" text-anchor="middle">call 2</text>
  <text x="210" y="48" class="d-label">&#8594;</text>
  <rect x="232" y="24" width="86" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="275" y="48" class="d-node" text-anchor="middle">call 3</text>
  <text x="326" y="48" class="d-label">&#8594;</text>
  <rect x="348" y="24" width="96" height="38" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="396" y="48" class="d-fix" text-anchor="middle">code stops</text>
  <text x="0" y="82" class="d-label">same path every time &#8212; predictable, and usually better when the task is clear</text>

  <text x="0" y="126" class="d-label">AGENT &#183; the model stops it</text>
  <rect x="0" y="138" width="110" height="46" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="55" y="166" class="d-node" text-anchor="middle">LLM + tools</text>
  <path d="M110 150 H176" stroke="var(--interference)" stroke-width="1.4" fill="none"/>
  <path d="M110 172 H176" stroke="var(--interference)" stroke-width="1.4" fill="none"/>
  <rect x="180" y="136" width="80" height="24" rx="3" fill="var(--interference)" opacity="0.35"/>
  <text x="220" y="152" class="d-label" text-anchor="middle">tool A</text>
  <rect x="180" y="164" width="80" height="24" rx="3" fill="var(--interference)" opacity="0.35"/>
  <text x="220" y="180" class="d-label" text-anchor="middle">tool B</text>
  <path d="M264 176 H288 V200 H55 V188" stroke="var(--interference)"
        stroke-width="1.4" fill="none" stroke-dasharray="4 4"/>
  <text x="300" y="152" class="d-label">loops until it decides</text>
  <text x="300" y="168" class="d-label">it is finished</text>
  <text x="0" y="216" class="d-label">more power to the model, less predictability &#8212; the same trade, both ways</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/kDnxr8W-bdE",
        "channel": "Matt Pocock",
        "title": "What even are Agents and Workflows?",
        "duration": "1:50",
    },
}
