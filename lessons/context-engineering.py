LESSON = {
    "id": "context-engineering",
    "title": "Everything is competing for the same window",
    "subject": "Context engineering",
    "standfirst": "One pool of tokens, one mechanism that degrades as it fills, and six different"
                  " things quietly spending it — the tools you added, the ones your harness"
                  " shipped, the memories your agent saved itself, the docs nobody tests. Same"
                  " resource, same fix.",
    "audience": "You use a coding agent daily and have watched it get worse mid-session without"
                " knowing why — or what was in the window before you typed anything.",

    # Order is the teaching order. build.py refuses to render if a note appears before one of
    # its own prerequisites — the concept graph is checked, not decorative. A prerequisite
    # taught by another lesson (tokens, in llm-fundamentals) links out rather than being
    # duplicated here.
    "notes": [
        "context-window",
        "dumb-zone",
        "tool-overload",
        "harness-bloat",
        "skill-hell",
        "agent-memory",
        "docs-drift",
        "hallucination-types",
    ],

    # Connective tissue: shown before the named note, to carry the argument between concepts.
    "bridges": {
        "dumb-zone": "The hard limit is the boring failure — it errors, so you see it. The"
                     " interesting one starts long before the limit and never announces itself.",
        "tool-overload": "So the window is a budget that degrades as it fills. The first thing"
                         " spending it is the one you added on purpose, believing it made the"
                         " agent more capable.",
        "harness-bloat": "You did not add most of what is in there. The tool you code in shipped"
                         " with its own tools, and they are re-sent on every request.",
        "skill-hell": "Tools are not the only thing that arrives in bulk. The same overload"
                      " comes through process, and it now has a name.",
        "agent-memory": "Tool definitions and skills at least do something you asked for. The"
                        " next occupant is material the agent chose to keep on your behalf.",
        "docs-drift": "The last one you wrote yourself, with the best intentions — and it is the"
                      " only one that can also be wrong.",
        "hallucination-types": "That is the audit. The mechanism also turns a vague complaint"
                               " into a diagnosis: not all hallucinations are the same failure,"
                               " and one question separates them.",
    },

    "closing": {
        "title": "The whole lesson in one move",
        "body": "There is one resource, it degrades as it fills, and almost every fix is the same"
                " fix: put less in the window. Fewer tools, fewer shipped features, no saved"
                " memories, thinner docs, smaller tasks, fresh sessions. Audit what is in the"
                " request once — a proxy, a settings page, a MEMORY.md — and you will usually"
                " find more to delete than to tune. The threshold moves as models improve; the"
                " mechanism doesn't.",
    },
}
