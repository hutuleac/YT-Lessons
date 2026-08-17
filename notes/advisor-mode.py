NOTE = {
    "id": "advisor-mode",
    "concept": "Advisor mode",
    "one_liner": "A strong model plans and a cheap model executes, calling the planner back only"
                 " when it gets stuck, so most turns run at the cheap model's price.",

    "prerequisites": ["prompt-caching"],
    "related": ["agents-vs-workflows"],

    "skeleton": [
        "A strong model plans the task.",
        "A cheap model executes the plan, turn by turn.",
        "The executor calls the planner back only when it gets stuck.",
        "Planner and executor each keep their own separate cache.",
        "The executor can be a different model family, not just a cheaper Claude.",
    ],

    "mechanism": [
        "Not every step of a task needs the strongest model watching it. A capable model writes"
        " the plan, since planning is the part that benefits most from extra reasoning. A"
        " smaller, cheaper model then executes: reading files, running tools, writing code —"
        " the bulk of the token-heavy work.",

        "The executor is not cut off from the planner. When it hits something it cannot resolve,"
        " it shares that specific problem back up, and the stronger model weighs in on just that"
        " step instead of supervising every step from the start. This is reported to produce"
        " better outcomes at lower cost than running one strong model through the whole task.",

        "Because planner and executor are two separate conversations running in parallel, each"
        " one builds and holds its own prompt cache. The planner's cache is not diluted by the"
        " executor's tool output, and the executor's cache is not inflated by the planner's"
        " reasoning.",

        "The executor does not have to stay inside one model family. The same split works with"
        " Codex as the executor behind a plugin, or in principle with a local model — the"
        " pattern is about who plans versus who executes, not about staying in one ecosystem.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Send the planning step to your strongest model.",
        "Send the execution step to a cheaper model.",
        "Let the executor escalate only when it is stuck.",
        "Try a non-Anthropic executor, such as Codex, for execution-heavy work.",
    ],

    "diagrams": [
        {
            "title": "Escalate only on trouble",
            "caption": "Most turns stay on the cheap executor. The strong planner is called in"
                       " only when execution stalls.",
            "svg": '''<svg viewBox="0 0 460 210" role="img"
  aria-label="A strong planner model produces a plan for a cheaper executor model. The executor handles most turns on its own, escalating back to the planner only when it hits trouble, then resuming execution."
       >
  <rect x="0" y="16" width="140" height="44" rx="4" fill="var(--signal)" opacity="0.45"/>
  <text x="70" y="36" class="d-node" text-anchor="middle">planner</text>
  <text x="70" y="52" class="d-label" text-anchor="middle">strong, high cost</text>

  <path d="M70 60 L 70 104" stroke="var(--line)" fill="none"/>
  <text x="78" y="86" class="d-label">plan</text>

  <rect x="0" y="108" width="140" height="44" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="70" y="128" class="d-node" text-anchor="middle">executor</text>
  <text x="70" y="144" class="d-label" text-anchor="middle">cheap, does the work</text>

  <text x="160" y="122" class="d-label">most turns stay here</text>
  <path d="M160 132 L 300 132" stroke="var(--line)" stroke-dasharray="3 3" fill="none"/>
  <circle cx="210" cy="132" r="3" fill="var(--muted)"/>
  <circle cx="260" cy="132" r="3" fill="var(--muted)"/>

  <path d="M140 116 C 220 60, 260 40, 60 22" stroke="var(--interference)" fill="none" stroke-width="2"/>
  <text x="160" y="52" class="d-fix">stuck &#8594; escalate</text>

  <text x="0" y="196" class="d-label">each side keeps its own cache</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=V0XbuApxlhg",
        "channel": "Chase AI",
        "title": "You're Paying Anthropic 20x MORE Than You Need To",
        "duration": "18:59",
    },
}
