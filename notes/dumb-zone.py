from _svg import complete_graph, edge_count

_g5 = complete_graph(5, 78, 86, 52)
_g10 = complete_graph(10, 250, 86, 62)

NOTE = {
    "id": "dumb-zone",
    "concept": "The dumb zone",
    "one_liner": "Every model degrades as its context window fills, so a large window has a usable"
                 " region and a wasteful one — the dumb zone is where you stop getting your"
                 " tokens' worth.",
    "prerequisites": [],
    "related": ["tool-overload", "hallucination-types"],

    # Deck-ready: short lines, no sub-clauses.
    "skeleton": [
        "A 1M-token window is not 1M tokens of usable work.",
        "Add a token and the model tracks every relationship it has to every other token.",
        "Performance sinks gradually — there is no cliff, so nothing warns you.",
        "Rule of thumb: the dumb zone starts around 150k tokens.",
    ],

    # Page prose: the mechanism, in full.
    "mechanism": [
        "Models now ship with a million tokens of context, and it is shocking how little of that"
        " is usable for real work. The cause is attention degradation. When you add a token to"
        " the context window, the model does not simply store it — it has to track that token's"
        " relationship to every other token already there.",

        "That is why the cost grows the way it does. Five tokens produce ten relationships. Ten"
        " thousand tokens produce roughly fifty million. The tokens grow in a line; the"
        " relationships grow as a square. Past some point the model starts hallucinating more,"
        " retrieving less reliably, and writing worse code.",

        "So an agent has a smart zone and a dumb zone. The important detail is that this is not a"
        " cliff — performance sinks slowly, which is precisely why it goes unnoticed. Nothing"
        " errors. The agent just quietly gets worse while you keep paying full price per token.",

        "Where the dumb zone begins is genuinely contested, and it differs per model and probably"
        " per task. Pocock's working rule of thumb is around 150,000 tokens — up from about 100k"
        " six months earlier, and he expects it to keep creeping upward.",
    ],

    "numbers": [
        {"value": "~150k", "unit": "tokens", "label": "working rule of thumb for where the dumb zone starts"},
        {"value": "~100k", "unit": "tokens", "label": "the same rule of thumb six months earlier — it is moving"},
        {"value": "10", "unit": "relationships", "label": "produced by just 5 tokens"},
        {"value": "~50M", "unit": "relationships", "label": "produced by 10,000 tokens"},
    ],

    "analogy": None,

    "practice": [
        "Break work into small chunks and run each in a fresh context window — fewer tokens spent, better results.",
        "Treat arrival in the dumb zone as a signal to clear, compact, or hand off to a new session.",
        "Not every task needs the smart zone. Cheap, mechanical work can run in the dumb zone on purpose.",
        "Redesign workflows so tasks don't need that much context in the first place.",
    ],

    "diagrams": [
        {
            "title": "Tokens grow in a line. Relationships grow as a square.",
            "caption": "5 tokens → 10 relationships. 10 tokens → 45. The model tracks the edges,"
                       " not the dots, and the edges are what run out.",
            "svg": f'''<svg viewBox="0 0 340 190" role="img"
  aria-label="Two node graphs. Five nodes joined by ten lines; ten nodes joined by forty-five lines.">
  <g>{_g5}</g>
  <g>{_g10}</g>
  <text x="78" y="168" class="d-label" text-anchor="middle">5 tokens</text>
  <text x="78" y="182" class="d-num" text-anchor="middle">{edge_count(5)} relationships</text>
  <text x="250" y="168" class="d-label" text-anchor="middle">10 tokens</text>
  <text x="250" y="182" class="d-num" text-anchor="middle">{edge_count(10)} relationships</text>
</svg>''',
        },
        {
            "title": "There is no cliff, which is the problem",
            "caption": "Quality sinks gradually as the window fills. Nothing errors and nothing"
                       " warns you — you simply stop getting your tokens' worth.",
            "svg": '''<svg viewBox="0 0 420 200" role="img"
  aria-label="A curve of agent quality descending as context fills, with a smart zone on the left and a dumb zone on the right divided near 150k tokens.">
  <defs>
    <linearGradient id="zoneFade" x1="0" x2="1">
      <stop offset="0%" stop-color="var(--signal)" stop-opacity="0.20"/>
      <stop offset="55%" stop-color="var(--signal)" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="var(--interference)" stop-opacity="0.20"/>
    </linearGradient>
  </defs>
  <rect x="40" y="18" width="352" height="122" fill="url(#zoneFade)"/>
  <line x1="40" y1="140" x2="392" y2="140" stroke="var(--line)" stroke-width="1"/>
  <line x1="40" y1="18" x2="40" y2="140" stroke="var(--line)" stroke-width="1"/>
  <path d="M40 34 C 150 40, 208 62, 250 92 S 340 132, 392 137"
        fill="none" stroke="var(--signal)" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="250" y1="18" x2="250" y2="140" stroke="var(--interference)"
        stroke-width="1.5" stroke-dasharray="4 4"/>
  <circle cx="250" cy="92" r="4" fill="var(--interference)"/>
  <text x="250" y="12" class="d-num" text-anchor="middle">~150k</text>
  <text x="128" y="160" class="d-label" text-anchor="middle">smart zone</text>
  <text x="322" y="160" class="d-label" text-anchor="middle">dumb zone</text>
  <text x="14" y="82" class="d-label" text-anchor="middle" transform="rotate(-90 14 82)">quality</text>
  <text x="216" y="186" class="d-label" text-anchor="middle">context window filling &#8594;</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/sOd7svdu_1I",
        "channel": "Matt Pocock",
        "title": "What is the dumb zone?",
        "duration": "1:47",
    },
}
