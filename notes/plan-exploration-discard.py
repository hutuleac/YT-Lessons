NOTE = {
    "id": "plan-exploration-discard",
    "concept": "The plan survives, the exploration doesn't have to",
    "one_liner": "Planning burns context reading files to figure out what to do, but once a plan"
                 " is accepted only the plan itself is worth keeping — the reads that produced it"
                 " can be dropped from the window.",

    "prerequisites": ["context-window"],
    "related": ["cache-loss-recovery"],

    "skeleton": [
        "Plan mode explores the codebase before proposing a plan.",
        "That exploration — every file read — sits in context afterward.",
        "The plan itself is written to its own file, separate from the chat.",
        "One setting drops the exploration from context, keeps the plan.",
    ],

    "mechanism": [
        "Plan mode has to do real work before it can propose anything: reading files, checking"
        " how things connect, ruling out approaches. All of that reasoning and every file it read"
        " lands in the conversation as normal turns, because that's how the model produced the"
        " plan in the first place. Once the plan is accepted, though, none of that discovery"
        " process is still doing anything for you — only the conclusion is.",

        "The two are separable because the plan doesn't actually live in the chat transcript."
        " Accepting a plan writes it to its own file, so the conclusion persists independently of"
        " the conversation that produced it. That's what makes the setting safe: clearing the"
        " context afterward looks like it should throw away the plan along with the exploration,"
        " but the plan was never only in the chat to begin with — the exploration was.",

        "The practical effect is that a feature that costs a large planning conversation to"
        " design doesn't have to cost a large context budget to build. Turn the setting on"
        " (`show clear context on plan accept` set to true in settings.json), and accepting a"
        " plan offers to bin the file reads and side-exploration while carrying the plan forward"
        " into the next turn — you get the answer without paying rent on how it was found.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Set `show clear context on plan accept: true` in settings.json.",
        "Take the offer to clear when a plan is accepted — the plan file survives it.",
        "Don't hand-copy plan-mode findings into notes before accepting; the plan file already keeps them.",
    ],

    "diagrams": [
        {
            "title": "One output, two different lifespans",
            "caption": "The plan is written to its own file. The exploration that produced it"
                       " only ever lived in the chat, so only it needs clearing.",
            "svg": '''<svg viewBox="0 0 480 210" role="img"
  aria-label="Plan mode produces two things: exploration, made of many file reads, which stays only in the chat window; and a plan, written to its own file. After accepting the plan, the exploration can be cleared from context while the plan file persists independently."
       >
  <rect x="175" y="0" width="130" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)" stroke-width="2"/>
  <text x="240" y="22" class="d-node" text-anchor="middle">plan mode</text>

  <path d="M240 34 V 50 M240 50 H 80 M240 50 H 400" stroke="var(--line)" fill="none"/>

  <rect x="10" y="56" width="140" height="52" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="80" y="76" class="d-label" text-anchor="middle">exploration</text>
  <text x="80" y="92" class="d-label" text-anchor="middle">(file reads, reasoning)</text>

  <path d="M80 108 V 128" stroke="var(--interference)" stroke-width="2" fill="none" marker-end="url(#ped-a)"/>
  <text x="90" y="122" class="d-fix">clearable</text>

  <rect x="10" y="134" width="140" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="80" y="156" class="d-label" text-anchor="middle">gone from context</text>

  <rect x="330" y="56" width="140" height="34" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="400" y="78" class="d-node" text-anchor="middle">own file</text>

  <path d="M400 90 V 128" stroke="var(--signal)" stroke-width="2" fill="none" marker-end="url(#ped-b)"/>

  <rect x="330" y="134" width="140" height="34" rx="4" fill="var(--surface-2)" stroke="var(--signal)" stroke-width="2"/>
  <text x="400" y="156" class="d-node" text-anchor="middle">survives clear</text>

  <text x="0" y="196" class="d-fix">only what only lived in the chat needs clearing from the chat</text>

  <defs>
    <marker id="ped-a" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="var(--interference)"/></marker>
    <marker id="ped-b" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="var(--signal)"/></marker>
  </defs>
</svg>''',
        },
    ],

    "source": {
        "url": "https://youtu.be/RDeofKimDxo",
        "channel": "Simon Scrapes",
        "title": "37 Cheat Codes to Level Up In Claude Code in 19 Minutes",
        "duration": "20:06",
    },
}
