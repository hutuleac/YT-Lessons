NOTE = {
    "id": "review-checkpoints",
    "concept": "Shift the checkpoint left or right",
    "one_liner": "Automating agent work is really the question of where the human checks it, and"
                 " the answer is set by diff size: big work is reviewed before it starts, small"
                 " work after it lands.",
    "prerequisites": [],
    "related": ["strategic-load", "effort-levels"],

    "skeleton": [
        "Plan, ship, review — the checkpoints are the human parts.",
        "Handing all three to AI at once is the wrong move.",
        "Big work: shift the checkpoint left, align before it starts.",
        "Small work: shift it right, review the diff at the end.",
    ],

    "mechanism": [
        "A pre-AI process has three human checkpoints: you plan the work, you ship the work, you"
        " review the work. The common ambition is to hand all three to the agent at once, and"
        " Pocock's argument is that this is the wrong unit of decision. The real question is where"
        " the human check belongs, not whether to have one.",

        "For very large pieces of work you want to be involved at the planning stage — aligning"
        " with the agent before it writes anything. That is what his own skills are for. You"
        " probably also want a human review at the end, before production.",

        "But the checkpoint can move. A refactor or an internal documentation rename might only"
        " need the early alignment: agree the plan, then let the agent ship it through. And a very"
        " small change — a button colour, a title, a two-line bug fix — might need no alignment at"
        " all: one prompt, let it run, review the diff before it goes live.",

        "The reason is regeneration cost. The smaller the diff, the easier it is to throw the code"
        " away and generate it again, and the easier it is to hold the whole thing in context. On"
        " massive work, fixing a wrong direction late is expensive, so the check has to happen"
        " before the work exists. Big work shifts the review left; small work shifts it right.",
    ],

    "numbers": [],

    "analogy": {
        "text": "For big work you shift the review left. For small work you shift the review"
                " right.",
        "note": "It replaces a yes-or-no question about trusting the agent with a placement"
                " question you can answer from the size of the diff before you start.",
    },

    "practice": [
        "Decide where the checkpoint goes before you start, using the expected size of the diff.",
        "Big or irreversible work: align on the plan first, because late fixes are the expensive ones.",
        "Small, low-blast-radius work: skip the alignment, review the diff before it goes live.",
        "If a change is cheap to regenerate from scratch, that is the signal to review it late.",
    ],

    "diagrams": [
        {
            "title": "The same pipeline, two placements",
            "caption": "One checkpoint, moved. Left for work that is expensive to redirect later,"
                       " right for work that is cheap to throw away and regenerate.",
            "svg": '''<svg viewBox="0 0 460 216" role="img"
  aria-label="Two pipelines of plan, ship and review. For big work the human checkpoint sits at the planning stage on the left. For small work the checkpoint sits at review on the right.">
  <text x="0" y="12" class="d-label">BIG WORK &#183; check before it exists</text>
  <rect x="0" y="24" width="130" height="38" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="65" y="48" class="d-node" text-anchor="middle">plan</text>
  <text x="136" y="48" class="d-label">&#8594;</text>
  <rect x="158" y="24" width="130" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="223" y="48" class="d-label" text-anchor="middle">agent ships</text>
  <text x="294" y="48" class="d-label">&#8594;</text>
  <rect x="316" y="24" width="144" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="388" y="48" class="d-label" text-anchor="middle">review</text>
  <circle cx="65" cy="76" r="7" fill="var(--interference)"/>
  <text x="80" y="81" class="d-label">human checkpoint &#8212; redirecting later is the expensive part</text>

  <text x="0" y="132" class="d-label">SMALL WORK &#183; check the diff at the end</text>
  <rect x="0" y="144" width="130" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="65" y="168" class="d-label" text-anchor="middle">one prompt</text>
  <text x="136" y="168" class="d-label">&#8594;</text>
  <rect x="158" y="144" width="130" height="38" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="223" y="168" class="d-label" text-anchor="middle">agent ships</text>
  <text x="294" y="168" class="d-label">&#8594;</text>
  <rect x="316" y="144" width="144" height="38" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="388" y="168" class="d-node" text-anchor="middle">review</text>
  <circle cx="388" cy="196" r="7" fill="var(--interference)"/>
  <text x="0" y="212" class="d-label">small diff &#8594; cheap to regenerate &#8594; the check can wait</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/Yn8h5Ip-L9c",
        "channel": "Matt Pocock",
        "title": "Do you even need human review?",
        "duration": "1:59",
    },
}
