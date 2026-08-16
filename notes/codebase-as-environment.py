NOTE = {
    "id": "codebase-as-environment",
    "concept": "The code is the agent's environment",
    "one_liner": "An agent's output quality is bounded by the codebase it works in, and unlike a"
                 " human it has no memory to route around a bad one — so software fundamentals"
                 " matter more now, not less.",
    "prerequisites": [],
    "related": ["agent-memory", "docs-drift", "no-greenfield"],

    "skeleton": [
        "The codebase is the environment the agent operates in.",
        "A garbage codebase produces garbage output.",
        "Humans build a feel for a bad codebase. Agents cannot — no memory.",
        "So the same mistakes repeat, on dumb models and smart ones alike.",
    ],

    "mechanism": [
        "The question is whether fundamentals still matter if the code is just something the AI"
        " produces. Pocock's answer inverts it: the code is the environment the agent operates in,"
        " and the quality of that environment shapes the output. A garbage codebase yields garbage"
        " work, and garbage codebases sneak up on you — software entropy means disorganisation"
        " accumulates unless someone is deliberately holding a long-term view.",

        "The asymmetry is memory. Humans are better at working in bad codebases than agents are,"
        " because a human accumulates a feel for it: what works here, what to avoid, which corner"
        " lies. Imperfect, but it compounds, and it keeps them productive in a mess.",

        "Agents have none of that unless you bolt on a memory system, which is itself unsolved."
        " Pocock's image is the man from Memento: the agent wakes up in the codebase, asks what it"
        " remembers, and the answer is nothing. So it makes the same mistake again and again"
        " unless you are there with guardrails preventing it.",

        "Crucially this is not a reasoning problem, so a smarter model does not fix it. The"
        " difficulty is that the codebase is hard to explore, hard to change, hard to work in."
        " Which makes the valuable skill building a good agent experience: code that is easy to"
        " explore, tests at good seams, clean module and interface design.",
    ],

    "numbers": [],

    "analogy": {
        "text": "They are kind of like the guy from Memento who wakes up in the codebase and"
                " goes: okay, I'm awake — what do I remember? Nothing.",
        "note": "It explains why the fix is environmental rather than a better prompt: you cannot"
                " teach something that starts every session from zero, you can only make the"
                " place it wakes up in easier to read.",
    },

    "practice": [
        "Judge a refactor by whether it makes the codebase easier for an agent to explore.",
        "Put tests at seams that let an agent verify a change without understanding everything.",
        "Encode the guardrails that stop repeated mistakes — the agent will not remember them.",
        "Stop reaching for a smarter model when the real obstacle is the environment.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/shorts/eEjBhVI9Qok",
        "channel": "Matt Pocock",
        "title": "Do software fundamentals still matter?",
        "duration": "2:12",
    },
}
