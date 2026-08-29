NOTE = {
    "id": "cache-loss-recovery",
    "concept": "Clear, compact, or handoff",
    "one_liner": "When the cache is gone, pick one of three moves: keep nothing and let the"
                 " project carry the context, summarise into the next chat, or write the summary"
                 " to a file on disk.",

    "prerequisites": ["prompt-caching"],
    "related": [],

    "skeleton": [
        "/clear wipes the chat. The project files carry the context forward.",
        "/compact summarises the chat, then starts a new one with that summary.",
        "A handoff writes the summary to a file on disk instead.",
        "Compact and handoff do the same summary step. Only the storage differs.",
        "Do this before you hit the auto-compact limit, not after.",
    ],

    "mechanism": [
        "All three answer one question: the cache is gone, so what do you send next instead of"
        " paying full price to resend everything? Which one fits depends on where the useful"
        " context actually lives — in the conversation, or in the project around it.",

        "/clear wipes the chat outright, and that is often the right move. Working inside a real"
        " codebase means the evidence of what happened sits in the files themselves. A fresh chat"
        " can read those files and pick up the work without needing the old transcript at all.",

        "/compact is for conversations that hold things the project cannot reconstruct on its"
        " own. It writes a summary of the chat, then starts a new chat with that summary already"
        " loaded in. Run it well before the automatic threshold — a chat in the 600,000 to"
        " 800,000 token range is already showing context rot, no matter how strong the model is.",

        "A handoff runs the same summary step, but saves the result to an actual markdown file"
        " on disk instead of the new chat's message list. Point the next chat at that file and"
        " it reads itself in. This suits a document you update across many sessions, not just a"
        " one-time summary for the next chat alone.",

        "What goes in that file matters as much as where it lives. A blogger named Paul (Paul's"
        " Programming Notes) makes the distinction: 'summarize our progress' produces a"
        " human-readable report — issues remaining, what the refactor did — which reads fine"
        " once and is useless the next morning, because it describes what happened instead of"
        " telling the next session what to do. Asking instead for a prompt for the next session,"
        " not a document for a human, changes the shape of the output: it points at exact files"
        " and folders instead of describing them, names what was already tried and didn't work,"
        " and opens with an instruction rather than a summary. Paste that straight into a fresh"
        " session and it reads as a task brief, not a report to file away.",
    ],

    "numbers": [
        {"value": "600k-800k", "unit": "tokens", "label": "range where context rot sets in, regardless of model"},
    ],

    "analogy": None,

    "practice": [
        "Use /clear by default when you work inside a real codebase.",
        "Run /compact before the auto-compact limit, not after.",
        "Use a handoff file when the summary needs to persist and update across sessions.",
        "Write the handoff as a prompt for the next session, not a summary for a human —"
        " point at files, name what didn't work, open with an instruction.",
    ],

    "diagrams": [
        {
            "title": "One summary step, two destinations",
            "caption": "Clear keeps nothing. Compact and handoff both summarise; only where the"
                       " summary lands differs.",
            "svg": '''<svg viewBox="0 0 480 260" role="img"
  aria-label="A long conversation splits three ways. Clear discards it and relies on project files. Compact writes a summary into the new conversation. Handoff writes a summary to a markdown file on disk that a new conversation reads.">
  <rect x="195" y="0" width="90" height="38" rx="5" fill="var(--surface-2)" stroke="var(--signal)" stroke-width="2"/>
  <text x="240" y="24" class="d-node" text-anchor="middle">long chat</text>

  <path d="M225 38 L 80 92" stroke="var(--line)" fill="none"/>
  <path d="M240 38 L 240 92" stroke="var(--line)" fill="none"/>
  <path d="M255 38 L 400 92" stroke="var(--line)" fill="none"/>

  <rect x="10" y="96" width="140" height="46" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="80" y="125" class="d-node" text-anchor="middle">/clear</text>
  <text x="80" y="168" class="d-label" text-anchor="middle">nothing kept</text>
  <text x="80" y="184" class="d-label" text-anchor="middle">files carry it</text>

  <rect x="170" y="96" width="140" height="46" rx="5" fill="var(--interference)" opacity="0.4"/>
  <text x="240" y="125" class="d-node" text-anchor="middle">/compact</text>
  <text x="240" y="168" class="d-label" text-anchor="middle">summary</text>
  <text x="240" y="184" class="d-label" text-anchor="middle">&#8594; new chat</text>

  <rect x="330" y="96" width="140" height="46" rx="5" fill="var(--interference)" opacity="0.4"/>
  <text x="400" y="125" class="d-node" text-anchor="middle">handoff</text>
  <text x="400" y="168" class="d-label" text-anchor="middle">summary</text>
  <text x="400" y="184" class="d-label" text-anchor="middle">&#8594; disk file</text>

  <text x="0" y="232" class="d-fix">clear: relies on the project</text>
  <text x="0" y="250" class="d-fix">compact / handoff: same summary, different home</text>
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
