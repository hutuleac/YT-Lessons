NOTE = {
    "id": "effort-levels",
    "concept": "Your effort level is too high",
    "one_liner": "Effort is thinking tokens spent per task, and the benchmarks that justify"
                 " cranking it up hold the task fixed — but you can rewrite the task, and a"
                 " better-specified task needs less effort.",
    "prerequisites": ["tokens"],
    "related": ["model-cost-curve", "review-checkpoints"],

    "skeleton": [
        "Higher effort means more thinking tokens for the same work.",
        "Exploration barely benefits from effort — it just costs more.",
        "Benchmarks hold the task static. You don't have to.",
        "Start at the lowest effort you have and crank up only if you need to.",
    ],

    "mechanism": [
        "Effort level controls how many reasoning tokens the agent spends. Crank it up and it"
        " thinks harder about the same work — including the parts that do not reward thinking."
        " Exploring a codebase is the clearest case: it is a task you do not really need effort"
        " for, so extra effort mostly buys you a slower, more expensive traversal and an agent"
        " pushing hard on things that did not need pushing.",

        "The benchmark charts do show quality rising with effort, and Pocock's objection to them"
        " is precise: those charts hold the task static. The task is a fixed prompt on a fixed"
        " problem. You, unlike the benchmark, can change how the task is specified.",

        "That is the substitution worth understanding. High-quality information given to the agent"
        " up front does the work that reasoning tokens would otherwise have to do. The better the"
        " spec, the less effort the same job requires — so effort is a knob you reach for when"
        " your specification has run out, not the first thing you turn up.",

        "The practical recommendation is to start at the lowest effort level you have access to"
        " and raise it from there. Not zero: some thinking tokens are worth having, because chain"
        " of thought is a genuinely useful way to work with agents.",
    ],

    "numbers": [],

    "analogy": {
        "text": "The more high-quality information you give it, the lower effort you actually"
                " need to complete the task.",
        "note": "It turns effort from a quality dial into a symptom: if you need max effort for"
                " routine work, the specification is doing too little.",
    },

    "practice": [
        "Start at the lowest effort level available and raise it only when output actually suffers.",
        "Don't spend effort on exploration — spend it on the reasoning-heavy step, if any.",
        "Improve the spec before raising the dial; information substitutes for thinking tokens.",
        "Keep some thinking tokens — chain of thought is worth its cost.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/shorts/iQb3F9UzBR4",
        "channel": "Matt Pocock",
        "title": "Your effort level is TOO DAMN HIGH",
        "duration": "1:17",
    },
}
