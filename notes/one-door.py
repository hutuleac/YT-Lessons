NOTE = {
    "id": "one-door",
    "concept": "One door instead of many",
    "one_liner": "Encapsulate a function's fan-out behind a single entry point so an agent learns"
                 " what it does by reading one function instead of jumping through every function"
                 " it calls."
                 ,

    "prerequisites": ["tool-overload"],
    "related": ["dumb-zone", "docs-drift"],

    "skeleton": [
        "A main function calling many small functions means many doors to open.",
        "Learning it means jumping through every function it calls, one by one.",
        "Each jump costs tokens — the hops add up fast.",
        "Fix: one entry point in front, each function still keeps its own file.",
    ],

    "mechanism": [
        "Picture a payment-processing function that calls calculate discounts, validate cards, and"
        " several other small functions. To understand what the main function does, an agent has"
        " to open every one of those doors — read each called function, and often what those call"
        " in turn — before it has learned how the whole thing behaves. That is a real benefit for"
        " unit testing, since each small function is independently testable, but it is a token"
        " cost for comprehension: understanding the main function this way might spend on the"
        " order of ten thousand tokens working through every door.",

        "The fix is not to merge everything into one giant file — that trades a comprehension"
        " problem for an unmaintainable one. Each function keeps its own file. What changes is that"
        " the many small functions get one shared entry point in front of them, so the agent — and"
        " the rest of the program — has a single door to walk through instead of many. Reading"
        " that one door can cost closer to a thousand tokens instead of ten thousand, because the"
        " agent no longer has to trace every function calling every other function back and forth"
        " to build a mental model.",

        "This only pays off if the door is real, not decorative — a wrapper that just forwards"
        " every call unchanged adds a hop without removing any of the underlying ones. The"
        " companion move for finding out which of those many small functions are still pulling"
        " their weight is the [[deletion-test]].",
    ],

    "numbers": [
        {"value": "~10,000", "unit": "tokens", "label": "estimated cost of learning via many doors"},
        {"value": "~1,000", "unit": "tokens", "label": "estimated cost of learning via one door"},
    ],

    "analogy": None,

    "practice": [
        "Give a cluster of small, related functions one shared entry point instead of exposing"
        " each one directly.",
        "Keep each function in its own file — the fix is one door, not one giant file.",
        "Before adding an entry point, check it actually reduces hops rather than just adding one.",
    ],

    "diagrams": [
        {
            "title": "Many doors vs. one door",
            "caption": "Same functions, same files — the difference is how many hops it takes to"
                       " learn what the whole thing does.",
            "svg": '''<svg viewBox="0 0 480 210" role="img"
  aria-label="Left: a main function connected directly to five small functions, each a separate door the agent must open, costing about ten thousand tokens to understand. Right: the same five functions behind one shared entry point, so the agent opens a single door, costing about one thousand tokens.">
  <text x="0" y="14" class="d-label">MANY DOORS</text>
  <rect x="60" y="24" width="90" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="105" y="43" class="d-node" text-anchor="middle">main</text>
  <path d="M105 54 V70" stroke="var(--interference)" stroke-width="1.2"/>
  <path d="M105 70 H10 M105 70 H200" stroke="var(--interference)" stroke-width="1.2"/>
  <path d="M10 70 V80 M55 70 V80 M105 70 V80 M155 70 V80 M200 70 V80" stroke="var(--interference)" stroke-width="1.2"/>
  <rect x="0" y="80" width="34" height="26" rx="3" fill="var(--interference)" opacity="0.4"/>
  <rect x="40" y="80" width="34" height="26" rx="3" fill="var(--interference)" opacity="0.4"/>
  <rect x="88" y="80" width="34" height="26" rx="3" fill="var(--interference)" opacity="0.4"/>
  <rect x="136" y="80" width="34" height="26" rx="3" fill="var(--interference)" opacity="0.4"/>
  <rect x="184" y="80" width="34" height="26" rx="3" fill="var(--interference)" opacity="0.4"/>
  <text x="110" y="124" class="d-fix" text-anchor="middle">5 doors to open</text>
  <text x="110" y="140" class="d-num" text-anchor="middle">~10,000 tokens</text>

  <text x="280" y="14" class="d-label">ONE DOOR</text>
  <rect x="340" y="24" width="90" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="385" y="43" class="d-node" text-anchor="middle">main</text>
  <path d="M385 54 V70" stroke="var(--signal)" stroke-width="1.4"/>
  <rect x="350" y="70" width="70" height="26" rx="4" fill="var(--signal)" opacity="0.45"/>
  <text x="385" y="88" class="d-fix" text-anchor="middle">entry point</text>
  <path d="M385 96 V110" stroke="var(--line)" stroke-width="1"/>
  <path d="M385 110 H310 M385 110 H460" stroke="var(--line)" stroke-width="1"/>
  <rect x="300" y="118" width="30" height="20" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <rect x="340" y="118" width="30" height="20" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <rect x="380" y="118" width="30" height="20" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <rect x="420" y="118" width="30" height="20" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="385" y="164" class="d-fix" text-anchor="middle">1 door to open</text>
  <text x="385" y="180" class="d-num" text-anchor="middle">~1,000 tokens</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=8D8ewFBJfFM",
        "channel": "Eric Tech",
        "title": "Matt Pocock's Claude Code Skills Beat Superpowers Now",
        "duration": "24:17",
    },
}
