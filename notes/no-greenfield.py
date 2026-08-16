NOTE = {
    "id": "no-greenfield",
    "concept": "There is no such thing as greenfield",
    "one_liner": "The only real difference between a greenfield and a brownfield codebase is that"
                 " one has settled conventions and the other hasn't yet — and with an agent"
                 " filling the repo, that distinction survives about a week.",
    "prerequisites": ["codebase-as-environment"],
    "related": ["docs-drift"],

    "skeleton": [
        "Everything is built for the real world, with real constraints.",
        "Brownfield means the conventions already exist, often only in the code.",
        "Greenfield just means you pick them — once.",
        "A repo goes from fresh to legacy faster than ever now.",
    ],

    "mechanism": [
        "The recurring question is whether a technique works on brownfield or only greenfield."
        " Pocock's answer is that they are basically the same thing, because whatever you are"
        " building is for the real world: external constraints, integration with existing"
        " software, real problems.",

        "The one genuine difference is that in a brownfield codebase you have not yet sorted out"
        " the experience of working in it — the conventions, test suite and standards already"
        " exist, and are often implicit in the code rather than documented anywhere. Greenfield"
        " means you choose all of that at the start.",

        "But choices harden. Once the agent has spat a pile of code into the repo, those decisions"
        " get progressively harder to change, which means the green period is short — a couple of"
        " days, maybe a week. We move from fresh codebase to legacy codebase faster than ever"
        " before, precisely because output volume went up.",

        "So the distinction is not worth planning around. A brownfield codebase can hold a lot of"
        " code and still be easy to navigate if the documentation and folder structure are"
        " designed properly, which is the same work that keeps a new repo workable past its first"
        " week.",
    ],

    "numbers": [
        {"value": "days", "unit": "to a week", "label": "how long a codebase stays meaningfully greenfield"},
    ],

    "analogy": None,

    "practice": [
        "Set conventions on day one and write them down — the implicit ones are what the agent misses.",
        "Design folder structure and docs for navigation, not for completeness.",
        "Stop filtering techniques by greenfield vs brownfield; the difference expires in a week.",
        "Treat the first week of a new repo as the only cheap window for changing your mind.",
    ],

    "diagrams": [
        {
            "title": "How long the green lasts",
            "caption": "The distinction is real for about a week. After that both codebases are"
                       " the same problem: conventions someone has to make legible.",
            "svg": '''<svg viewBox="0 0 460 150" role="img"
  aria-label="A timeline of a codebase from day zero. A short green segment lasting about a week, then a long segment labelled the same as any brownfield codebase.">
  <rect x="0" y="34" width="64" height="34" rx="3" fill="var(--signal)" opacity="0.45"/>
  <rect x="64" y="34" width="396" height="34" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="32" y="24" class="d-num" text-anchor="middle">~1 week</text>
  <text x="262" y="56" class="d-label" text-anchor="middle">conventions set, choices now expensive to change</text>
  <line x1="64" y1="30" x2="64" y2="76" stroke="var(--interference)" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="0" y="94" class="d-label">day 0</text>
  <text x="460" y="94" class="d-label" text-anchor="end">legacy</text>
  <text x="0" y="126" class="d-label">agents fill the repo faster, so the green segment gets shorter, not longer</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/0l7zOp260yc",
        "channel": "Matt Pocock",
        "title": "There is no such thing as greenfield",
        "duration": "1:27",
    },
}
