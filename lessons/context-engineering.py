LESSON = {
    "id": "context-engineering",
    "title": "Why your agent gets dumber the longer you talk to it",
    "subject": "Context engineering",
    "standfirst": "Every model degrades as its context fills. Once you can see the mechanism, three"
                  " unrelated-looking failures turn out to be the same problem — and the fixes stop"
                  " being guesswork.",
    "audience": "You use a coding agent daily and have watched it get worse mid-session without knowing why.",

    # Order is the teaching order. build.py refuses to render if a note appears before one of
    # its own prerequisites — the concept graph is checked, not decorative.
    "notes": [
        "dumb-zone",
        "tool-overload",
        "skill-hell",
        "hallucination-types",
    ],

    # Connective tissue: shown before the named note, to carry the argument between concepts.
    "bridges": {
        "tool-overload": "The mechanism explains a failure that looks like it has nothing to do"
                         " with context length — and is the most common way people fill a window"
                         " without noticing.",
        "skill-hell": "Tools are not the only thing that floods a window. The same overload"
                      " arrives through process, and it now has a name.",
        "hallucination-types": "It also turns a vague complaint into a diagnosis. Not all"
                               " hallucinations are the same failure, and one question separates them.",
    },

    "closing": {
        "title": "The whole lesson in one move",
        "body": "There is one resource, it degrades as it fills, and almost every fix is the same"
                " fix: put less in the window. Fewer tools, smaller tasks, fresh sessions. The"
                " threshold moves as models improve — the mechanism doesn't.",
    },
}
