NOTE = {
    "id": "tactical-vs-strategic",
    "concept": "Tactical versus strategic programming",
    "one_liner": "Agents work well at tactical programming, which means writing one piece of code"
                 " that works. Agents work poorly at strategic programming, which means deciding"
                 " how a whole system should be built. This changes what a junior developer"
                 " should practice.",

    "prerequisites": [],
    "related": ["strategic-load"],

    "skeleton": [
        "Tactical work is the soldier fighting one battle. Strategic work is the general"
        " planning the war.",
        "Agents are strong at tactical work. Agents are weak at strategic work.",
        "A junior's fix: let a team treat you like an agent for a while, on purpose.",
        "Fundamentals exist to make complex systems easy to grasp, for people and for models.",
    ],

    "mechanism": [
        "Uncle Bob uses John Ousterhout's split between tactical and strategic programming."
        " Tactical work is \"the sergeant on the ground, the person kind of fighting the"
        " battle.\" Strategic work is \"the general kind of the person directing the course of"
        " the war.\" Both speakers agree that agents are strong at tactical work. Agents move"
        " fast and get one task done well. But agents are weak at strategic work, the decisions"
        " about how a whole system should be shaped.",

        "This split changes how a junior developer should spend their time. Uncle Bob's advice:"
        " write code by hand for about a year first. This shows you what the agents actually"
        " deal with. Next, once you join a team that uses agents a lot, expect to be treated"
        " like one of the agents. You will get the same small tasks, checked by the same tools."
        " Spend months \"horribly unproductive but learning a hell of a lot,\" before anyone"
        " trusts you to direct an agent yourself. This matches advice he has given for decades:"
        " if you have never written assembly language, spend a weekend writing it, so you"
        " understand what runs beneath a high-level language. The same idea now adds one more"
        " step. Learn binary, then assembly, then a high-level language, then agent work under"
        " strict tools, and only then direct an agent yourself at the strategic level.",

        "The real skill underneath all of this, he says, is recognition. Back in December, what"
        " told him his agents were struggling was not just messy output. It was watching them"
        " thrash: fixing one thing while breaking another, going in circles, one agent almost"
        " giving up. He recognized the struggle because he had lived through the same struggle"
        " himself, by hand. A new developer who has never done the tactical work has nothing to"
        " compare it against.",

        "His closing point on why fundamentals still matter comes from a claim he credits to"
        " Dijkstra, though he is not fully sure of the source: software is the most complex"
        " thing humans have ever tried to build. So the fundamentals exist to organize that"
        " complexity into something people can grasp, and models can grasp it too, since models"
        " are built on human patterns. He treats the claim \"agents make fundamentals useless\""
        " as the same complaint every past change has caused. Assembly replaced binary."
        " Compilers replaced assembly. Now models sit above the compiler. Each time, people"
        " predicted the old skill would stop mattering. In his words: \"The rules you throw away"
        " are the ones you're going to pick up off the floor in a year and dust off and"
        " remember why you need them.\"",
    ],

    "numbers": [],

    "analogy": {
        "text": "If you've never written assembly language, you should spend the weekend writing"
                " assembly language just so that you know what's really going on behind the"
                " scenes.",
        "note": "This is his old advice for programmers who use high-level languages, with one"
                " more step added: spend real time doing agent-style work, so you understand"
                " what agents deal with, before you try to direct one.",
    },

    "practice": [
        "Write code yourself for a real stretch of time before you lean on agents. This gives"
        " you the experience to see when an agent is struggling.",
        "If you are junior on a team that uses agents a lot, treat months of small, checked"
        " tasks as the fastest path to strategic skill, not as a step down.",
        "Read older books (Tom DeMarco, Ed Yourdon, The Pragmatic Programmer) for judgment."
        " Skip the old tech details. Keep the reasoning.",
        "When an agent looks stuck, watch for thrashing: fixing one thing while breaking"
        " another. Do not just judge the output.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
