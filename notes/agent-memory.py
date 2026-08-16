NOTE = {
    "id": "agent-memory",
    "concept": "Kill the auto-memory",
    "one_liner": "Letting an agent save its own memories trades predictability for convenience —"
                 " a stateless agent starts from the same base every time, and anything worth"
                 " keeping belongs in a file you wrote.",
    "prerequisites": ["context-window"],
    "related": ["docs-drift", "dumb-zone"],

    "skeleton": [
        "Turn auto-memory off and delete what the agent saved itself.",
        "It is too eager: a one-off preference leaks into every later conversation.",
        "Stateless means a consistent base, so behaviour is predictable.",
        "Write preferences yourself, in a file you control.",
    ],

    "mechanism": [
        "Pocock's position is blunt: turn auto-memory off completely and delete almost everything"
        " the agent has saved into its own memory banks. In Claude Code that is a setting, and the"
        " memories live in an uppercase MEMORY.md.",

        "The problem is eagerness. A preference you expressed about one specific feature — how"
        " that thing should be built — gets saved, and then influences every conversation you have"
        " afterwards, in contexts where it was never meant to apply.",

        "The gain from switching it off is predictability. A stateless agent remembers nothing"
        " between sessions, so every session starts from the same base and you know how it will"
        " behave. With memory accumulating, the behaviour drifts: each use is slightly different"
        " and slightly less predictable than the last, and none of that drift is visible to you.",

        "The alternative is not to have no preferences — it is to write them down deliberately."
        " Edit your CLAUDE.md, add a doc in the repo. You stay in control of the steering, and the"
        " preference exists because you decided it should, not because the agent inferred it.",
    ],

    "numbers": [],

    "analogy": {
        "text": "You should be in control of the steering.",
        "note": "The same test as any other agent feature: does it make your process repeatable,"
                " or does it quietly change the starting conditions on you?",
    },

    "practice": [
        "Turn auto-memory off in settings and clear what has already accumulated.",
        "Put durable preferences in CLAUDE.md or a repo doc — deliberately, by hand.",
        "Treat a stateless agent as the feature: a consistent base is what makes results comparable.",
        "If behaviour drifts between sessions, look at saved memory before blaming the model.",
    ],

    "diagrams": [
        {
            "title": "Four sessions, with and without saved memory",
            "caption": "Stateless, every session starts from the same base you wrote. With"
                       " auto-memory, the base is different each time and nothing shows you how.",
            "svg": '''<svg viewBox="0 0 520 238" role="img"
  aria-label="Top row: four stateless sessions, each starting from an identical small base. Bottom row: four sessions where saved memory accumulates, so each base is larger and different from the last.">
  <text x="0" y="12" class="d-label">STATELESS &#183; same base every time</text>
  <g>
    <rect x="0" y="24" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
    <rect x="4" y="28" width="30" height="38" rx="3" fill="var(--signal)" opacity="0.45"/>
    <text x="56" y="84" class="d-label" text-anchor="middle">session 1</text>

    <rect x="136" y="24" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
    <rect x="140" y="28" width="30" height="38" rx="3" fill="var(--signal)" opacity="0.45"/>
    <text x="192" y="84" class="d-label" text-anchor="middle">session 2</text>

    <rect x="272" y="24" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
    <rect x="276" y="28" width="30" height="38" rx="3" fill="var(--signal)" opacity="0.45"/>
    <text x="328" y="84" class="d-label" text-anchor="middle">session 3</text>

    <rect x="408" y="24" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
    <rect x="412" y="28" width="30" height="38" rx="3" fill="var(--signal)" opacity="0.45"/>
    <text x="464" y="84" class="d-label" text-anchor="middle">session 4</text>
  </g>
  <text x="0" y="106" class="d-label">the base is what you wrote &#8212; comparable results, predictable behaviour</text>

  <text x="0" y="140" class="d-label">AUTO&#8209;MEMORY &#183; the base drifts</text>
  <g>
    <rect x="0" y="152" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
    <rect x="4" y="156" width="30" height="38" rx="3" fill="var(--interference)" opacity="0.45"/>
    <text x="56" y="214" class="d-label" text-anchor="middle">session 1</text>

    <rect x="136" y="152" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
    <rect x="140" y="156" width="46" height="38" rx="3" fill="var(--interference)" opacity="0.45"/>
    <text x="192" y="214" class="d-label" text-anchor="middle">session 2</text>

    <rect x="272" y="152" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
    <rect x="276" y="156" width="66" height="38" rx="3" fill="var(--interference)" opacity="0.45"/>
    <text x="328" y="214" class="d-label" text-anchor="middle">session 3</text>

    <rect x="408" y="152" width="112" height="46" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
    <rect x="412" y="156" width="88" height="38" rx="3" fill="var(--interference)" opacity="0.45"/>
    <text x="464" y="214" class="d-label" text-anchor="middle">session 4</text>
  </g>
  <text x="0" y="234" class="d-label">a preference about one feature, saved once, now shapes every conversation after it</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/A0scuiiGBC4",
        "channel": "Matt Pocock",
        "title": "Kill your MEMORY.md",
        "duration": "1:29",
    },
}
