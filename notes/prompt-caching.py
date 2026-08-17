NOTE = {
    "id": "prompt-caching",
    "concept": "Prompt caching",
    "one_liner": "A cache stores your growing conversation, so Claude reads it cheaply on each"
                 " new message instead of paying full price to process it again.",

    "prerequisites": ["context-window"],
    "related": ["cache-loss-recovery"],

    "skeleton": [
        "Each message resends your full chat history.",
        "The cache stores that history for fast, cheap reads.",
        "Writing to the cache costs more than reading from it.",
        "The cache ends after 1 hour with no new messages.",
        "Switching models or running /compact ends the cache early.",
    ],

    "mechanism": [
        "A follow-on message never sends only its own text. Ask a short question after an"
        " earlier exchange, and Anthropic still receives that earlier exchange too, because the"
        " model needs the full history to answer. Left alone, this grows every turn until a long"
        " conversation resends tens or hundreds of thousands of tokens on each message.",

        "Caching exists so that history is not reprocessed at full cost each time. The first"
        " time a stretch of conversation is sent, Claude's infrastructure does real work: it"
        " computes how each token relates to the ones before it, then stores that result. That"
        " stored result is the cache. A cache write pays for this extra compute and storage,"
        " which is why it costs more than a normal input token. A cache read skips the"
        " computation — Claude reuses the stored result — so it costs a fraction of the price.",

        "A subscription plan, which is what Claude Code runs on, writes every cache at a 1-hour"
        " hold. The Anthropic API also offers a 5-minute cache, priced lower at write time for"
        " callers who send requests close together and don't need the longer hold: 1.25x the"
        " base rate, against 2x for the 1-hour option. Once written, a hit on either cache costs"
        " about a tenth of the base input price — the read saving is the same either way, only"
        " the write price and the hold time differ.",

        "None of this holds forever. The cache expires after 1 hour of no activity, and the"
        " clock resets on every message sent, so an active back-and-forth stays cheap"
        " indefinitely. Per Anthropic's documentation, switching model, changing effort level,"
        " toggling fast mode, connecting or disconnecting an MCP server, enabling a plugin,"
        " denying a tool call, compacting, or upgrading the CLI all end the cache immediately."
        " Walk away for over an hour on a 500,000-token conversation, and the next message jumps"
        " from about 50 cents (cache read) to about $10 (cache write) for the same history.",
    ],

    "numbers": [
        {"value": "$10", "unit": "per million tokens", "label": "base input price (Claude Fable 5)"},
        {"value": "$12.50", "unit": "per million tokens", "label": "5-minute cache write, 1.25x base — API only"},
        {"value": "$20", "unit": "per million tokens", "label": "1-hour cache write, 2x base — Claude Code default"},
        {"value": "$1", "unit": "per million tokens", "label": "cache read, 0.1x base — 20x cheaper than the 1-hour write"},
        {"value": "~$0.50 vs ~$10", "unit": "next message, 500k-token chat", "label": "cache read vs. cache write, same history"},
    ],

    "analogy": {
        "text": "\"I want you to think of the message cache as simply a document that Claude has"
                " in front of it that has your entire conversation up until that point.\"",
        "note": "A physical object with a shelf life, not invisible magic — it makes the expiry"
                " intuitive: the document gets taken away, not silently forgotten.",
    },

    "practice": [
        "Send your next message within the hour to keep the cache warm.",
        "Avoid changing model, effort, or MCPs mid-task if the cache matters to you.",
        "Use 5-minute caching on the API for quick, one-off calls; use 1-hour for longer work.",
        "Plan your break before it happens: /clear, /compact, or hand off — not after.",
    ],

    "diagrams": [
        {
            "title": "Every message resends the history",
            "caption": "Message 2 is not 6 tokens. It is message 1's 9 tokens plus the new 6.",
            "svg": '''<svg viewBox="0 0 480 190" role="img"
  aria-label="Two stacked message rows. Message 1 sends 5 input and 4 output tokens. Message 2 must resend all 9 of those tokens plus its own 6 new input tokens, for 15 tokens actually sent.">
  <text x="0" y="18" class="d-label">message 1</text>
  <rect x="0" y="26" width="60" height="30" rx="3" fill="var(--signal)" opacity="0.45"/>
  <text x="30" y="46" class="d-num" text-anchor="middle">5</text>
  <rect x="66" y="26" width="60" height="30" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="96" y="46" class="d-num" text-anchor="middle">4</text>
  <text x="132" y="46" class="d-label">in / out, 9 tokens</text>

  <text x="0" y="92" class="d-label">message 2 &#8212; you type</text>
  <rect x="0" y="100" width="60" height="30" rx="3" fill="var(--surface-2)" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="30" y="120" class="d-num" text-anchor="middle">6</text>
  <text x="66" y="120" class="d-label">new tokens only</text>

  <text x="0" y="152" class="d-label">message 2 &#8212; actually sent</text>
  <rect x="0" y="160" width="60" height="26" rx="3" fill="var(--signal)" opacity="0.45"/>
  <rect x="60" y="160" width="48" height="26" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <rect x="108" y="160" width="60" height="26" rx="3" fill="var(--interference)" opacity="0.5"/>
  <text x="176" y="178" class="d-fix">9 + 6 = 15 tokens, every turn</text>
</svg>''',
        },
        {
            "title": "Write once, read many times",
            "caption": "The write pays for the compute that builds the cache. Every read after"
                       " that reuses it.",
            "svg": '''<svg viewBox="0 0 480 230" role="img"
  aria-label="A new message enters a compute step that writes it into the cache at the higher write price. Every later message reads that same cache at the much lower read price, shown as a repeating loop."
       >
  <rect x="0" y="86" width="92" height="40" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="46" y="110" class="d-node" text-anchor="middle">new turn</text>

  <path d="M92 106 L 158 106" stroke="var(--interference)" stroke-width="2" fill="none" marker-end="url(#pc-a1)"/>
  <text x="94" y="94" class="d-fix">write</text>

  <rect x="164" y="70" width="150" height="72" rx="6" fill="var(--surface-2)" stroke="var(--signal)" stroke-width="2"/>
  <rect x="180" y="92" width="20" height="14" rx="2" fill="none" stroke="var(--sand)" stroke-width="2"/>
  <path d="M184 92 v-6 a4 4 0 0 1 8 0 v6" fill="none" stroke="var(--sand)" stroke-width="2"/>
  <text x="239" y="102" class="d-node" text-anchor="middle">cache</text>
  <text x="239" y="120" class="d-label" text-anchor="middle">stored once</text>

  <path d="M314 96 C 360 70, 400 70, 400 96" stroke="var(--signal)" stroke-width="2" fill="none" marker-end="url(#pc-a2)"/>
  <path d="M400 116 C 400 142, 360 142, 314 116" stroke="var(--signal)" stroke-width="2" fill="none" marker-end="url(#pc-a2)"/>
  <text x="330" y="60" class="d-fix">read, read, read &#8230;</text>

  <rect x="400" y="86" width="80" height="40" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="440" y="110" class="d-node" text-anchor="middle">reply</text>

  <defs>
    <marker id="pc-a1" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="var(--interference)"/></marker>
    <marker id="pc-a2" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="var(--signal)"/></marker>
  </defs>

  <text x="0" y="176" class="d-label">write: pay once, 1.25x&#8211;2x base</text>
  <text x="0" y="196" class="d-label">read: pay each time, 0.1x base</text>
</svg>''',
        },
        {
            "title": "Four prices for the same tokens",
            "caption": "Claude Fable 5 rates. Read is the cheapest way to move a token through"
                       " the model twice.",
            "svg": '''<svg viewBox="0 0 460 230" role="img"
  aria-label="Bar chart of four token prices per million on Claude Fable 5: cache read at 1 dollar, base input at 10 dollars, 5-minute cache write at 12.50 dollars, and 1-hour cache write at 20 dollars.">
  <line x1="10" y1="180" x2="450" y2="180" stroke="var(--line)" stroke-width="1"/>

  <rect x="30" y="170" width="34" height="10" fill="var(--signal)"/>
  <text x="47" y="150" class="d-num" text-anchor="middle">$1</text>
  <text x="47" y="200" class="d-label" text-anchor="middle">read</text>

  <rect x="130" y="100" width="34" height="80" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="147" y="90" class="d-num" text-anchor="middle">$10</text>
  <text x="147" y="200" class="d-label" text-anchor="middle">base</text>

  <rect x="230" y="80" width="34" height="100" fill="var(--sand)" opacity="0.65"/>
  <text x="247" y="70" class="d-num" text-anchor="middle">$12.50</text>
  <text x="247" y="200" class="d-label" text-anchor="middle">5-min write</text>

  <rect x="330" y="20" width="34" height="160" fill="var(--interference)"/>
  <text x="347" y="10" class="d-num" text-anchor="middle">$20</text>
  <text x="347" y="200" class="d-label" text-anchor="middle">1-hour write</text>

  <text x="10" y="222" class="d-fix">read is 20x cheaper than a 1-hour write, same tokens</text>
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
