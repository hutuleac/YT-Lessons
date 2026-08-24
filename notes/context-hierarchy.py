NOTE = {
    "id": "context-hierarchy",
    "concept": "The context hierarchy",
    "one_liner": "Agent context is not one file but a stack of scopes — enterprise, user,"
                 " project, directory — and the useful question about any piece of context is"
                 " which scope owns it and whether it loads every session or only on demand.",

    "prerequisites": [],
    "related": ["harness-bloat", "agent-memory", "repo-as-onboarding-packet",
                "skills-connectors-hooks"],

    "skeleton": [
        "A project CLAUDE.md is read into the first user turn of every session.",
        "The same scoping applies to commands, permissions and MCP config, not just memory.",
        "Enterprise scope sets policy users cannot override; local scope stays out of git.",
        "Nested files load only when the agent works in that directory — context on demand.",
        "Keep the always-loaded file short: it is paid for on every single request.",
        "Start with the shared project scope — written once, it benefits the whole team.",
    ],

    "mechanism": [
        "Boris's framing in his Claude Code talk is that the more context the agent has,"
        " the better its decisions, because an engineer working in a codebase carries a large"
        " amount of unwritten history that the agent starts without. But context is not free and"
        " not uniform, so the design question is placement: which scope owns this fact, and does"
        " it need to be present always or only sometimes.",

        "Two axes describe the whole system. The first is scope, running from enterprise policy"
        " through a user's global config, down to a project file checked into source control, a"
        " local project file kept out of it, and files in nested directories. The second is when"
        " it loads: a project-root CLAUDE.md is read automatically into the first user turn of"
        " every session, while a nested one is pulled in only when the agent works in that"
        " directory, and a slash command or an @-mentioned file is pulled in only when invoked.",

        "The same hierarchy governs more than memory. Permissions follow it, which is what makes"
        " enterprise scope interesting: a test command every employee runs can be pre-approved"
        " once for everyone, and a URL that should never be fetched can be blocked in a way an"
        " individual cannot override. MCP server configuration follows it too — an .mcp.json"
        " checked into the repo prompts every engineer who opens it to install the servers the"
        " team uses, instead of each one wiring up their own.",

        "The counterweight is cost. Everything in the always-loaded file is spent on every"
        " request, so his advice is to keep it as short as possible — common commands, the"
        " style guide, a few core files, architectural decisions — and to accept that a long one"
        " is usually not useful. When the matrix of options gets overwhelming, his recommended"
        " starting point is the shared project scope, because it is written once and everyone on"
        " the team gets the benefit. (Scope names and file locations are as of the talk; the"
        " shape of the hierarchy has been more stable than the specific paths.)",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Put team-wide facts in the project file and check it in; keep personal ones local.",
        "Move anything only relevant to one subtree into a CLAUDE.md inside that subtree.",
        "Turn a repeated multi-step prompt into a slash command instead of always-loaded prose.",
        "Use enterprise scope for pre-approved commands and hard blocks, not for advice.",
        "Check in the MCP config so a teammate's first session already has the team's tools.",
        "Re-read the always-loaded file periodically and cut anything not earning its tokens.",
    ],

    "diagrams": [
        {
            "title": "Scope against load time",
            "caption": "Both axes matter. Broad scope decides who gets it; load time decides"
                       " what it costs.",
            "svg": '''<svg viewBox="0 0 520 250" role="img"
  aria-label="A grid with two columns, loaded every session and loaded on demand, and rows for scope from enterprise down to directory. Enterprise policy, user global config and project CLAUDE.md sit in the always-loaded column. Nested directory CLAUDE.md files, slash commands and at-mentioned files sit in the on-demand column. A note marks the always-loaded column as paid on every request.">
  <text x="120" y="16" class="d-label">EVERY SESSION</text>
  <text x="330" y="16" class="d-label">ON DEMAND</text>

  <text x="0" y="48" class="d-label">enterprise</text>
  <rect x="110" y="30" width="180" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="120" y="48" class="d-node">policy: allow / block</text>

  <text x="0" y="86" class="d-label">user</text>
  <rect x="110" y="68" width="180" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="120" y="86" class="d-node">global config</text>
  <rect x="320" y="68" width="190" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="330" y="86" class="d-node">personal slash commands</text>

  <text x="0" y="124" class="d-label">project</text>
  <rect x="110" y="106" width="180" height="26" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="120" y="124" class="d-node">CLAUDE.md (checked in)</text>
  <rect x="320" y="106" width="190" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="330" y="124" class="d-node">commands, .mcp.json</text>

  <text x="0" y="162" class="d-label">directory</text>
  <rect x="320" y="144" width="190" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="330" y="162" class="d-node">nested CLAUDE.md</text>

  <text x="0" y="200" class="d-label">ad hoc</text>
  <rect x="320" y="182" width="190" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="330" y="200" class="d-node">@-mentioned file</text>

  <path d="M110 220 H290" fill="none" stroke="var(--interference)" stroke-width="1.5"/>
  <text x="110" y="240" class="d-fix">this column is paid for on every request &#8212; keep it short</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=pQ6G9TQfGIA",
        "channel": "frugle",
        "title": "Anthropic's FREE 24-Min Prompt Engineering Workshop (Beats Every $500 Course)",
        "duration": "27:55",
    },
}
