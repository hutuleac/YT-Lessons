LESSON = {
    "id": "claude-code-in-practice",
    "title": "Questions, then checks, then context, then pipelines",
    "subject": "Working with a coding agent",
    "standfirst": "The person who built Claude Code teaches it as a ladder, not a feature list:"
                  " start by asking the codebase questions, give the agent a way to grade its own"
                  " work, place your context where it belongs, and only then wire it into"
                  " everything else.",
    "audience": "You have a coding agent installed, you're getting mixed results out of it, and"
                " you want the progression its own author recommends rather than a pile of"
                " tips.",

    "notes": [
        "codebase-qa-first",
        "checkable-oracle",
        "context-hierarchy",
        "agent-as-unix-utility",
        "parallel-worktree-agents",
    ],

    "bridges": {
        "checkable-oracle": "Questions calibrate you on what the agent can do unaided. The moment"
                            " you move from asking to building, the limit stops being its"
                            " knowledge and starts being whether it can tell how the last attempt"
                            " went.",
        "context-hierarchy": "A check tells the agent whether it hit the target. It says nothing"
                             " about which target — that comes from the context you give it, and"
                             " where you put that context decides who gets it and what it costs.",
        "agent-as-unix-utility": "Once the context and the checks live in the repo rather than in"
                                 " your head, a run no longer needs you sitting in front of it —"
                                 " which is the precondition for running it somewhere other than"
                                 " your terminal.",
        "parallel-worktree-agents": "And once a run is something you launch rather than something"
                                    " you attend, the obvious next question is how many you can"
                                    " have going at once — which is where the ceiling turns out"
                                    " to be isolation, not the tool.",
    },

    "closing": {
        "title": "The ladder is the point",
        "body": "Every rung buys the next one. Questions teach you where the agent's competence"
                " ends, so you know what to delegate. A checkable target lets it close that gap"
                " itself, two or three iterations at a time. Context placed at the right scope"
                " makes the target correct without being re-explained every session. And an agent"
                " that needs neither your explanation nor your approval is one you can pipe,"
                " schedule, and run several of at once. Skipping to the last rung is how people"
                " end up with an expensive autocomplete.",
    },
}
