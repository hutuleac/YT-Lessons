NOTE = {
    "id": "codebase-qa-first",
    "concept": "Start with codebase Q&A",
    "one_liner": "Before letting an agent edit anything, use it to ask questions about the"
                 " codebase — it answers by exploring the repo the way an engineer would, and"
                 " asking teaches you where its competence ends.",

    "prerequisites": [],
    "related": ["repo-as-onboarding-packet", "ticket-scoping"],

    "skeleton": [
        "First use of an agent on a repo should be questions, not edits.",
        "It answers by exploring — grep, git log, linked issues — not by text search.",
        "Anthropic's technical onboarding went from 2-3 weeks to 2-3 days this way.",
        "Asking is how you learn what it one-shots and what needs hand-holding.",
        "Nothing is indexed or uploaded, so there is no setup step to wait through.",
    ],

    "mechanism": [
        "Boris, who built Claude Code, gives this as his first recommendation in his"
        " Claude Code talk at Anthropic's Code w/ Claude (the video is a re-upload of that"
        " conference session). A free-form agent opens on an empty prompt bar and it is not"
        " obvious what to type. Questions are the answer, because a question is the one request"
        " where a wrong answer costs nothing — no diff to review, no state changed.",

        "The reason the answers are worth having is that the agent does not resolve a question"
        " by searching for the string. Asked how a class is used, it goes looking for real"
        " instantiations. Asked why a function has fifteen arguments, it reads git history, finds"
        " which commits introduced each one, and follows the issues those commits link to. That"
        " is a chain a wiki page cannot give you and Command-F cannot reconstruct. He notes"
        " none of this is prompted for — there is nothing in the system prompt about git; the"
        " model simply knows how to use it when told to.",

        "The organisational payoff is onboarding. At Anthropic, technical hires used to take two"
        " to three weeks to get productive, mostly by taxing other engineers with questions;"
        " with codebase Q&A that dropped to two or three days. Nothing is indexed, no remote"
        " database holds your code, and the code is not used to train models — which also means"
        " there is no indexing wait before the first question. He puts the internal"
        " adoption at roughly 80% of technical staff using it daily, so this is how the whole"
        " company reads its own code, not an onboarding-only trick.",

        "The second payoff is calibration. Asking questions teaches a new user where the"
        " boundary sits: what gets one-shotted, what takes two or three attempts, what needs"
        " an interactive session with you steering. You cannot prompt well for editing until you"
        " have a feel for that boundary, and questions are the cheap way to acquire it.",
    ],

    "numbers": [
        {"value": "2-3", "unit": "weeks", "label": "technical onboarding at Anthropic, before"},
        {"value": "2-3", "unit": "days", "label": "technical onboarding at Anthropic, after"},
        {"value": "~80", "unit": "%", "label": "technical staff at Anthropic using Claude Code"
                                               " daily, as of the talk"},
        {"value": "15", "unit": "arguments", "label": "his example of a function whose history"
                                                      " only git log can explain"},
    ],

    "analogy": None,

    "practice": [
        "Make the first session on any unfamiliar repo a question session — edit nothing.",
        "Ask about usage, not just definitions: how is this instantiated, where is this called.",
        "Ask about history — why an argument exists, who added it, what issue it links to.",
        "When onboarding a teammate, have them start here rather than with tools or edits.",
        "Track which questions get one-shotted; that boundary is what tells you how to prompt.",
    ],

    "diagrams": [
        {
            "title": "How a question gets answered",
            "caption": "A search returns matches. The agent returns the chain that explains"
                       " them.",
            "svg": '''<svg viewBox="0 0 500 210" role="img"
  aria-label="A question, why does this function have fifteen arguments, sent two ways. Text search returns only the line where the function is defined. The agent instead runs grep for call sites, reads git blame and log for the commits that added each argument, and fetches the issues those commits link to, then returns a synthesized history.">
  <text x="0" y="14" class="d-label">&#8220;why does this function have 15 arguments?&#8221;</text>

  <text x="0" y="46" class="d-label">TEXT SEARCH</text>
  <rect x="0" y="56" width="170" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="10" y="77" class="d-node">1 match: the def line</text>
  <text x="0" y="108" class="d-fix">tells you what, never why</text>

  <text x="230" y="46" class="d-label">AGENT</text>
  <rect x="230" y="56" width="120" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="240" y="73" class="d-node">grep call sites</text>
  <rect x="230" y="88" width="120" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="240" y="105" class="d-node">git log / blame</text>
  <rect x="230" y="120" width="120" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="240" y="137" class="d-node">linked issues</text>
  <path d="M350 69 H375 V133 H350" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <path d="M350 101 H375" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <path d="M375 101 H395" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="395" y="84" width="105" height="34" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="405" y="105" class="d-node">the history</text>

  <text x="230" y="170" class="d-fix">nothing prompts it to use git &#8212; it knows</text>
  <text x="0" y="196" class="d-label">Onboarding at Anthropic: 2&#8211;3 weeks &#8594; 2&#8211;3 days.</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=pQ6G9TQfGIA",
        "channel": "frugle",
        "title": "Anthropic's FREE 24-Min Prompt Engineering Workshop (Beats Every $500 Course)",
        "duration": "27:55",
    },
}
