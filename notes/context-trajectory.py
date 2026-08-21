NOTE = {
    "id": "context-trajectory",
    "concept": "Context trajectory",
    "one_liner": "Once a session gets steered toward a topic or approach, every later turn in that"
                 " same context window keeps following it, whether you asked for that or not — the"
                 " only real reset is a fresh context window.",

    "prerequisites": ["context-window"],
    "related": ["dumb-zone", "codebase-as-environment"],

    "skeleton": [
        "Steer an agent one way, and it keeps going that way.",
        "An unrelated topic that enters the context contaminates every later turn.",
        "The model can't tell your intent from noise that arrived by accident.",
        "Only a fresh context window resets the trajectory.",
    ],

    "mechanism": [
        "Matt Pocock's term for something both speakers had separately noticed: once you steer an"
        " agent toward an approach — ask it to test through the UI once, say — every later change"
        " in that same session keeps following that direction, no matter what you actually ask"
        " for next. The only way to clear it is to clear the context window itself.",

        "Uncle Bob's example makes the mechanism concrete. You're chatting with a model about the"
        " best way to brew coffee. Someone walks by talking about a soap opera, and that"
        " conversation leaks into the context. From that point on, every coffee reference in the"
        " session somehow relates back to the soap opera — the model can't tell the difference"
        " between what you meant to say and what arrived by accident. It just keeps building on"
        " whatever is already in the window.",

        "The same logic explains why code structure matters to an agent the way it matters to a"
        " human: a well-partitioned module with a disciplined interface keeps unrelated topics out"
        " of an agent's working context the same way a clean session does, so the agent stays on"
        " one trajectory instead of one contaminated by whatever else is nearby. \"It's the same"
        " argument. It's the coffee and soap opera argument.\"",
    ],

    "numbers": [],

    "analogy": {
        "text": "Somebody walks by and they happen to be talking about the latest soap opera... but"
                " then from that point on all the coffee references have to do with the soap"
                " opera.",
        "note": "Trajectory isn't memory going wrong — it's contamination. The model treats"
                " whatever entered the window as equally load-bearing, whether you meant it to be"
                " there or not.",
    },

    "practice": [
        "Clear the context window when you want a genuinely different approach, not just a"
        " different instruction on top of the last one.",
        "Don't let an unrelated aside enter a working session — start a fresh one for it instead.",
        "Design modules so an agent working inside one can't wander into a different topic's"
        " context.",
        "If an agent keeps repeating an approach you didn't ask for, suspect trajectory before you"
        " suspect stubbornness.",
    ],

    "diagrams": [
        {
            "title": "One early input, every later turn",
            "caption": "Whatever enters the context first keeps steering everything after it —"
                       " on purpose or not. A fresh window is the only real reset.",
            "svg": '''<svg viewBox="0 0 460 230" role="img"
  aria-label="A session timeline where an early input (either an intended instruction or an unrelated aside) colors every later turn in the same context window, until a fresh window starts a new, uncolored trajectory.">
  <text x="0" y="14" class="d-label">SAME CONTEXT WINDOW</text>
  <rect x="0" y="24" width="60" height="30" rx="4" fill="var(--interference)" opacity="0.55"/>
  <text x="30" y="43" class="d-label" text-anchor="middle">input</text>
  <line x1="60" y1="39" x2="80" y2="39" stroke="var(--muted)" stroke-width="1.5"/>
  <rect x="80" y="24" width="90" height="30" rx="4" fill="var(--interference)" opacity="0.3"/>
  <text x="125" y="43" class="d-label" text-anchor="middle">turn 2</text>
  <line x1="170" y1="39" x2="190" y2="39" stroke="var(--muted)" stroke-width="1.5"/>
  <rect x="190" y="24" width="90" height="30" rx="4" fill="var(--interference)" opacity="0.3"/>
  <text x="235" y="43" class="d-label" text-anchor="middle">turn 3</text>
  <line x1="280" y1="39" x2="300" y2="39" stroke="var(--muted)" stroke-width="1.5"/>
  <rect x="300" y="24" width="90" height="30" rx="4" fill="var(--interference)" opacity="0.3"/>
  <text x="345" y="43" class="d-label" text-anchor="middle">turn 4</text>
  <text x="0" y="78" class="d-fix">every later turn keeps the trajectory</text>
  <text x="0" y="96" class="d-fix">the first input set, wanted or not</text>

  <line x1="0" y1="112" x2="460" y2="112" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>
  <text x="0" y="136" class="d-label">FRESH CONTEXT WINDOW</text>
  <rect x="0" y="146" width="90" height="30" rx="4" fill="var(--signal)" opacity="0.18" stroke="var(--signal)"/>
  <text x="45" y="165" class="d-label" text-anchor="middle">turn 1</text>
  <text x="0" y="200" class="d-fix">clearing the window is the only way to</text>
  <text x="0" y="218" class="d-fix">drop the old trajectory</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
