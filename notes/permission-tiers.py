NOTE = {
    "id": "permission-tiers",
    "concept": "Three tiers of permission",
    "one_liner": "Split what an agent can do into safe, ask-first, and human-owned — the same"
                 " delegation model you'd use for a new hire, so autonomy grows with trust instead"
                 " of being all-or-nothing."
                 ,

    "prerequisites": [],
    "related": ["scheduled-routines", "review-checkpoints"],

    "skeleton": [
        "Safe: read files, run local tests, edit a small branch, draft a PR. No approval needed.",
        "Ask first: install dependencies, touch migrations, auth, or payment logic, delete files.",
        "Human-owned: production deploys, customer data, billing, security-sensitive changes.",
        "Start conservative. Loosen the tier as the repo brain and review checklist get stronger.",
    ],

    "mechanism": [
        "Treating agent permissions as a single on/off switch forces a bad trade: either the agent"
        " can do nothing without approval, which defeats the point, or it can do everything, which"
        " is how a small task turns into an unreviewed production incident. Splitting actions into"
        " three tiers by blast radius avoids both — most work stays fully autonomous, risky work"
        " pauses for a yes, and a defined set of decisions never leaves the human's hands"
        " regardless of how much trust has been built up.",

        "The tiers track consequence, not difficulty: reading code and running local tests are"
        " safe because they're reversible and contained to the agent's own branch. Installing a"
        " dependency or touching a migration is ask-first because it's the kind of change whose"
        " damage doesn't stay local. Production deploys, customer data, and billing stay"
        " human-owned permanently — not because the agent can't do them, but because some"
        " decisions are supposed to require a person even after everything else has been"
        " automated.",

        "This is a strategy that scales rather than a fixed setting: as [[repo-as-onboarding-"
        "packet]]'s review checklist and task scoping get stronger, more work can move from"
        " ask-first toward safe. The alternative — starting at full autonomy — just moves the"
        " same review burden from before the change to after the incident.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Write down which actions fall in each tier before turning an agent loose on a repo — "
        "don't decide it live, mid-task.",
        "Keep production deploys, customer data, and billing decisions human-owned no matter how"
        " much autonomy the agent has earned elsewhere.",
        "Start conservative and use plan mode plus manual review for anything new, then loosen as"
        " trust and tooling (routines, review checklist) mature.",
    ],

    "diagrams": [
        {
            "title": "Autonomy by blast radius",
            "caption": "The tier tracks how far a mistake reaches, not how hard the task is.",
            "svg": '''<svg viewBox="0 0 460 190" role="img"
  aria-label="Three concentric tiers of agent permission. Innermost, safe: read files, run local tests, edit a small branch, no approval needed. Middle, ask first: install dependencies, touch migrations, auth, or payments. Outer, human-owned: production deploys, customer data, billing.">
  <circle cx="230" cy="95" r="86" fill="var(--interference)" opacity="0.18"/>
  <circle cx="230" cy="95" r="58" fill="var(--sand)" opacity="0.35"/>
  <circle cx="230" cy="95" r="30" fill="var(--signal)" opacity="0.4"/>

  <text x="230" y="90" class="d-node" text-anchor="middle">safe</text>
  <text x="230" y="104" class="d-fix" text-anchor="middle">read, test, branch</text>

  <text x="230" y="46" class="d-label" text-anchor="middle">ask first</text>
  <text x="230" y="14" class="d-label" text-anchor="middle">human-owned</text>

  <text x="0" y="180" class="d-label">deploys, customer data, billing &#8212; stay human no matter what</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=SkY-tR9kf-k",
        "channel": "Greg Isenberg",
        "title": "Claude Code New Features, Explained",
        "duration": "48:10",
    },
}
