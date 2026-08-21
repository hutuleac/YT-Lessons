LESSON = {
    "id": "agent-native-engineering",
    "title": "Stop steering agents. Build gauntlets instead.",
    "subject": "Agent-native engineering practice",
    "standfirst": "Uncle Bob spent fifty years writing the rules for humans, then spent the last"
                  " year finding out which of them transfer to agents unchanged, which need new"
                  " thresholds, and which were never rules at all — just habits built around a"
                  " human's limits.",
    "audience": "You run coding agents daily, you've felt the instructions-get-ignored problem"
                " firsthand, and you want a working model for verification, multi-agent"
                " pipelines, and planning that isn't just vibes.",

    "notes": [
        "deterministic-gauntlet",
        "single-job-agents",
        "context-trajectory",
        "agent-thresholds",
        "spec-driven-trap",
        "tactical-vs-strategic",
    ],

    "bridges": {
        "single-job-agents": "One agent enforcing its own checks is the unit. The next question"
                             " is what happens when you stop asking one agent to do everything.",
        "context-trajectory": "Splitting agents by job protects each one's context from"
                              " unrelated topics. Here's the mechanism that makes that protection"
                              " necessary in the first place.",
        "agent-thresholds": "If context contamination is the failure mode, the fix so far has"
                            " been mechanical — checks and clean handoffs. But some of Bob's own"
                            " numbers, the ones from his book, needed to change too.",
        "spec-driven-trap": "Thresholds are one kind of rule Bob revised. Whether to plan a"
                            " feature in detail before touching code is another — and here his"
                            " answer breaks with a decade of habit.",
        "tactical-vs-strategic": "Everything so far has been about how Bob runs agents. The last"
                                 " question is what a junior developer does when the tactical"
                                 " work agents are good at is exactly the work they used to learn"
                                 " on.",
    },

    "closing": {
        "title": "The whole lesson in one move",
        "body": "Every practice here replaces trust in an instruction with trust in a mechanism:"
                " a check the agent must pass, a job narrow enough to keep in context, a clean"
                " window instead of a contaminated one, a threshold re-measured instead of"
                " inherited, a story reviewed instead of a plan trusted. None of it argues"
                " fundamentals stopped mattering — it argues they now have to survive contact"
                " with something that reads perfectly and forgets selectively. The rules you"
                " throw away this year are the ones you'll be picking back up next year.",
    },
}
