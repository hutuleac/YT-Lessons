NOTE = {
    "id": "code-smell-vocabulary",
    "concept": "Named vocabulary instead of instructions",
    "one_liner": "A code review checklist built from named smells — shotgun surgery, feature"
                 " envy, data clumps — packs a whole diagnostic step into one word the model"
                 " already knows, instead of a paragraph explaining what to look for.",

    "prerequisites": [],
    "related": ["grooming-skill"],

    "skeleton": [
        "The review checklist is 12 words, not 12 paragraphs of instructions.",
        "The words come from Fowler's Refactoring — a book the model has already read.",
        "Shotgun surgery: one change that has to be repeated in many places.",
        "Feature envy: logic living in the wrong file.",
        "Data clumps: the same group of fields passed around separately instead of as one type.",
    ],

    "mechanism": [
        "A skill that spells out every review step in plain instructions grows long, and every"
        " extra word in a skill is something that can distract the model rather than help it. The"
        " fix demonstrated here is to replace instructions with names: instead of writing out what"
        " counts as a review problem, the skill points at twelve terms lifted from Martin Fowler's"
        " Refactoring — shotgun surgery, feature envy, data clumps, and others — and tells the"
        " model to check for them.",

        "This works because those terms already carry their full definition inside a model that"
        " has ingested the book they come from. Shotgun surgery names the case where one logical"
        " change requires edits scattered across many files — miss one and the change is"
        " inconsistent. Feature envy names logic that references another module's data more than"
        " its own, meaning it is filed in the wrong place — logic that belongs to orders.ts but"
        " lives in inventory.ts. Data clumps names a group of fields — say three related IDs —"
        " that keep travelling together as separate arguments across many functions, when they"
        " should be one type. Each term compresses a diagnostic paragraph into a single lookup.",

        "The same move is why this checklist runs in a fresh context window rather than the"
        " session that wrote the code: a reviewer checking its own recent work is reviewing its"
        " own blind spots, so a clean window walking a checklist of named smells catches what a"
        " same-session self-check would miss.",
    ],

    "numbers": [
        {"value": "12", "unit": "words", "label": "the entire review checklist"},
    ],

    "analogy": None,

    "practice": [
        "When writing a review or audit skill, reach for an established vocabulary the model"
        " already knows before writing new instructions from scratch.",
        "Run code review in a fresh context window, not the session that wrote the code.",
        "Learn the term, not just the fix — 'feature envy' catches more than the one instance you"
        " first spotted it in.",
    ],

    "diagrams": [
        {
            "title": "One word instead of one paragraph",
            "caption": "The model already knows what the term means from the book — the skill"
                       " only has to name it.",
            "svg": '''<svg viewBox="0 0 480 150" role="img"
  aria-label="A paragraph of review instructions compresses down to a single named term, shotgun surgery, because the model already knows the term's meaning from having read Fowler's Refactoring.">
  <rect x="0" y="10" width="230" height="80" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="10" y="28" class="d-label">"check whether a single</text>
  <text x="10" y="42" class="d-label">logical change requires</text>
  <text x="10" y="56" class="d-label">edits across many files,</text>
  <text x="10" y="70" class="d-label">and flag it if one is</text>
  <text x="10" y="84" class="d-label">likely to be missed..."</text>

  <path d="M236 50 H278" stroke="var(--signal)" stroke-width="1.6"/>
  <text x="257" y="44" class="d-fix" text-anchor="middle">compresses to</text>

  <rect x="286" y="30" width="194" height="40" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="383" y="55" class="d-node" text-anchor="middle">shotgun surgery</text>

  <text x="0" y="118" class="d-label">the term already means this &#8212; from the book, not the skill</text>
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
