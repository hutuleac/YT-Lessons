NOTE = {
    "id": "auto-mode",
    "concept": "Auto mode and the permission ladder",
    "one_liner": "Permission modes are a spectrum of how much the agent asks before acting, and"
                 " auto mode — now the default — resolves each action against your written rules"
                 " first, falling through to a separate classifier model only when the rules are"
                 " silent.",
    "prerequisites": ["review-checkpoints"],
    "related": ["harness-bloat", "prompt-injection"],

    "skeleton": [
        "A permission mode sets how much the agent asks before it acts.",
        "Auto mode is the new default: it does almost everything, blocking dangerous actions.",
        "Every action hits your rules first — exact matches never reach the classifier.",
        "Only unmatched actions go to a classifier that asks two questions.",
        "The classifier's decisions are practically invisible without OpenTelemetry.",
    ],

    "mechanism": [
        "A permission mode controls how much the agent checks with you before doing anything, and"
        " Claude Code ships six of them. Four can be switched mid-session with shift-tab: manual"
        " approval, accept-edits (file edits in the current folder go through), plan mode, and"
        " auto. Two can only be set at startup: don't-ask, which executes pre-approved actions and"
        " auto-denies everything else, and bypass-permissions, which skips every check. The video's"
        " own position on bypass is that you should not use it — you need control over the agent."
        " Defaults live in settings JSON, and any mode can also be chosen with a launch flag.",

        "The change worth understanding is that auto is now the default rather than manual"
        " approval. Auto does almost everything on its own and aims to block dangerous actions,"
        " and it decides in two stages.",

        "Stage one is your rules. When the agent wants to act — editing a file, fetching a site,"
        " running a bash command — the rules are consulted first, and an exact match resolves it"
        " without any model being involved. You can allow web fetches outright and hard-deny"
        " `git push`, for example. The configuration has several levers: an `environment` field"
        " describing your infrastructure in plain English, `allow` for exceptions, `soft deny` for"
        " things blocked unless you explicitly ask, `hard deny` for things blocked whatever you"
        " ask, plus `deny` and `ask` rules. The distinction matters: environment and the deny"
        " levels are guidance the classifier weighs, while `deny` and `ask` rules are hard limits"
        " on matching tool calls.",

        "Stage two only runs when the rules are silent. The classifier is itself an AI model —"
        " Sonnet 5, in a separate context — and it answers two questions about the action: could"
        " this cause a security issue, and is this dangerous and irreversible, like deleting the"
        " files in your folder. Two noes and the action proceeds; a single yes denies it.",

        "The gap is observability. Classifier decisions can be tracked through OpenTelemetry, but"
        " that takes a background most users don't have, so in practice you cannot review what was"
        " approved on your behalf. That is the argument for writing rules rather than relying on"
        " the classifier: a rule is a decision you can read afterwards.",
    ],

    "numbers": [
        {"value": "6", "unit": "permission modes", "label": "four switchable with shift-tab, two set only at startup"},
        {"value": "2", "unit": "questions", "label": "the classifier asks: security issue, and dangerous or irreversible"},
    ],

    "analogy": None,

    "practice": [
        "Write rules for the actions you already have an opinion on — they resolve before any model runs.",
        "Use hard deny and ask rules for real limits; environment and soft deny are only guidance.",
        "Describe your infrastructure in the environment field so the classifier judges in context.",
        "Avoid bypass-permissions; auto plus rules gives you the speed without losing the checks.",
        "Assume you cannot audit classifier decisions after the fact, and put the important ones in rules.",
    ],

    "diagrams": [
        {
            "title": "How much the agent asks, mode by mode",
            "caption": "One axis: how often you are interrupted, against how much can happen"
                       " without you. Auto sits where the default used to be manual.",
            "svg": '''<svg viewBox="0 0 520 148" role="img"
  aria-label="A spectrum of six permission modes from manual approval, which asks about everything, through plan, accept edits, auto and don't ask, to bypass permissions, which asks about nothing.">
  <line x1="0" y1="86" x2="520" y2="86" stroke="var(--line)" stroke-width="1.5"/>
  <g>
    <circle cx="30" cy="86" r="6" fill="var(--signal)"/>
    <circle cx="130" cy="86" r="6" fill="var(--signal)"/>
    <circle cx="230" cy="86" r="6" fill="var(--signal)"/>
    <circle cx="330" cy="86" r="8" fill="var(--sand)"/>
    <circle cx="424" cy="86" r="6" fill="var(--interference)"/>
    <circle cx="504" cy="86" r="6" fill="var(--interference)"/>
  </g>
  <text x="30" y="72" class="d-label" text-anchor="middle">manual</text>
  <text x="130" y="72" class="d-label" text-anchor="middle">plan</text>
  <text x="230" y="72" class="d-label" text-anchor="middle">accept edits</text>
  <text x="330" y="66" class="d-num" text-anchor="middle">auto</text>
  <text x="330" y="52" class="d-label" text-anchor="middle">the new default</text>
  <text x="424" y="72" class="d-label" text-anchor="middle">don't ask</text>
  <text x="510" y="58" class="d-label" text-anchor="end">bypass</text>
  <line x1="504" y1="64" x2="504" y2="78" stroke="var(--line)" stroke-width="1"/>
  <text x="0" y="112" class="d-label">asks about everything</text>
  <text x="520" y="112" class="d-label" text-anchor="end">asks about nothing</text>
  <text x="0" y="140" class="d-label">shift-tab switches the middle four; don't-ask and bypass are set at startup</text>
</svg>''',
        },
        {
            "title": "Rules first, classifier only if the rules are silent",
            "caption": "An exact rule match never reaches a model. Everything else is judged by a"
                       " separate Sonnet 5 instance answering two questions, invisibly.",
            "svg": '''<svg viewBox="0 0 520 226" role="img"
  aria-label="Decision flow. An action from the agent is checked against your rules. A match approves or denies it directly. No match sends it to a classifier model which asks whether it is a security issue and whether it is dangerous or irreversible; two noes approve, any yes denies.">
  <rect x="0" y="16" width="132" height="40" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="66" y="34" class="d-node" text-anchor="middle">action</text>
  <text x="66" y="49" class="d-label" text-anchor="middle">edit &#183; fetch &#183; bash</text>

  <path d="M132 36 H176" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="180" y="16" width="150" height="40" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="255" y="34" class="d-node" text-anchor="middle">your rules</text>
  <text x="255" y="49" class="d-label" text-anchor="middle">allow &#183; ask &#183; deny</text>

  <path d="M330 36 H404" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="408" y="16" width="112" height="40" rx="4" fill="none" stroke="var(--signal)"/>
  <text x="464" y="41" class="d-fix" text-anchor="middle">resolved</text>
  <text x="352" y="12" class="d-label">exact match</text>

  <path d="M255 56 V92" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="264" y="78" class="d-label">no match</text>

  <rect x="140" y="92" width="240" height="62" rx="4" fill="var(--surface-2)" stroke="var(--interference)"/>
  <text x="260" y="112" class="d-node" text-anchor="middle">classifier &#183; Sonnet 5</text>
  <text x="260" y="128" class="d-label" text-anchor="middle">1. a security issue?</text>
  <text x="260" y="144" class="d-label" text-anchor="middle">2. dangerous and irreversible?</text>

  <path d="M170 154 V160 H60 V166" stroke="var(--signal)" stroke-width="1.5" fill="none"/>
  <rect x="0" y="170" width="120" height="34" rx="4" fill="none" stroke="var(--signal)"/>
  <text x="60" y="192" class="d-fix" text-anchor="middle">both no &#8594; run</text>

  <path d="M350 154 V160 H460 V166" stroke="var(--interference)" stroke-width="1.5" fill="none"/>
  <rect x="400" y="170" width="120" height="34" rx="4" fill="none" stroke="var(--interference)"/>
  <text x="460" y="192" class="d-node" text-anchor="middle">any yes &#8594; denied</text>

  <text x="0" y="222" class="d-label">the classifier runs in its own context, and its decisions are not practically auditable</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=afe41XkD8Vg",
        "channel": "Software Engineer Meets AI",
        "title": "Claude Code Auto Mode: This Is the New Default",
        "duration": "4:43",
    },
}
