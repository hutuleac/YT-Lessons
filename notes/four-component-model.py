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
        " project, not task-specific instructions. Common uses: coding style rules, your stack"
        " and role, standing project constraints. Stuffing one-off procedures into it means"
        " paying to load them on turns that never need them.",

        "A skill and an MCP look similar from the outside — both are things you 'install' — but"
        " they solve opposite problems. A skill packages a way of doing something you already"
        " know how to describe in words: the instructions live in the skill, and Claude still"
        " does the work itself. Common uses: a PR review checklist, a landing-page teardown, a"
        " customer-notes extraction — anything you've typed a version of more than once. An MCP"
        " gives Claude reach it doesn't otherwise have — a live connection into Gmail, a CRM, a"
        " video editor — where the point isn't packaged instructions but the ability to act"
        " inside a system it couldn't touch before. Common uses: reading your inbox, pulling"
        " issues from a tracker, checking a live doc instead of a pasted copy.",

        "A sub agent solves neither memory nor access — it solves scale. When a task is too big"
        " to fit in one context window, or splits naturally into independent pieces, a sub agent"
        " lets Claude farm the work out to parallel workers and keep the main conversation's"
        " context clean instead of filling it with the intermediate steps of every sub-task."
        " Common uses: a refactor that touches many files, research fanned out across several"
        " sources, a codebase-wide audit.",

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
            "title": "CLAUDE.md: the same file, read again every turn",
            "caption": "Not triggered, always there — which is exactly why it should hold only"
                       " what needs to be true on every single turn.",
            "svg": '''<svg viewBox="0 0 440 218" role="img"
  aria-label="CLAUDE.md stays attached across three separate conversation turns, unlike a skill which is triggered on demand. Common uses: coding style rules, your stack and role, standing project constraints.">
  <text x="0" y="14" class="d-fix">CLAUDE.md</text>
  <rect x="20" y="20" width="8" height="140" rx="4" fill="var(--signal)" opacity="0.35"/>

  <rect x="50" y="20" width="150" height="40" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="125" y="44" class="d-node" text-anchor="middle">turn 1</text>
  <path d="M28 40 H50" stroke="var(--signal)" stroke-width="1.5"/>

  <rect x="50" y="70" width="150" height="40" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="125" y="94" class="d-node" text-anchor="middle">turn 2</text>
  <path d="M28 90 H50" stroke="var(--signal)" stroke-width="1.5"/>

  <rect x="50" y="120" width="150" height="40" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="125" y="144" class="d-node" text-anchor="middle">turn 3</text>
  <path d="M28 140 H50" stroke="var(--signal)" stroke-width="1.5"/>

  <path d="M200 40 H228" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="228" y="25" width="190" height="30" rx="5" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="323" y="45" class="d-label" text-anchor="middle">coding style rules</text>

  <path d="M200 90 H228" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="228" y="75" width="190" height="30" rx="5" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="323" y="95" class="d-label" text-anchor="middle">your stack, role, facts</text>

  <path d="M200 140 H228" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="228" y="125" width="190" height="30" rx="5" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="323" y="145" class="d-label" text-anchor="middle">project constraints</text>

  <text x="0" y="192" class="d-label">the same file, read again every turn —</text>
  <text x="0" y="206" class="d-label">not triggered, always there</text>
</svg>''',
        },
        {
            "title": "Skill: package once, trigger by name",
            "caption": "The second time you type a version of the same prompt, it should become"
                       " this instead.",
            "svg": '''<svg viewBox="0 0 460 240" role="img"
  aria-label="A prompt typed three times gets packaged once into a skill, then triggered by name into three different use cases: PR review checklist, landing-page teardown, customer-notes extraction.">
  <rect x="70" y="10" width="320" height="34" rx="6" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="230" y="32" class="d-label" text-anchor="middle">typed 3x: "review this the same way again"</text>

  <path d="M230 44 V70" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="140" y="70" width="180" height="50" rx="6" fill="var(--sand)" opacity="0.4"/>
  <text x="230" y="92" class="d-fix" text-anchor="middle">skill</text>
  <text x="230" y="108" class="d-label" text-anchor="middle">package once, run forever</text>

  <path d="M230 120 V150" stroke="var(--signal)" stroke-width="1.5"/>

  <path d="M230 150 V162 H80 V174" fill="none" stroke="var(--line)" stroke-width="1.5"/>
  <path d="M230 150 V174" stroke="var(--line)" stroke-width="1.5"/>
  <path d="M230 150 V162 H380 V174" fill="none" stroke="var(--line)" stroke-width="1.5"/>

  <rect x="10" y="174" width="140" height="46" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="80" y="193" class="d-node" text-anchor="middle">PR review</text>
  <text x="80" y="208" class="d-label" text-anchor="middle">checklist</text>

  <rect x="160" y="174" width="140" height="46" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="230" y="193" class="d-node" text-anchor="middle">landing-page</text>
  <text x="230" y="208" class="d-label" text-anchor="middle">teardown</text>

  <rect x="310" y="174" width="140" height="46" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="380" y="193" class="d-node" text-anchor="middle">customer notes</text>
  <text x="380" y="208" class="d-label" text-anchor="middle">extraction</text>

  <text x="10" y="236" class="d-label">one instruction, packaged once, triggered by name from then on</text>
</svg>''',
        },
        {
            "title": "MCP: access, not instructions",
            "caption": "A skill tells Claude how; an MCP gives it somewhere new to actually reach.",
            "svg": '''<svg viewBox="0 0 460 200" role="img"
  aria-label="Claude connects out through MCP to three external apps — Gmail, Linear, and Drive — reading and acting inside each. Common uses: read your inbox, pull issues from a tracker, check a live doc.">
  <rect x="170" y="10" width="120" height="40" rx="6" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="230" y="35" class="d-fix" text-anchor="middle">Claude</text>
  <circle cx="230" cy="50" r="3" fill="var(--signal)"/>

  <path d="M230 50 V66 H75 V110" fill="none" stroke="var(--interference)" stroke-width="1.5"/>
  <path d="M230 50 V110" stroke="var(--interference)" stroke-width="1.5"/>
  <path d="M230 50 V66 H385 V110" fill="none" stroke="var(--interference)" stroke-width="1.5"/>
  <circle cx="75" cy="110" r="3" fill="var(--interference)"/>
  <circle cx="230" cy="110" r="3" fill="var(--interference)"/>
  <circle cx="385" cy="110" r="3" fill="var(--interference)"/>

  <rect x="10" y="110" width="130" height="50" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="75" y="132" class="d-node" text-anchor="middle">Gmail</text>
  <text x="75" y="148" class="d-label" text-anchor="middle">read inbox</text>

  <rect x="165" y="110" width="130" height="50" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="230" y="132" class="d-node" text-anchor="middle">Linear</text>
  <text x="230" y="148" class="d-label" text-anchor="middle">pull issues</text>

  <rect x="320" y="110" width="130" height="50" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="385" y="132" class="d-node" text-anchor="middle">Drive</text>
  <text x="385" y="148" class="d-label" text-anchor="middle">check a doc</text>

  <text x="10" y="188" class="d-label">a live connection out — Claude reaches into the app itself</text>
</svg>''',
        },
        {
            "title": "Sub agent: split for scale, converge clean",
            "caption": "The trade is always the same: parallel workers out, a clean main thread"
                       " back.",
            "svg": '''<svg viewBox="0 0 460 250" role="img"
  aria-label="One main task splits into three parallel sub agent workers — a multi-file refactor, parallel research, a codebase audit — then converges back into a clean main context.">
  <rect x="140" y="10" width="180" height="44" rx="6" fill="var(--muted)" opacity="0.3"/>
  <text x="230" y="30" class="d-fix" text-anchor="middle">main task</text>
  <text x="230" y="46" class="d-label" text-anchor="middle">too big for one window</text>

  <path d="M230 54 V70 H75 V90" fill="none" stroke="var(--line)" stroke-width="1.5"/>
  <path d="M230 54 V90" stroke="var(--line)" stroke-width="1.5"/>
  <path d="M230 54 V70 H385 V90" fill="none" stroke="var(--line)" stroke-width="1.5"/>

  <rect x="10" y="90" width="130" height="50" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="75" y="110" class="d-node" text-anchor="middle">worker 1</text>
  <text x="75" y="126" class="d-label" text-anchor="middle">refactor files</text>

  <rect x="165" y="90" width="130" height="50" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="230" y="110" class="d-node" text-anchor="middle">worker 2</text>
  <text x="230" y="126" class="d-label" text-anchor="middle">parallel research</text>

  <rect x="320" y="90" width="130" height="50" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="385" y="110" class="d-node" text-anchor="middle">worker 3</text>
  <text x="385" y="126" class="d-label" text-anchor="middle">codebase audit</text>

  <path d="M75 140 V160 H230 V180" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <path d="M230 140 V180" stroke="var(--signal)" stroke-width="1.5"/>
  <path d="M385 140 V160 H230 V180" fill="none" stroke="var(--signal)" stroke-width="1.5"/>

  <rect x="140" y="180" width="180" height="44" rx="6" fill="none" stroke="var(--signal)"/>
  <text x="230" y="200" class="d-fix" text-anchor="middle">clean main context</text>
  <text x="230" y="216" class="d-label" text-anchor="middle">results merged back</text>
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
