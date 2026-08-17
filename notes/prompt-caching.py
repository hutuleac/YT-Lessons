NOTE = {
    "id": "prompt-caching",
    "concept": "Prompt caching",
    "one_liner": "Every message resends the whole conversation so far, but Anthropic caches that"
                 " growing history as a document Claude re-reads instead of reprocessing — so a"
                 " message that continues an active conversation costs a fraction of one that"
                 " doesn't, and the gap between those two prices is 20x.",

    "prerequisites": ["context-window"],
    "related": ["cache-loss-recovery"],

    "skeleton": [
        "Every message resends the entire conversation, not just the new text.",
        "That growing history is cached as a document Claude re-reads instead of reprocessing.",
        "A cache write costs 2x base input price; a cache read costs 1/10th — a 20x swing.",
        "The cache expires after 1 hour of no activity, and refreshes on every message sent.",
        "Switching model, effort, MCPs, or compacting resets it early, mid-conversation.",
    ],

    "mechanism": [
        "A follow-on message never sends just its own text. Ask something short after an earlier"
        " exchange and what actually reaches Anthropic is that earlier exchange plus the new"
        " message, because the model needs the full history to understand context. Left alone,"
        " this compounds every single turn until a real conversation is carrying tens or hundreds"
        " of thousands of tokens on every message.",

        "Caching is what keeps that from being reprocessed at full price each time. Think of the"
        " cache as a document Claude already has in front of it, holding the conversation so far —"
        " reading that document is far cheaper than being handed the same text cold. Writing a"
        " new turn into the cache for the first time costs double the base input rate (about"
        " $20 per million tokens); reading what's already cached costs about a tenth of the base"
        " rate (about $1 per million). Base input pricing on its own is close to meaningless,"
        " since almost every real message is one or the other of these two rates, never the"
        " sticker number.",

        "The cache is not permanent — it holds for 1 hour of no activity and the clock resets on"
        " every message sent, so an active back-and-forth stays cheap indefinitely. Walk away for"
        " over an hour, though, and it's gone: a 500,000-token conversation that would have cost"
        " about 50 cents to continue at the cache-read rate instead gets billed as if none of it"
        " had ever been processed, at the cache-write rate — roughly $10 for the same next"
        " message. Nothing else covered in this lesson saves anywhere close to this much.",

        "Time isn't the only way to lose it. Per Anthropic's own documentation, switching model,"
        " changing effort level, toggling fast mode, connecting or disconnecting an MCP server,"
        " enabling a plugin, denying a tool call, compacting the conversation, or upgrading the"
        " CLI all invalidate the cache immediately — the very next message is priced at the full"
        " write rate regardless of how long the conversation has been running.",
    ],

    "numbers": [
        {"value": "$20", "unit": "per million tokens", "label": "cache write (1-hour), roughly 2x base input"},
        {"value": "$1", "unit": "per million tokens", "label": "cache read, roughly 1/10 base input"},
        {"value": "20x", "unit": "cost multiple", "label": "cache read vs. cache write for the same tokens"},
        {"value": "1 hour", "unit": "of inactivity", "label": "before the cache expires; refreshes on every message"},
        {"value": "~$0.50", "unit": "vs ~$10", "label": "next message on a 500k-token conversation, warm vs. cold"},
    ],

    "analogy": {
        "text": "\"I want you to think of the message cache as simply a document that Claude has"
                " in front of it that has your entire conversation up until that point.\"",
        "note": "Reframes caching from something invisible happening to your tokens into a"
                " physical object with a shelf life — it makes the 1-hour expiry intuitive: the"
                " document gets taken away, not silently forgotten.",
    },

    "practice": [
        "Don't leave an important long conversation idle for over an hour if you intend to"
        " continue it — the next message pays full cache-write price for everything before it.",
        "Avoid switching models, effort level, or MCPs mid-conversation if preserving the cache"
        " matters more than the change.",
        "If you must step away for over an hour, decide in advance whether to /clear, /compact,"
        " or hand off — don't just come back and send the next message cold.",
    ],

    "diagrams": [
        {
            "title": "Every message resends the history",
            "caption": "Message 2 isn't 6 tokens — it's message 1's 9 tokens plus the new 6.",
            "svg": '''<svg viewBox="0 0 480 190" role="img"
  aria-label="Two stacked message rows. Message 1 sends 5 input and 4 output tokens. Message 2 must resend all 9 of those tokens plus its own 6 new input tokens, for 15 tokens actually sent.">
  <text x="0" y="18" class="d-label">message 1</text>
  <rect x="0" y="26" width="60" height="30" rx="3" fill="var(--signal)" opacity="0.45"/>
  <text x="30" y="46" class="d-num" text-anchor="middle">5</text>
  <rect x="66" y="26" width="60" height="30" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="96" y="46" class="d-num" text-anchor="middle">4</text>
  <text x="132" y="46" class="d-label">in / out — 9 tokens total</text>

  <text x="0" y="92" class="d-label">message 2 (what you think you send)</text>
  <rect x="0" y="100" width="60" height="30" rx="3" fill="var(--surface-2)" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="30" y="120" class="d-num" text-anchor="middle">6</text>
  <text x="66" y="120" class="d-label">new input only</text>

  <text x="0" y="152" class="d-label">message 2 (what actually gets sent)</text>
  <rect x="0" y="160" width="60" height="26" rx="3" fill="var(--signal)" opacity="0.45"/>
  <rect x="60" y="160" width="48" height="26" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <rect x="108" y="160" width="60" height="26" rx="3" fill="var(--interference)" opacity="0.5"/>
  <text x="192" y="178" class="d-fix">msg 1 (9) + new (6) = 15 tokens, every turn</text>
</svg>''',
        },
        {
            "title": "Cache write vs. cache read: a 20x gap",
            "caption": "Same 500k-token history, two prices depending on whether the hour ran out.",
            "svg": '''<svg viewBox="0 0 460 232" role="img"
  aria-label="Bar chart comparing the cost of the next message on a 500,000 token conversation: about 50 cents if the cache is still warm (cache read), versus about 10 dollars if the cache expired (cache write), a 20x difference.">
  <line x1="90" y1="16" x2="90" y2="168" stroke="var(--line)" stroke-width="1"/>
  <line x1="90" y1="168" x2="440" y2="168" stroke="var(--line)" stroke-width="1"/>

  <text x="0" y="52" class="d-label">warm</text>
  <text x="0" y="66" class="d-label">(within 1h)</text>
  <rect x="90" y="44" width="16" height="124" fill="var(--signal)"/>
  <text x="116" y="52" class="d-num">~$0.50</text>
  <text x="116" y="68" class="d-label">cache read, $1/M</text>

  <text x="0" y="132" class="d-label">cold</text>
  <text x="0" y="146" class="d-label">(&gt;1h idle)</text>
  <rect x="230" y="26" width="16" height="142" fill="var(--interference)"/>
  <text x="256" y="34" class="d-num">~$10</text>
  <text x="256" y="50" class="d-label">cache write, $20/M</text>

  <text x="0" y="196" class="d-fix">same conversation, same next message &#8212;</text>
  <text x="0" y="214" class="d-fix">20x apart on timing alone</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=V0XbuApxlhg",
        "channel": "Chase AI",
        "title": "You're Paying Anthropic 20x MORE Than You Need To",
        "duration": "18:59",
    },
}
