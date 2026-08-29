LESSON = {
    "id": "skill-design-principles",
    "title": "How to design a skill an agent actually follows",
    "subject": "Skill design",
    "standfirst": "Seven small techniques for turning a fuzzy request into working code, and for"
                  " keeping the skills and codebase that get you there lean instead of bloated.",
    "audience": "You write skills or specs for a coding agent, or maintain a codebase agents work"
                " in, and want fewer rewrites and less wasted context per request.",

    "notes": [
        "skill-description-routing",
        "grooming-skill",
        "spec-without-code",
        "slice-by-feature",
        "ralph-loop",
        "code-smell-vocabulary",
        "one-door",
        "deletion-test",
    ],

    "bridges": {
        "grooming-skill": "None of that works if the skill never activates in the first place —"
                           " the interview only starts once the router picks it.",
        "spec-without-code": "The grooming interview ends in a shared understanding that lives"
                              " only in the conversation — the spec is what makes it survive.",
        "slice-by-feature": "A spec is only useful once it's broken into tickets an agent can pick"
                             " up one at a time — how you slice them decides what's testable after"
                             " the first one ships.",
        "ralph-loop": "Slicing gives you tickets small enough to hand off unattended — but"
                       " unattended only works once each ticket is gated on its own test, and only"
                       " once you've done enough tickets by hand to trust the gate.",
        "code-smell-vocabulary": "Once code exists, it needs review — and a review checklist is"
                                  " just another set of instructions with the same bloat risk as"
                                  " a spec or a skill.",
        "one-door": "The same instinct that shrinks a review checklist to twelve words applies to"
                    " the codebase itself: fewer things to read is fewer things to get wrong.",
        "deletion-test": "Encapsulating behind one door only helps if what's behind it still"
                          " earns its place — the deletion test is how you find out.",
    },

    "closing": {
        "title": "The pattern under all six",
        "body": "Every technique here trades a bigger, vaguer thing for a smaller, sharper one:"
                " one question instead of a brief, one word instead of a paragraph, one door"
                " instead of five. None of it is about the agent getting smarter — it's about"
                " giving it less to wade through before it can do the part only it can do.",
    },
}
