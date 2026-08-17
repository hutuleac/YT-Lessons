NOTE = {
    "id": "advisor-mode",
    "concept": "Advisor mode",
    "one_liner": "A strong model plans and a cheaper model executes, sharing context back to the"
                 " planner only when it hits trouble — so most of the conversation runs at the"
                 " cheap model's rate instead of the strong one's, and each keeps its own cache.",

    "prerequisites": ["prompt-caching"],
    "related": ["agents-vs-workflows"],

    "skeleton": [
        "A smart model plans the task; a cheaper model executes it.",
        "The executor only pulls the planner back in when it runs into trouble.",
        "Planner and executor each keep their own separate prompt cache.",
        "The executor doesn't have to be another Claude model — Codex works the same way.",
    ],

    "mechanism": [
        "The premise is that not every step of a task needs the strongest model looking at it."
        " A capable model produces the plan — the part that genuinely benefits from more"
        " reasoning — and hands execution to a smaller, cheaper model, which does the bulk of the"
        " token-heavy work: reading files, running tools, writing code.",

        "The executor isn't cut off from the planner. When it hits something it can't resolve, it"
        " shares its context back up so the stronger model can weigh in on that specific problem,"
        " rather than the strong model babysitting every step from the start. This is reported to"
        " produce better outcomes at lower cost than running one strong model through the whole"
        " task.",

        "Because it's two separate conversations happening in parallel rather than one long one,"
        " each side builds and holds its own prompt cache independently — the planner's cache"
        " isn't diluted by the executor's tool output, and the executor's cache isn't inflated by"
        " the planner's reasoning.",

        "The executor doesn't have to stay inside the same model family. The same planner/executor"
        " split works delegating out to Codex via a plugin, or in principle to a local model — the"
        " pattern is about which model does the thinking versus the doing, not about staying"
        " inside one ecosystem.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Route the planning step to your strongest model and the execution step to a cheaper one,"
        " rather than running one model through the whole task.",
        "Let the executor escalate to the planner only when it's stuck — don't route every step"
        " through the strong model by default.",
        "Consider a non-Anthropic executor (Codex, a local model) for execution-heavy work where"
        " the planner's reasoning is the only part that needs a top-tier model.",
    ],

    "diagrams": [
        {
            "title": "Planner and executor, escalating only on trouble",
            "caption": "Most turns stay on the cheap executor; the strong planner is called in"
                       " only when execution stalls.",
            "svg": '''<svg viewBox="0 0 460 190" role="img"
  aria-label="A strong planner model produces a plan for a cheaper executor model. The executor handles most turns on its own, escalating back to the planner only when it hits trouble, then resuming execution."
       >
  <rect x="0" y="16" width="130" height="44" rx="4" fill="var(--signal)" opacity="0.45"/>
  <text x="65" y="34" class="d-node" text-anchor="middle">planner</text>
  <text x="65" y="50" class="d-label" text-anchor="middle">strong, expensive</text>

  <path d="M65 60 L 65 100" stroke="var(--line)" fill="none"/>
  <text x="72" y="84" class="d-label">plan</text>

  <rect x="0" y="104" width="130" height="44" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="65" y="122" class="d-node" text-anchor="middle">executor</text>
  <text x="65" y="138" class="d-label" text-anchor="middle">cheap, does the work</text>

  <path d="M130 126 C 220 126, 220 126, 300 126" stroke="var(--line)" fill="none" stroke-dasharray="3 3"/>
  <text x="150" y="118" class="d-label">most turns stay here</text>
  <circle cx="200" cy="126" r="3" fill="var(--muted)"/>
  <circle cx="260" cy="126" r="3" fill="var(--muted)"/>

  <path d="M130 118 C 220 100, 220 30, 132 22" stroke="var(--interference)" fill="none" stroke-width="2"/>
  <text x="150" y="70" class="d-fix">stuck &#8594; escalate to planner</text>

  <text x="0" y="182" class="d-label">each side keeps its own separate prompt cache</text>
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
