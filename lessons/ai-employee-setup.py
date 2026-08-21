LESSON = {
    "id": "ai-employee-setup",
    "title": "Set up a coding agent like you'd onboard a new hire",
    "subject": "Agent operations",
    "standfirst": "The same eight things a new employee needs — a workspace, a clear ticket, a way"
                  " to check their own work, review standards, recurring duties, and boundaries —"
                  " turn a coding agent from a chat window into something closer to staff.",
    "audience": "You run a coding agent on a real product and want it doing more than one-off"
                " edits: recurring work, parallel tasks, and changes you can actually trust"
                " without reading every line.",

    "notes": [
        "repo-as-onboarding-packet",
        "ticket-scoping",
        "agent-eyes",
        "review-triage",
        "scheduled-routines",
        "parallel-worktree-agents",
        "permission-tiers",
        "skills-connectors-hooks",
    ],

    "bridges": {
        "ticket-scoping": "The repo tells the agent who the business is — the ticket tells it"
                           " what to actually do today, and how small a job has to be to stay"
                           " reviewable.",
        "agent-eyes": "A ticket can be implemented correctly and still miss the point — the only"
                      " way to catch that is to have the agent use the thing, not just build it.",
        "review-triage": "Once the agent is both building and checking its own work, you need a"
                          " second layer: judging that work against a standard, not just a vibe.",
        "scheduled-routines": "All of this so far happens while you're present. A routine is the"
                               " same discipline running without you in the room.",
        "parallel-worktree-agents": "One routine running unattended is a start — the next step is"
                                     " several scoped sessions running unattended at once.",
        "permission-tiers": "More sessions running with less supervision is only safe if what"
                             " they're allowed to do is bounded ahead of time, not decided live.",
        "skills-connectors-hooks": "The last layer isn't a new capability, it's naming which of"
                                    " the three you actually need instead of writing another"
                                    " instruction into every prompt.",
    },

    "closing": {
        "title": "The whole loop",
        "body": "Customer feedback goes into /customers. Direction goes into roadmap.md. Working"
                " style goes into claude.md. Standards go into review.md. Small tasks go through"
                " plan mode. Changes go through preview and review. Recurring work becomes a"
                " scheduled routine. None of these pieces is impressive alone — the leverage is"
                " in running them as one loop instead of reaching for whichever one you remember"
                " that day.",
    },
}
