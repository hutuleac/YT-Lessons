NOTE = {
    "id": "docs-drift",
    "concept": "Docs as a second source of truth",
    "one_liner": "A layer of markdown written to explain your code becomes a second source of"
                 " truth that nothing tests, and when it drifts the agent cannot tell which one"
                 " is real.",
    "prerequisites": ["context-window"],
    "related": ["agent-memory", "harness-bloat"],

    "skeleton": [
        "Docs written to explain the code are not executable and not testable.",
        "So they drift, and now two sources of truth disagree.",
        "The agent can't tell which one is real — and it costs tokens to read both.",
        "Keep the docs code genuinely can't carry: decisions, glossary, a thin map.",
    ],

    "mechanism": [
        "When an agent explores a codebase, the code is normally all it has to go on. That puts"
        " the burden on the code: formatted well, in sensible files, organised into reasonable"
        " chunks, interfaces separated from implementations so the agent can take what it needs.",

        "The antipattern is avoiding that work by building a layer of markdown docs and pointing"
        " the agent at those instead. Those files are not executable and not testable against the"
        " code, so nothing stops them drifting. Once they have drifted you have two sources of"
        " truth that disagree, and the agent has no way to tell which one is real. It also costs"
        " tokens to read the explanation on top of the thing it explains.",

        "This is not an argument against all docs. Code genuinely cannot record what alternatives"
        " were considered and rejected — that is what architecture decision records are for. It"
        " cannot define your domain language either: whether the agent knows what an \"order\""
        " means in your codebase is a question a glossary answers. And a thin navigational layer"
        " speeds up exploration.",

        "The line is docs as the source of truth. A doc that captures something the code cannot"
        " express is worth keeping. A doc that restates what the code already says is a liability"
        " that starts accurate and ends misleading.",
    ],

    "numbers": [],

    "analogy": {
        "text": "If there are two sources of truth and they conflict, AI won't know which one is"
                " the real one.",
        "note": "It reframes the choice: the question is not whether docs are useful, but whether"
                " this doc can ever be checked against the thing it describes.",
    },

    "practice": [
        "Delete docs that restate the code — invest that effort in making the code readable instead.",
        "Keep architecture decision records: alternatives considered are not recoverable from code.",
        "Keep a glossary of domain terms; the agent cannot infer what your nouns mean.",
        "Keep the navigational layer thin — a map, not a mirror.",
    ],

    "diagrams": [
        {
            "title": "Two sources of truth, drifting apart",
            "caption": "The code changes because it has to. The doc changes when someone"
                       " remembers. Nothing fails when the gap opens.",
            "svg": '''<svg viewBox="0 0 460 184" role="img"
  aria-label="Two parallel timelines starting together. The code line advances through several commits. The docs line stops early, and the gap between them is labelled drift.">
  <text x="0" y="14" class="d-label">CODE &#183; tested, executed, forced to stay true</text>
  <line x1="0" y1="44" x2="440" y2="44" stroke="var(--signal)" stroke-width="2.5"/>
  <g fill="var(--signal)">
    <circle cx="20" cy="44" r="5"/><circle cx="120" cy="44" r="5"/><circle cx="220" cy="44" r="5"/>
    <circle cx="320" cy="44" r="5"/><circle cx="430" cy="44" r="5"/>
  </g>

  <text x="0" y="104" class="d-label">DOCS &#183; nothing checks them</text>
  <line x1="0" y1="134" x2="120" y2="134" stroke="var(--interference)" stroke-width="2.5"/>
  <line x1="120" y1="134" x2="440" y2="134" stroke="var(--interference)" stroke-width="2.5"
        stroke-dasharray="5 6" opacity="0.5"/>
  <g fill="var(--interference)"><circle cx="20" cy="134" r="5"/><circle cx="120" cy="134" r="5"/></g>

  <line x1="320" y1="44" x2="320" y2="134" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="330" y="94" class="d-num">drift</text>
  <text x="0" y="174" class="d-label">both still claim to be true, and the agent has no way to break the tie</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/Fj8DKMbdIzU",
        "channel": "Matt Pocock",
        "title": "Delete (most of) your docs",
        "duration": "2:04",
    },
}
