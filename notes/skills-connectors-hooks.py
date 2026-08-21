NOTE = {
    "id": "skills-connectors-hooks",
    "concept": "Skills, connectors, and hooks",
    "one_liner": "Three different jobs get confused under \"make the agent smarter\" — a skill"
                 " makes a prompt repeatable, a connector gives it access to a tool, a hook"
                 " enforces a rule automatically. Naming which one you need keeps the setup from"
                 " turning into one big pile of instructions."
                 ,

    "prerequisites": [],
    "related": ["skill-hell", "repo-as-onboarding-packet"],

    "skeleton": [
        "Typing the same prompt repeatedly? That's a skill — save it, reuse it.",
        "Need GitHub, Linear, Drive, Slack context? That's a connector — access, not instructions.",
        "Need formatting or tests to run automatically? That's a hook — a rule, not a request.",
        "Skills make work repeatable. Connectors give context. Hooks make the workflow safer.",
    ],

    "mechanism": [
        "These three solve different problems and get reached for interchangeably, which is how"
        " setups turn into an unstructured pile of instructions. A skill is a saved, repeatable"
        " way of doing a specific task — a landing-page teardown that checks five-second clarity"
        " and trust signals, a customer-notes pass that pulls out the exact language customers"
        " use. The signal that something should become a skill is noticing you've typed a version"
        " of the same prompt more than once.",

        "A connector is not a prompt at all — it's access. It's what lets the agent read GitHub"
        " issues, pull from Linear, or check a Google Drive doc instead of you copy-pasting"
        " content into the conversation. Where a skill encodes *how* to do something, a connector"
        " just gives the agent somewhere new *to look*.",

        "A hook is neither a prompt nor a source of context — it's an automatic rule that runs at"
        " a fixed point in the workflow regardless of what was asked: run formatting after an"
        " edit, run tests before a PR summary, run checks before anything ships. This is the"
        " enforcement layer [[skill-hell]] warns against skipping: a hook doesn't rely on the"
        " agent remembering to do the safe thing, it makes the safe thing happen structurally.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Before writing a new instruction, ask which of the three it actually is — a repeatable"
        " task (skill), a data source (connector), or a rule that must always fire (hook).",
        "Turn a prompt into a skill the second time you type a version of it, not the fifth.",
        "Put anything that must always happen — formatting, tests before a PR — in a hook, not in"
        " a prompt you might forget to add.",
    ],

    "diagrams": [
        {
            "title": "Three layers, three jobs",
            "caption": "Confusing these is how a setup turns into one long, unstructured"
                       " instruction dump.",
            "svg": '''<svg viewBox="0 0 460 170" role="img"
  aria-label="Three separate layers. Skills: repeatable prompts, e.g. landing page teardown. Connectors: access to tools, e.g. GitHub, Linear, Drive. Hooks: automatic rules, e.g. run tests before a PR.">
  <rect x="0" y="10" width="140" height="60" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="70" y="34" class="d-node" text-anchor="middle">skills</text>
  <text x="70" y="52" class="d-fix" text-anchor="middle">repeatable prompt</text>

  <rect x="160" y="10" width="140" height="60" rx="4" fill="var(--sand)" opacity="0.45"/>
  <text x="230" y="34" class="d-node" text-anchor="middle">connectors</text>
  <text x="230" y="52" class="d-fix" text-anchor="middle">access to a tool</text>

  <rect x="320" y="10" width="140" height="60" rx="4" fill="var(--interference)" opacity="0.35"/>
  <text x="390" y="34" class="d-node" text-anchor="middle">hooks</text>
  <text x="390" y="52" class="d-fix" text-anchor="middle">rule that always fires</text>

  <text x="70" y="96" class="d-label" text-anchor="middle">"tear down this</text>
  <text x="70" y="110" class="d-label" text-anchor="middle">landing page"</text>

  <text x="230" y="96" class="d-label" text-anchor="middle">read GitHub</text>
  <text x="230" y="110" class="d-label" text-anchor="middle">issues</text>

  <text x="390" y="96" class="d-label" text-anchor="middle">run tests</text>
  <text x="390" y="110" class="d-label" text-anchor="middle">before every PR</text>

  <text x="0" y="150" class="d-label">a request you asked for, access you granted, a rule that needs no asking</text>
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
