NOTE = {
    "id": "tool-overload",
    "concept": "Tool definitions are context",
    "one_liner": "Every tool you hand an agent is text pinned to the top of its system prompt, so"
                 " more tools means less room and worse tool choice — the opposite of what adding"
                 " a tool is meant to do.",
    "prerequisites": ["dumb-zone"],
    "related": ["dumb-zone"],

    "skeleton": [
        "The more tools you give an LLM, the worse it performs.",
        "A tool is not code to the model — it is a title, a description and a JSON schema.",
        "All of it sits in the system prompt, above everything else you sent.",
        "Six to eight is fine. Dozens fills the window before you have said anything.",
    ],

    "mechanism": [
        "It helps to know what a tool actually is from the model's side. It is not a function the"
        " model can call into — it is a definition injected into the system prompt: a title, a"
        " description, and a JSON schema for the arguments. Everything else in your system prompt"
        " sits underneath that block.",

        "That works fine for roughly six to eight tools, depending on the model. Attach dozens and"
        " the definitions alone fill a large share of the window before the actual task arrives.",

        "Two things then go wrong at once. The window is smaller, so you reach the dumb zone"
        " sooner. And the model has to pick the right definition out of fifty near-identical"
        " candidates, which is the lost-in-the-middle problem — material buried in a long context"
        " gets attended to least. Pocock notes this bites at as few as twelve tools.",

        "MCP servers make this easy to do by accident: each one you connect can bring a dozen"
        " tools with it, and nothing in the setup flags that you are spending context.",
    ],

    "numbers": [
        {"value": "6–8", "unit": "tools", "label": "roughly where it still works, depending on the model"},
        {"value": "12", "unit": "tools", "label": "enough to start causing selection problems"},
    ],

    "analogy": None,

    "practice": [
        "Keep only the tools a task actually needs in the system prompt.",
        "Disable unused MCP tools — VS Code and Cursor both let you toggle them per tool, not just per server.",
        "Audit after connecting a new MCP server: assume it added more than you think.",
    ],

    "diagrams": [
        {
            "title": "What a tool costs before it does anything",
            "caption": "Definitions are pinned above your actual prompt. Add enough of them and"
                       " the task arrives already deep in the window.",
            "svg": '''<svg viewBox="0 0 420 176" role="img"
  aria-label="Two stacked bars representing a system prompt. With eight tools, definitions take a small top slice and most space is left for work. With forty tools, definitions consume most of the bar.">
  <text x="0" y="14" class="d-label">8 tools</text>
  <rect x="0" y="22" width="420" height="34" rx="3" fill="var(--surface-2)"/>
  <rect x="0" y="22" width="96" height="34" rx="3" fill="var(--interference)" opacity="0.55"/>
  <text x="48" y="43" class="d-num" text-anchor="middle">defs</text>
  <text x="258" y="43" class="d-label" text-anchor="middle">room to actually work</text>

  <text x="0" y="94" class="d-label">40 tools</text>
  <rect x="0" y="102" width="420" height="34" rx="3" fill="var(--surface-2)"/>
  <rect x="0" y="102" width="330" height="34" rx="3" fill="var(--interference)" opacity="0.55"/>
  <text x="165" y="123" class="d-num" text-anchor="middle">tool definitions</text>
  <text x="375" y="123" class="d-label" text-anchor="middle">what's left</text>
  <text x="0" y="164" class="d-label">Same window. The task now starts 78% of the way in.</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/_1KrC_5Xv4s",
        "channel": "Matt Pocock",
        "title": "Stop giving your LLM more tools",
        "duration": "1:12",
    },
}
