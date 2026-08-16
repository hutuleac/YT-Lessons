NOTE = {
    "id": "harness-bloat",
    "concept": "Harness bloat",
    "one_liner": "The tool you code in ships thousands of tokens of features you never use, all"
                 " of it in the system prompt on every request — and most of it can be switched"
                 " off in settings.",
    "prerequisites": ["tool-overload"],
    "related": ["dumb-zone", "context-window"],

    "skeleton": [
        "Your harness ships a system prompt full of features you don't use.",
        "Every unused tool definition is sent again on every single request.",
        "Settings can remove them — the definitions leave the prompt entirely.",
        "Pocock cut his from 25K tokens to about 8K.",
    ],

    "mechanism": [
        "Most harnesses, Claude Code especially, ship with a large system prompt covering every"
        " feature they offer. Pocock's audit found whole blocks for things he never touched —"
        " workflows, design sync, monitor — on the order of eight to ten thousand tokens per"
        " request.",

        "The cost is recurring, not one-off: it is in the system prompt, so it is re-sent on every"
        " request in every session. It is also the most expensive place to spend tokens, because"
        " the system prompt sits above your actual task.",

        "The fix is configuration rather than cleverness. Disabling a feature in global settings"
        " removes its tool definitions from the system prompt outright. He disabled plan-mode"
        " control, the ask-user-question tool, cron scheduling, bundled skills, dynamic workflows,"
        " remote control, connectors and artifacts — taking the shipped system tools from roughly"
        " 25K tokens down to around 8K. He used a proxy to see what was actually going over the"
        " wire, which is how you find yours rather than guessing.",

        "The reason this is worth doing is the same one behind every fix in this lesson: the less"
        " you send, the better the output, because there is less material distracting the agent.",
    ],

    "numbers": [
        {"value": "25K", "unit": "tokens", "label": "shipped system tools before the audit"},
        {"value": "~8K", "unit": "tokens", "label": "after disabling the unused features"},
        {"value": "8–10K", "unit": "tokens", "label": "in blocks for three features he never used"},
    ],

    "analogy": None,

    "practice": [
        "Run a proxy once to see what your harness actually sends — don't estimate it.",
        "Disable features you never use in global settings; the definitions leave the prompt.",
        "Re-audit after upgrades: new features arrive switched on.",
        "Judge the saving per request, not per session — the system prompt is re-sent every time.",
    ],

    "diagrams": [
        {
            "title": "25K down to 8K, on every request",
            "caption": "The bar is the system prompt before your task starts. Everything shaded is"
                       " shipped features, re-sent on every single call.",
            "svg": '''<svg viewBox="0 0 460 172" role="img"
  aria-label="Two bars. Before: 25 thousand tokens of shipped system tools filling most of the bar. After: about 8 thousand tokens, leaving far more room for the task.">
  <text x="0" y="14" class="d-label">BEFORE</text>
  <rect x="0" y="24" width="460" height="34" rx="3" fill="var(--surface-2)"/>
  <rect x="0" y="24" width="368" height="34" rx="3" fill="var(--interference)" opacity="0.5"/>
  <text x="184" y="45" class="d-num" text-anchor="middle">25K shipped tools</text>
  <text x="414" y="45" class="d-label" text-anchor="middle">your task</text>

  <text x="0" y="94" class="d-label">AFTER</text>
  <rect x="0" y="104" width="460" height="34" rx="3" fill="var(--surface-2)"/>
  <rect x="0" y="104" width="118" height="34" rx="3" fill="var(--signal)" opacity="0.45"/>
  <text x="59" y="125" class="d-num" text-anchor="middle">~8K</text>
  <text x="290" y="125" class="d-label" text-anchor="middle">room to actually work</text>

  <text x="0" y="164" class="d-label">a settings change, not a prompt trick &#8212; and it applies to every request</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/oLx4yCbeklQ",
        "channel": "Matt Pocock",
        "title": "Claude Code's system tools are SO BLOATED",
        "duration": "1:38",
    },
}
