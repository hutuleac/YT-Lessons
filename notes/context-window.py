NOTE = {
    "id": "context-window",
    "concept": "The context window",
    "one_liner": "The context window is the whole conversation — input and output tokens together"
                 " — capped by a hard per-model limit, and the fuller it gets the less attention"
                 " the middle of it receives.",
    "prerequisites": ["tokens"],
    "related": ["dumb-zone", "message-anatomy"],

    "skeleton": [
        "The window is input plus output tokens — the whole thing, not one side.",
        "Every model has a hard limit and you get an error when you cross it.",
        "You can hit the limit mid-generation; the model can't route around its own ceiling.",
        "The bigger the window, the worse lost-in-the-middle gets.",
    ],

    "mechanism": [
        "The common confusion is thinking the window is the input, or the output, or the model's"
        " memory. It is all of it: system prompt, user messages, reasoning tokens and the"
        " assistant's replies are one pool of tokens, and that pool is the context window.",

        "It grows as the conversation grows, and it cannot grow forever. Each model has a"
        " hard-coded limit on how many tokens it can see at once, and querying past that limit"
        " returns an error from the API. You can also hit it part-way through a generation — the"
        " reply starts fine and runs into the ceiling — because the model is not smart enough to"
        " work around its own limit.",

        "The subtler failure matters more. In a long conversation the messages at the start carry"
        " weight and so do the ones at the end, but the material in the middle gets attended to"
        " least. This is the lost-in-the-middle effect, and it is more pronounced the larger the"
        " window gets — a model may struggle to retrieve information from its own context.",

        "So a big advertised window is not the win it looks like. A model that supports an"
        " enormous context still has lost-in-the-middle problems inside it, and you will get"
        " better results from using fewer tokens regardless of what the limit allows.",

        "Ross Mike's practical version of the same effect: watch the context-used percentage"
        " Claude Code shows you, and start a fresh session around 40-50% rather than riding a"
        " single session to its ceiling. His number for Opus 4.5's 200k-token window is a rough"
        " rule of thumb from his own use, not a measured threshold — but it matches the mechanism"
        " above, since that's the point past which lost-in-the-middle has more of the window to"
        " work with.",
    ],

    "numbers": [
        {"value": "40-50%", "unit": "context used", "label": "Ross Mike's rule of thumb for when to start a fresh session, on Opus 4.5's 200k-token window"},
    ],

    "analogy": {
        "text": "The context window is not any part of this — it's the whole thing.",
        "note": "Holding input and output in one pool is what makes the later maths work: every"
                " tool definition, every reasoning token and every reply is competing for the"
                " same ceiling.",
    },

    "practice": [
        "Count the whole conversation against the limit, not just what you typed.",
        "Put what matters at the start or the end; the middle is where attention thins.",
        "Read a big advertised window as headroom, not as usable capacity.",
        "Expect mid-generation failures on long replies and leave room for the output.",
    ],

    "diagrams": [
        {
            "title": "Attention is U-shaped across a long history",
            "caption": "Start and end land; the middle thins out. The effect gets stronger as the"
                       " window gets bigger, which is why huge contexts disappoint.",
            "svg": '''<svg viewBox="0 0 460 200" role="img"
  aria-label="A curve showing attention high at the beginning of a conversation, dipping through the middle, and rising again at the end, over a row of message markers.">
  <line x1="34" y1="150" x2="440" y2="150" stroke="var(--line)" stroke-width="1"/>
  <line x1="34" y1="20" x2="34" y2="150" stroke="var(--line)" stroke-width="1"/>
  <path d="M34 40 C 120 66, 150 118, 237 120 C 324 118, 354 66, 440 40"
        fill="none" stroke="var(--signal)" stroke-width="2.5" stroke-linecap="round"/>
  <rect x="150" y="20" width="174" height="130" fill="var(--interference)" opacity="0.12"/>
  <text x="237" y="100" class="d-label" text-anchor="middle">lost in the middle</text>
  <g fill="var(--muted)">
    <circle cx="60" cy="166" r="4"/><circle cx="106" cy="166" r="4"/><circle cx="152" cy="166" r="4"/>
    <circle cx="198" cy="166" r="4"/><circle cx="244" cy="166" r="4"/><circle cx="290" cy="166" r="4"/>
    <circle cx="336" cy="166" r="4"/><circle cx="382" cy="166" r="4"/><circle cx="428" cy="166" r="4"/>
  </g>
  <text x="14" y="88" class="d-label" text-anchor="middle" transform="rotate(-90 14 88)">attention</text>
  <text x="60" y="192" class="d-label">oldest message</text>
  <text x="440" y="192" class="d-label" text-anchor="end">newest message</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/9P36wMntNSI",
        "channel": "Matt Pocock",
        "title": "Stop stuffing your context window (here's why)",
        "duration": "2:09",
    },
}
