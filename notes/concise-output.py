NOTE = {
    "id": "concise-output",
    "concept": "Sacrifice grammar for concision",
    "one_liner": "One line in your global config — report to me extremely concisely, sacrificing"
                 " grammar — turns an agent's essays into headers and fragments you can scan,"
                 " without changing what the agent understood.",
    "prerequisites": [],
    "related": ["context-window", "strategic-load"],

    "skeleton": [
        "Agents default to paragraphs. You have to read all of them.",
        "Ask for extreme concision, explicitly sacrificing grammar.",
        "You get headers, fragments and short lists instead of prose.",
        "Put it in the global config so it applies everywhere.",
    ],

    "mechanism": [
        "The instruction is one sentence: when reporting information to me, be extremely concise"
        " and sacrifice grammar for the sake of concision. Adding it to a prompt reshapes the"
        " reply; adding it to the global CLAUDE.md applies it to every session.",

        "The difference Pocock demonstrates on a debugging session is structural rather than"
        " cosmetic. Without it: paragraphs — scannable, but still prose. With it: \"ESM/CJS"
        " mismatch. Let me check the build output and config,\" then a header, \"root cause"
        " found,\" then the specific incompatibility. The biggest gap is in the final summary,"
        " which goes from a mini-article to a couple of headings and a short list.",

        "The key point is that this changes the report, not the work. Under the hood the model has"
        " the same understanding of what it did; you are choosing the format of the first thing"
        " you receive. Follow-up questions still get you the long version whenever you want it.",

        "Which is why the win compounds: shorter reports mean less to read at every checkpoint,"
        " and fewer tokens spent re-stating work you already agreed to.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Add the concision line to your global config, not to individual prompts.",
        "Ask for the format you want to receive — headers and fragments are a legitimate request.",
        "Treat the short summary as the default and ask follow-ups when you need depth.",
        "Judge the change on how fast you can scan a report, not on how polished it reads.",
    ],

    "diagrams": [
        {
            "title": "Same debugging session, two report formats",
            "caption": "The model's understanding is identical either side. What changes is how"
                       " long it takes you to find the root cause in the reply.",
            "svg": '''<svg viewBox="0 0 460 196" role="img"
  aria-label="Two report blocks. The default report is three long paragraph bars. The concise report is a short header, two short fragments and a two-item list.">
  <text x="0" y="12" class="d-label">DEFAULT</text>
  <rect x="0" y="22" width="212" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <rect x="0" y="38" width="212" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <rect x="0" y="54" width="180" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <rect x="0" y="76" width="212" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <rect x="0" y="92" width="196" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <rect x="0" y="108" width="212" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <rect x="0" y="124" width="150" height="10" rx="2" fill="var(--muted)" opacity="0.45"/>
  <text x="0" y="158" class="d-label">root cause is in there</text>

  <text x="248" y="12" class="d-label">CONCISE</text>
  <text x="248" y="36" class="d-node">ESM/CJS mismatch</text>
  <rect x="248" y="46" width="140" height="8" rx="2" fill="var(--signal)" opacity="0.5"/>
  <text x="248" y="78" class="d-fix">root cause found</text>
  <rect x="248" y="88" width="120" height="8" rx="2" fill="var(--signal)" opacity="0.5"/>
  <rect x="248" y="102" width="164" height="8" rx="2" fill="var(--signal)" opacity="0.5"/>
  <rect x="248" y="120" width="96" height="8" rx="2" fill="var(--signal)" opacity="0.5"/>
  <text x="248" y="158" class="d-label">headers first, detail on request</text>
  <text x="0" y="188" class="d-label">one line in the global config &#8212; same understanding, different report</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/I12Mf8KBT1I",
        "channel": "Matt Pocock",
        "title": "Make Claude Code give you answers, not essays",
        "duration": "1:30",
    },
}
