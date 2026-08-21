NOTE = {
    "id": "spec-driven-trap",
    "concept": "The spec-driven development trap",
    "one_liner": "Handing an agent a heavy upfront plan fails the same way waterfall failed on"
                 " humans, because agents love writing gorgeous, detailed plans that fall apart"
                 " the moment implementation starts.",

    "prerequisites": [],
    "related": ["review-checkpoints"],

    "skeleton": [
        "Heavy upfront planning for agents repeats the 1970s waterfall mistake.",
        "Agents write gorgeous plans, and the plans fall apart in implementation.",
        "The cost of changing agent-written code is near zero — so why pay upfront for a plan?",
        "Iterate a story at a time and review, the way agile always argued for.",
    ],

    "mechanism": [
        "Uncle Bob tried heavy upfront planning with agents the same week as this conversation,"
        " and calls the result \"always a disaster.\" The pattern repeats every time: he plans"
        " thoroughly, hands it to the agents, and the agents run ahead on the plan until it's"
        " clear they can't actually follow it — they didn't anticipate everything he did, and"
        " aren't as wise as he is about the gaps — forcing him to stop, back up, rewrite the plan,"
        " and start over.",

        "He draws a direct line to software history: heavy upfront specification produced"
        " waterfall in the 1970s, and the agile movement was the industry's correction to that"
        " failure. He argues the same correction is needed now for agents, because the failure"
        " mode is identical. \"The agents love to write plans. Oh my goodness, they love it. And"
        " they will embellish the plans and the plans will be gorgeous and beautiful and spell out"
        " all kinds of details\" — and then they fall apart once implementation actually starts.",

        "His argument for why iteration wins is economic, not just experiential. If every change"
        " to a house — including laying the foundation — cost a flat dollar, you wouldn't pay an"
        " architect thousands for a perfect upfront plan; you'd stand next to the contractor and"
        " adjust the kitchen, the stairs, the traffic pattern as you went, because changing your"
        " mind is nearly free. He argues the cost of changing code with agents has \"plummeted to"
        " as close to zero as we're ever going to get it,\" which removes the economic case for"
        " paying upfront for a perfect plan the same way it removed it for the house.",

        "What he does instead: a story or two, then review the architecture, intervene manually"
        " if needed, then a few more stories, repeating — admitting \"we may never escape that"
        " manual organizing step at the end.\" He also doesn't persist specifications in the repo"
        " at all; they're ephemeral, fiddled with and discarded, since there's no longer a"
        " human-authored source code to treat as the final spec that a document needs to stay"
        " consistent with.",
    ],

    "numbers": [],

    "analogy": {
        "text": "If it cost you a dollar to make a change to a house, including the initial laying"
                " of the foundation... would you hire an architect... or would you walk up to the"
                " contractor and say, 'Put the kitchen over here'?",
        "note": "The cost of change is what decides whether upfront planning pays for itself — and"
                " with agents, that cost has collapsed toward zero, so the case for paying it"
                " upfront collapses with it.",
    },

    "practice": [
        "Don't hand an agent a fully-specified plan and walk away — review after each story, not"
        " after the whole plan.",
        "Treat an agent-written plan as a draft to interrogate, not a contract to implement"
        " verbatim.",
        "Stop keeping specs as permanent repo artifacts if nothing actually enforces them staying"
        " in sync with the code.",
        "To share reusable tooling, point another agent at your existing tool and have it build"
        " its own version, rather than writing a spec for someone else's agent to follow.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
