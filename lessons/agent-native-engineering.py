LESSON = {
    "id": "agent-native-engineering",
    "title": "Stop steering agents. Build gauntlets instead.",
    "subject": "Agent-native engineering practice",
    "standfirst": "Uncle Bob spent fifty years writing rules for humans. In the last year, he"
                  " tested which rules still work for agents, which rules need new limits, and"
                  " which rules were never real rules at all, just habits built around a human's"
                  " limits.",
    "audience": "You run coding agents every day. You have seen agents ignore your instructions."
                " You want a working method for checks, multi-agent pipelines, and planning that"
                " does not rely on guesswork.",

    "notes": [
        "deterministic-gauntlet",
        "single-job-agents",
        "context-trajectory",
        "agent-thresholds",
        "spec-driven-trap",
        "tactical-vs-strategic",
    ],

    "bridges": {
        "single-job-agents": "One agent that checks its own work is the base case. The next"
                             " question: what happens when you stop asking one agent to do"
                             " everything.",
        "context-trajectory": "Splitting agents by job keeps each one's context free of"
                              " unrelated topics. Here is the reason that protection matters at"
                              " all.",
        "agent-thresholds": "Context problems get a mechanical fix: checks and clean handoffs."
                            " But some of Bob's own numbers, the ones from his book, also had to"
                            " change.",
        "spec-driven-trap": "Thresholds are one rule Bob changed. Planning a feature in full"
                            " before writing any code is another. Here, his answer breaks with"
                            " years of habit.",
        "tactical-vs-strategic": "So far, this has all been about how Bob runs agents. The last"
                                 " question is different: what should a junior developer do when"
                                 " agents already do the tactical work junior developers used to"
                                 " learn on.",
    },

    "closing": {
        "title": "The whole lesson in one move",
        "body": "Every practice here swaps trust in an instruction for trust in a mechanism: a"
                " check the agent must pass, a job small enough to fit in one context, a clean"
                " window instead of a spoiled one, a threshold checked again instead of copied,"
                " a story reviewed instead of a plan trusted on faith. None of this means"
                " fundamentals stopped mattering. It means fundamentals now have to survive"
                " contact with something that reads every word and still forgets on its own"
                " terms. The rules you drop this year are the ones you will pick back up next"
                " year.",
    },
}
