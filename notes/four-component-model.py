NOTE = {
    "id": "four-component-model",
    "concept": "CLAUDE.md, skill, MCP, sub agent",
    "one_liner": "Claude Code has four components with non-overlapping jobs — memory, repeatable"
                 " action, external access, and context-splitting — and most setups burn tokens"
                 " because people reach for whichever one they know instead of the one whose job"
                 " actually matches the problem.",

    "prerequisites": [],
    "related": ["skills-connectors-hooks", "skill-hell", "context-window"],

    "skeleton": [
        "CLAUDE.md is memory — rules and facts Claude should know every conversation.",
        "A skill is a repeatable task — package it once, trigger it on demand.",
        "An MCP is access to another app or live data, not instructions.",
        "A sub agent splits a task too big for one context window into parallel workers.",
        "Jamming everything into CLAUDE.md, or installing skills and MCPs you never trigger, is what burns tokens.",
    ],

    "mechanism": [
        "Each component answers a different question, and the failure mode is picking the one"
        " you already know how to use instead of the one whose job matches the problem. CLAUDE.md"
        " loads into every conversation whether it's relevant or not, so it should hold only what"
        " actually needs to be true every time — durable facts and rules about you or the"
        " project, not task-specific instructions. Stuffing one-off procedures into it means"
        " paying to load them on turns that never need them.",

        "A skill and an MCP look similar from the outside — both are things you 'install' — but"
        " they solve opposite problems. A skill packages a way of doing something you already"
        " know how to describe in words: the instructions live in the skill, and Claude still"
        " does the work itself. An MCP gives Claude reach it doesn't otherwise have — a live"
        " connection into Gmail, a CRM, a video editor — where the point isn't packaged"
        " instructions but the ability to act inside a system it couldn't touch before.",

        "A sub agent solves neither memory nor access — it solves scale. When a task is too big"
        " to fit in one context window, or splits naturally into independent pieces, a sub agent"
        " lets Claude farm the work out to parallel workers and keep the main conversation's"
        " context clean instead of filling it with the intermediate steps of every sub-task.",

        "The video doesn't explain the token-burning mechanism beyond naming it — 'unintentional"
        " bloat' from a bloated CLAUDE.md plus unused MCP servers and skills is asserted, not"
        " walked through. The plausible mechanism, consistent with how CLAUDE.md and skills"
        " actually load, is that CLAUDE.md content loads on every single turn regardless of"
        " relevance, while an installed-but-untriggered skill or MCP server's overhead depends on"
        " how the client surfaces it — worth treating as this video's least-supported claim.",
    ],

    "numbers": [
        {"value": "10", "unit": "MCP servers", "label": "example count the video gives for a bloated, unintentional setup"},
        {"value": "hundreds", "unit": "skills", "label": "example scale of skills installed from GitHub and never used"},
    ],

    "analogy": None,

    "practice": [
        "Before adding anything, name which of the four it is: does Claude need to know this every"
        " time (CLAUDE.md), do it repeatably on demand (skill), reach into another app (MCP), or"
        " offload a task too big for one context window (sub agent)?",
        "Keep CLAUDE.md to what must be true every conversation — move task-specific instructions"
        " into a skill instead.",
        "Uninstall MCP servers and skills you can't currently name a trigger for.",
    ],

    "diagrams": [
        {
            "title": "Four jobs, one question each",
            "caption": "Confusing these is what turns a setup into unintentional bloat.",
            "svg": '''<svg viewBox="0 0 460 260" role="img"
  aria-label="Four components each answer a different question. CLAUDE.md: know every time, memory. Skill: do on demand, repeatable action. MCP: reach another app, external access. Sub agent: too big for one window, parallel split.">
  <rect x="0" y="10" width="210" height="60" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="105" y="34" class="d-node" text-anchor="middle">CLAUDE.md</text>
  <text x="105" y="52" class="d-fix" text-anchor="middle">know every time — memory</text>

  <rect x="230" y="10" width="210" height="60" rx="4" fill="var(--sand)" opacity="0.45"/>
  <text x="335" y="34" class="d-node" text-anchor="middle">skill</text>
  <text x="335" y="52" class="d-fix" text-anchor="middle">do on demand — repeatable</text>

  <rect x="0" y="90" width="210" height="60" rx="4" fill="var(--interference)" opacity="0.3"/>
  <text x="105" y="114" class="d-node" text-anchor="middle">MCP</text>
  <text x="105" y="132" class="d-fix" text-anchor="middle">reach another app — access</text>

  <rect x="230" y="90" width="210" height="60" rx="4" fill="var(--muted)" opacity="0.3"/>
  <text x="335" y="114" class="d-node" text-anchor="middle">sub agent</text>
  <text x="335" y="132" class="d-fix" text-anchor="middle">too big for one window — split</text>

  <text x="0" y="180" class="d-label">rules and facts</text>
  <text x="230" y="180" class="d-label">a packaged, repeatable task</text>
  <text x="0" y="200" class="d-label">Gmail, CRM, video editor</text>
  <text x="230" y="200" class="d-label">parallel workers, clean main context</text>

  <text x="0" y="240" class="d-label">jam these together and you get unintentional bloat</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://youtube.com/shorts/JgdGmeAvZts",
        "channel": "Charlie Automates",
        "title": "CLAUDE.md vs Skills vs Subagents explained",
        "duration": "1:27",
    },
}
