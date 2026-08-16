LESSON = {
    "id": "window-hygiene",
    "title": "Everything competing for the same window",
    "subject": "Context hygiene",
    "standfirst": "One pool of tokens, and four different things quietly filling it: the tools you"
                  " added, the ones your harness shipped, the memories your agent saved itself,"
                  " and a layer of docs nobody tests. Same resource, same fix.",
    "audience": "You already know your agent degrades in long sessions and want the list of things"
                " eating the window before you have typed anything.",

    "notes": [
        "tokens",
        "context-window",
        "dumb-zone",
        "tool-overload",
        "harness-bloat",
        "agent-memory",
        "docs-drift",
    ],

    "bridges": {
        "context-window": "Everything in this lesson is measured in one unit, so start there —"
                          " then look at what the unit adds up to.",
        "dumb-zone": "The hard limit is the boring failure — it errors, so you see it. The"
                     " interesting one starts long before the limit and never announces itself.",
        "tool-overload": "So the window is a budget. The first thing spending it is the one you"
                         " added on purpose, believing it made the agent more capable.",
        "harness-bloat": "You did not add most of what is in there. The tool you code in shipped"
                         " with its own tools, and they are re-sent on every request.",
        "agent-memory": "Tool definitions at least do something. The next occupant is material the"
                        " agent chose to keep on your behalf.",
        "docs-drift": "The last one is written by you, with the best intentions, and it is the"
                      " only one that can also be wrong.",
    },

    "closing": {
        "title": "Audit what is in the window before you optimise what you put in it",
        "body": "Every concept here is the same sentence: something is occupying the window and"
                " nothing told you. Tools you added, features you never enabled, memories you"
                " didn't write, docs that stopped matching the code. Look at the whole request"
                " once — a proxy, a settings page, a MEMORY.md — and you will usually find more"
                " to delete than to tune.",
    },
}
