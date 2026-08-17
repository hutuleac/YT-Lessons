NOTE = {
    "id": "cache-loss-recovery",
    "concept": "Clear, compact, or handoff",
    "one_liner": "When a long conversation's cache is gone or about to be, the choice isn't"
                 " whether to lose the history — it's whether nothing carries forward (/clear),"
                 " a summary rides in the message history (/compact), or a summary lives as a"
                 " file on disk (a handoff document).",

    "prerequisites": ["prompt-caching"],
    "related": [],

    "skeleton": [
        "/clear wipes the conversation; the codebase itself carries the context forward.",
        "/compact summarises the conversation, then starts fresh with that summary injected.",
        "A handoff writes the summary to a markdown file on disk instead of into the message.",
        "The difference between compact and handoff is only where the summary lives.",
        "None of these beat staying under a few hundred thousand tokens in the first place.",
    ],

    "mechanism": [
        "All three exist to answer one question: the cache is stale or about to be, so what do"
        " you actually do next, instead of just sending the next message at full price? Which one"
        " fits depends on whether the context worth keeping lives in the conversation or in the"
        " project around it.",

        "/clear is the nuclear option, and it's often the right one — it wipes the conversation"
        " outright. If you're working inside a codebase or project with real files, that's usually"
        " fine: the evidence of what happened is sitting in the project itself, so a fresh"
        " conversation can pick the pieces back up without needing the old transcript at all.",

        "/compact is for when the conversation held things the project can't reconstruct on its"
        " own. It generates a summary of what was discussed, then effectively does a /clear and"
        " starts the new conversation with that summary already injected into the message"
        " history — worth doing proactively well before the auto-compact threshold, since"
        " conversations in the 600-800k token range are already suffering context rot regardless"
        " of how strong the model is.",

        "A custom handoff does the same summarisation but changes where the result lives: instead"
        " of sitting in the new conversation's message history, it's written out as an actual"
        " markdown file on disk. The next conversation is then pointed at that file rather than"
        " carrying the summary inline — useful when you want a living document that keeps getting"
        " updated across many sessions, not just a one-time injection.",
    ],

    "numbers": [
        {"value": "600-800k", "unit": "tokens", "label": "range where context rot sets in regardless of model strength"},
    ],

    "analogy": None,

    "practice": [
        "Default to /clear when working in a real codebase — let the project carry the context.",
        "Use /compact before you'd naturally hit auto-compact, not after, to avoid the context-rot"
        " range.",
        "Reach for a handoff file specifically when you want a document that persists and updates"
        " across many sessions, not just the next one.",
    ],

    "diagrams": [
        {
            "title": "Same summarising step, different destination",
            "caption": "Clear keeps nothing; compact and handoff both summarise — only where the"
                       " summary ends up differs.",
            "svg": '''<svg viewBox="0 0 480 200" role="img"
  aria-label="A long conversation branches into three outcomes: clear discards it entirely and relies on the project files; compact summarises it into the new conversation's message history; handoff summarises it into a markdown file on disk that a new conversation reads.">
  <rect x="0" y="80" width="110" height="40" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="55" y="104" class="d-node" text-anchor="middle">long convo</text>

  <path d="M110 90 L 200 40" stroke="var(--line)" fill="none"/>
  <path d="M110 100 L 200 100" stroke="var(--line)" fill="none"/>
  <path d="M110 110 L 200 160" stroke="var(--line)" fill="none"/>

  <rect x="204" y="18" width="90" height="44" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="249" y="36" class="d-node" text-anchor="middle">/clear</text>
  <text x="249" y="52" class="d-label" text-anchor="middle">nothing kept</text>

  <rect x="204" y="78" width="90" height="44" rx="4" fill="var(--interference)" opacity="0.45"/>
  <text x="249" y="96" class="d-node" text-anchor="middle">/compact</text>
  <text x="249" y="112" class="d-label" text-anchor="middle">summary &#8594; new chat</text>

  <rect x="204" y="138" width="90" height="44" rx="4" fill="var(--interference)" opacity="0.45"/>
  <text x="249" y="156" class="d-node" text-anchor="middle">handoff</text>
  <text x="249" y="172" class="d-label" text-anchor="middle">summary &#8594; disk file</text>

  <text x="310" y="36" class="d-label">project files fill the gap</text>
  <text x="310" y="105" class="d-label">lives in message history</text>
  <text x="310" y="165" class="d-label">lives as a .md, reusable</text>
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
