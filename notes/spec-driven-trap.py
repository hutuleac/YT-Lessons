NOTE = {
    "id": "spec-driven-trap",
    "concept": "The spec-driven development trap",
    "one_liner": "A large plan written before any code fails an agent the same way it failed"
                 " humans in the waterfall era. Agents write large, detailed plans with ease. But"
                 " those plans break apart once real work starts.",

    "prerequisites": [],
    "related": ["review-checkpoints"],

    "skeleton": [
        "A large plan written before any code repeats an old mistake: waterfall, from the 1970s.",
        "Agents write large, clean plans. Then the plans break apart during real work.",
        "The cost to change agent-written code is close to zero. So why pay for a plan up front?",
        "Work one story at a time. Review as you go. This is the agile method.",
    ],

    "mechanism": [
        "Uncle Bob tried a large upfront plan with agents in the same week as this talk. He calls"
        " the result \"always a disaster.\" The same pattern repeats each time. He plans in"
        " detail. He gives the plan to the agents. The agents run ahead on the plan. At some"
        " point it is clear the agents cannot follow the plan. They did not see every gap he did."
        " So he must stop, go back, rewrite the plan, and start again.",

        "He points to a clear parallel in software history. A large plan made before any code"
        " led to waterfall in the 1970s. The agile method was the industry's fix for that"
        " problem. He argues agents need the same fix now, because the failure looks the same."
        " In his words: \"The agents love to write plans. Oh my goodness, they love it. And they"
        " will embellish the plans and the plans will be gorgeous and beautiful and spell out all"
        " kinds of details\" — and then the plans break apart once real work starts.",

        "His case for small steps is about cost, not just his own experience. Picture a house"
        " where every change costs one dollar, even a change to the foundation. You would not pay"
        " an architect a large fee for a perfect plan. You would stand next to the builder and"
        " change the kitchen, the stairs, or the layout as you go, because a change costs almost"
        " nothing. He argues that the cost to change agent-written code has \"plummeted to as"
        " close to zero as we're ever going to get it.\" This removes the reason to pay for a"
        " perfect plan up front, the same way it removes that reason for the house.",

        "Here is what he does instead. He builds one or two stories. Then he checks the"
        " structure. He steps in by hand if needed. Then he builds a few more stories, and"
        " repeats this cycle. He admits: \"we may never escape that manual organizing step at the"
        " end.\" He also does not keep specs as permanent files in the repo. He treats a spec as"
        " a short-lived note. He writes it, uses it, and drops it, because there is no"
        " human-written source code left to act as the final spec a document must match.",
    ],

    "numbers": [],

    "analogy": {
        "text": "If it cost you a dollar to make a change to a house, including the initial laying"
                " of the foundation... would you hire an architect... or would you walk up to the"
                " contractor and say, 'Put the kitchen over here'?",
        "note": "The cost of a change decides whether a plan made up front is worth its price."
                " With agents, that cost has dropped toward zero. So the case for a plan made"
                " up front drops with it.",
    },

    "practice": [
        "Do not give an agent a full plan and walk away. Review the work after each story, not"
        " after the whole plan.",
        "Treat an agent-written plan as a draft to question, not a contract to build word for"
        " word.",
        "Stop keeping specs as permanent files in the repo, if nothing keeps them in sync with"
        " the code.",
        "To share a tool with others, point another agent at your tool and let it build its own"
        " version. Do not write a spec for someone else's agent to follow.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
