NOTE = {
    "id": "agent-memory",
    "concept": "Kill the auto-memory",
    "one_liner": "Letting an agent save its own memories trades predictability for convenience —"
                 " a stateless agent starts from the same base every time, and anything worth"
                 " keeping belongs in a file you wrote.",
    "prerequisites": ["context-window"],
    "related": ["docs-drift", "dumb-zone"],

    "skeleton": [
        "Turn auto-memory off and delete what the agent saved itself.",
        "It is too eager: a one-off preference leaks into every later conversation.",
        "Stateless means a consistent base, so behaviour is predictable.",
        "Write preferences yourself, in a file you control.",
    ],

    "mechanism": [
        "Pocock's position is blunt: turn auto-memory off completely and delete almost everything"
        " the agent has saved into its own memory banks. In Claude Code that is a setting, and the"
        " memories live in an uppercase MEMORY.md.",

        "The problem is eagerness. A preference you expressed about one specific feature — how"
        " that thing should be built — gets saved, and then influences every conversation you have"
        " afterwards, in contexts where it was never meant to apply.",

        "The gain from switching it off is predictability. A stateless agent remembers nothing"
        " between sessions, so every session starts from the same base and you know how it will"
        " behave. With memory accumulating, the behaviour drifts: each use is slightly different"
        " and slightly less predictable than the last, and none of that drift is visible to you.",

        "The alternative is not to have no preferences — it is to write them down deliberately."
        " Edit your CLAUDE.md, add a doc in the repo. You stay in control of the steering, and the"
        " preference exists because you decided it should, not because the agent inferred it.",
    ],

    "numbers": [],

    "analogy": {
        "text": "You should be in control of the steering.",
        "note": "The same test as any other agent feature: does it make your process repeatable,"
                " or does it quietly change the starting conditions on you?",
    },

    "practice": [
        "Turn auto-memory off in settings and clear what has already accumulated.",
        "Put durable preferences in CLAUDE.md or a repo doc — deliberately, by hand.",
        "Treat a stateless agent as the feature: a consistent base is what makes results comparable.",
        "If behaviour drifts between sessions, look at saved memory before blaming the model.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/shorts/A0scuiiGBC4",
        "channel": "Matt Pocock",
        "title": "Kill your MEMORY.md",
        "duration": "1:29",
    },
}
