NOTE = {
    "id": "grooming-skill",
    "concept": "The grooming skill",
    "one_liner": "A skill that turns a vague request into a shared understanding by interviewing"
                 " you one branch, one question at a time — never acting until you confirm.",

    "prerequisites": [],
    "related": ["skill-hell", "spec-driven-trap"],

    "skeleton": [
        "Relentless: keep asking until you and the agent share understanding.",
        "One branch: finish the checkout page before moving to the about page.",
        "One question: wait for your answer before asking the next.",
        "Recommend: never a blank question — always options and a pick.",
        "Do not act: no building until you confirm.",
    ],

    "mechanism": [
        "The problem it answers is that an agent given everything at once — colours, copy,"
        " functionality — has no way to build any of it with real accuracy, and asking the user to"
        " dump all of that context up front does not work because the user does not know what"
        " context the agent needs. The grooming skill inverts the direction: the agent interviews"
        " the user instead of the user briefing the agent.",

        "The five rules are what make the interview usable rather than exhausting. One branch at a"
        " time keeps the questions from jumping between the checkout page and the about page"
        " mid-thought — a decision tree is walked one path to its end before the next path opens."
        " One question at a time means the agent waits for an answer instead of stacking three"
        " questions the user has to hold in their head. Recommend one means every question ships"
        " with a default the user can just accept, so the interview does not stall on questions"
        " the user has no opinion about. Do not act is the backstop: nothing gets built until the"
        " user has confirmed, so a misunderstanding costs a correction, not a rewrite.",

        "The result is closer to a decision machine than a chat: the model supplies options, the"
        " user picks, and each pick stacks onto the last until the tree runs out of branches. That"
        " is also why it pairs with a spec — see [[spec-driven-trap]] and the sibling note on"
        " writing the result down before the conversation is lost.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Let the agent ask before it builds — resist the urge to front-load every requirement.",
        "Answer one branch fully before letting the conversation jump to the next.",
        "Take the recommended default when you have no strong opinion; it keeps the interview moving.",
        "Don't let the agent act on an answer you haven't actually confirmed.",
    ],

    "diagrams": [
        {
            "title": "One branch, fully cleared, before the next",
            "caption": "The interview walks one path of the decision tree to its end — checkout,"
                       " then about page — instead of hopping between branches mid-question.",
            "svg": '''<svg viewBox="0 0 480 210" role="img"
  aria-label="A decision tree with two branches, checkout page and about page. The checkout branch is fully walked through three questions before the about page branch begins, shown greyed out and untouched until the checkout branch completes.">
  <text x="0" y="14" class="d-label">REQUEST</text>
  <rect x="0" y="24" width="120" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="60" y="46" class="d-node" text-anchor="middle">build the app</text>

  <path d="M60 58 V78 M60 78 H150 M60 78 H0" stroke="var(--line)" stroke-width="1.4"/>

  <rect x="90" y="86" width="120" height="30" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="150" y="105" class="d-node" text-anchor="middle">checkout page</text>

  <rect x="0" y="86" width="70" height="30" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="35" y="105" class="d-label" text-anchor="middle">about</text>

  <rect x="90" y="130" width="120" height="26" rx="4" fill="var(--signal)" opacity="0.3"/>
  <text x="150" y="147" class="d-label" text-anchor="middle">Q1: card or wallet?</text>
  <rect x="90" y="162" width="120" height="26" rx="4" fill="var(--signal)" opacity="0.3"/>
  <text x="150" y="179" class="d-label" text-anchor="middle">Q2: guest checkout?</text>
  <rect x="90" y="194" width="120" height="12" rx="3" fill="var(--signal)" opacity="0.2"/>

  <text x="230" y="147" class="d-fix">answered, one at a time</text>
  <text x="0" y="205" class="d-label">about page waits, untouched, until checkout is fully cleared</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=8D8ewFBJfFM",
        "channel": "Eric Tech",
        "title": "Matt Pocock's Claude Code Skills Beat Superpowers Now",
        "duration": "24:17",
    },
}
