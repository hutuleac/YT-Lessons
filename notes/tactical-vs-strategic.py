NOTE = {
    "id": "tactical-vs-strategic",
    "concept": "Tactical versus strategic programming",
    "one_liner": "Agents are strong at tactical programming — getting a specific piece of code"
                 " working — and weak at strategic programming — deciding how the system should be"
                 " organized — which changes what a junior actually needs to practice.",

    "prerequisites": [],
    "related": ["strategic-load"],

    "skeleton": [
        "Tactical is the sergeant fighting the battle; strategic is the general directing the war.",
        "Agents are strong tactically, weak strategically.",
        "A junior's fix: get treated like an agent for a while, on purpose.",
        "Fundamentals exist to make complexity conceivable — by people and by models.",
    ],

    "mechanism": [
        "Uncle Bob borrows John Ousterhout's split between tactical and strategic programming:"
        " tactical is \"the sergeant on the ground, the person kind of fighting the battle,\""
        " strategic is \"the general kind of the person directing the course of the war.\" Both"
        " speakers agree agents land firmly on the tactical side — fast, capable in the moment —"
        " and are weak on the strategic side, the decisions about how a whole system should be"
        " shaped.",

        "That split reframes how a junior developer should spend their time. His recommended path:"
        " write code yourself for roughly a year first, so you know what the agents are actually"
        " dealing with. Then, once hired somewhere agent-heavy, expect to be treated like one of"
        " the agents — given the same deterministic-tool-constrained tasks — and spend months"
        " \"horribly unproductive but learning a hell of a lot\" before anyone trusts you to"
        " direct an agent yourself. It echoes advice he's given for decades: if you've never"
        " written assembly language, spend a weekend doing it, so you understand what's really"
        " happening beneath a high-level language. The same ladder logic now extends one more"
        " rung — binary, assembly, a higher-level language, agent work under deterministic tools,"
        " and only then strategic supervision of an agent.",

        "The recognition skill underneath this is the one he says actually matters. Back in"
        " December, what told him his agents were struggling wasn't the messy output on its own —"
        " it was watching them thrash: fixing one thing while inadvertently breaking another,"
        " going in circles, one agent effectively giving up. He recognized the struggle because"
        " he'd lived through the same struggle himself, doing it by hand. A novice who's never"
        " done the tactical work has nothing to recognize it against.",

        "His closing argument for why the fundamentals still matter, attributed — with some"
        " hedging on the exact source — to Dijkstra: software is the most complicated thing"
        " humans have ever attempted, so the fundamentals are how that complexity gets organized"
        " into something conceivable, by humans and by models alike, since the models are"
        " themselves modeled after humans. He frames \"agents make fundamentals obsolete\" as the"
        " same complaint every abstraction layer has triggered — assembly over binary, compilers"
        " over assembly, and now models above the compiler — always accompanied by predictions"
        " that the underlying skill would stop mattering. \"The rules you throw away are the ones"
        " you're going to pick up off the floor in a year and dust off and remember why you need"
        " them.\"",
    ],

    "numbers": [],

    "analogy": {
        "text": "If you've never written assembly language, you should spend the weekend writing"
                " assembly language just so that you know what's really going on behind the"
                " scenes.",
        "note": "His decades-old advice for high-level-language programmers, extended one more"
                " rung: spend real time doing agent-constrained work so you understand what"
                " agents are actually dealing with, before you try to direct one.",
    },

    "practice": [
        "Write code yourself for a real stretch before leaning on agents — you need the reference"
        " experience to recognize when an agent is struggling.",
        "If you're junior on an agent-heavy team, treat months of constrained, agent-style tasks"
        " as the fastest path to strategic judgment, not as a demotion.",
        "Read older books (Tom DeMarco, Ed Yourdon, The Pragmatic Programmer) for the judgment"
        " layer — filter the dated tech, keep the reasoning.",
        "When an agent looks stuck, watch for thrashing — fixing one thing, breaking another — not"
        " just the quality of what it outputs.",
    ],

    "diagrams": [],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
