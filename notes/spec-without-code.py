NOTE = {
    "id": "spec-without-code",
    "concept": "No code blocks in the spec",
    "one_liner": "A spec should point at the code, not paste it — a pasted snippet goes stale the"
                 " moment implementation starts, and an agent will follow stale code over the"
                 " live codebase in front of it.",

    "prerequisites": [],
    "related": ["spec-driven-trap", "grooming-skill"],

    "skeleton": [
        "The spec is what survives once the grooming conversation is closed.",
        "Rule: never put a code block in the spec, even a highly technical one.",
        "A pasted snippet is a snapshot — the real code moves on without it.",
        "Without code, the agent has to cross-reference the live codebase instead.",
    ],

    "mechanism": [
        "Once a grooming interview reaches a shared understanding, that understanding only exists"
        " in the conversation — close it without writing it down and every question, every answer,"
        " every decision is gone. The spec is that write-down: a design plan converted from the"
        " conversation into a document the next step can build from.",

        "The rule that makes this spec different from a typical design doc is what it leaves out."
        " No code block goes in the file, even when the content is highly technical. The reasoning"
        " is about staleness, not style: if a spec contains code, the agent treats that code as"
        " instruction and follows it — but code written during a planning conversation is a"
        " snapshot, and by the time implementation starts the real codebase has usually moved. An"
        " agent following stale pasted code over the live file in front of it produces exactly the"
        " kind of bug that looks like it followed instructions correctly.",

        "Dropping code from the spec forces the alternative: the agent has to look at the actual"
        " code and cross-reference it to decide what is right, rather than trusting a fossil. The"
        " spec stays cleaner as a description of intent, and the codebase — not the document —"
        " stays the source of truth for how anything is actually implemented.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Write specs as prose and intent, never as pasted implementation code.",
        "If a decision feels like it needs a code sample to be clear, point at the file and line"
        " instead of copying it in.",
        "Treat the codebase, not the spec, as the source of truth once implementation starts.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/watch?v=8D8ewFBJfFM",
        "channel": "Eric Tech",
        "title": "Matt Pocock's Claude Code Skills Beat Superpowers Now",
        "duration": "24:17",
    },
}
