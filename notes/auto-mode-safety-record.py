NOTE = {
    "id": "auto-mode-safety-record",
    "concept": "Auto mode's empirical safety record",
    "one_liner": "Manual permission prompts get rubber-stamped almost every time, so Anthropic"
                 " tested auto mode's classifier against how people actually click through"
                 " prompts, and across every measure — blind studies, real sessions, and"
                 " adversarial red-teaming — auto mode caught more of what mattered.",
    "prerequisites": ["auto-mode"],
    "related": ["prompt-injection"],

    "skeleton": [
        "Users approve 97% of permission prompts — reviewed reflexively, not read.",
        "Blind study: humans caught 13.6% of a swapped-in dangerous command; auto mode caught 89%.",
        "Human catch rate fell over a session, from 17% to 5%; auto mode's stayed flat.",
        "In flagged production sessions, manual approval had over twice the rate of unintended harm.",
        "Adversarial red-teaming with Apollo Research cut the classifier's miss rate from 12% to 7%.",
    ],

    "mechanism": [
        "The case for auto mode isn't that people are careless — it's that permission prompts are"
        " the wrong shape for the decision being asked. A session can throw dozens or hundreds of"
        " prompts at a developer who is mid-task, and the data shows what happens to any review"
        " process under that load: it becomes habitual. Users approve 97% of prompts, and 62% have"
        " at some point used bypassPermissions or clicked \"don't ask again\" on Bash outright."
        " Tellingly, people don't review everything equally badly — when Claude proposes a full"
        " plan for approval, users reject it 39% of the time. It's the small, frequent, individual"
        " permission request that gets rubber-stamped, at a 3% rejection rate.",

        "To test whether a classifier does better, Anthropic ran a blind study: 1,053 paid testers"
        " worked through a coding task, and partway through, one ordinary permission prompt was"
        " swapped for a clearly dangerous command — with the action itself never actually run,"
        " only the prompt text changed. Humans caught it 13.6% of the time. Auto mode, given the"
        " same swapped prompts, caught 89%. The gap widened with fatigue: human catch rate dropped"
        " from about 17% early in a session to about 5% after 50-plus prior prompts, while the"
        " classifier's rate held flat — it doesn't get tired, because it evaluates each action on"
        " its own, with no memory of how many prompts came before.",

        "That result held outside the lab too. Anthropic re-graded real sessions flagged by its"
        " safety pipeline on a 0-10 harm-severity scale, and at production-level severity (7+),"
        " sessions using manual approval contained a harmful action the user hadn't explicitly"
        " asked for 6.3% of the time, versus 2.4% for auto mode sessions — the gap held at every"
        " severity level tested.",

        "The prompt-injection numbers hide a detail worth pulling out: the risk isn't spread"
        " evenly across what an agent does. Split by task type, tool-calling tasks — where a"
        " result comes back as text — were already close to safe for everyone: 0% for Claude in"
        " auto mode, 2.00% even for GPT-5.6 Sol in Codex's Auto-review mode. Browser-use tasks,"
        " where the model reads a screenshot instead of structured text, are where the gap opens:"
        " still 0% for Claude, but 7.87% for GPT-5.6 Sol in Auto-review and 25.53% in Full Access."
        " The vulnerability isn't the model reasoning about untrusted content in general — it's"
        " specifically the harder-to-screen channel of a rendered image.",

        "The classifier isn't static, either. A two-week adversarial pilot with Apollo Research"
        " injected synthetic attacks into real coding trajectories; Anthropic hardened the"
        " classifier mainly by giving it more context about what it's protecting — repo"
        " visibility, git state, data-handling rules — rather than patching individual attacks."
        " Re-tested on a held-out attack set Anthropic never saw, the miss rate fell from 12% to"
        " 7%, evidence the fix generalized rather than just covering the shared examples. The same"
        " logic shows up in specific, narrow defenses layered on top: hard denies that can never"
        " be approved even if asked (data exfiltration), a check on whether a git push target is"
        " public or private before it runs, and a git-status check before destructive commands"
        " like `git reset --hard`.",
    ],

    "numbers": [
        {"value": "97", "unit": "%", "label": "of permission prompts users approve"},
        {"value": "3", "unit": "% vs 39%", "label": "rejection rate for individual permission requests vs. full plans"},
        {"value": "13.6", "unit": "%", "label": "of a swapped-in dangerous command humans caught (143 of 1,053 testers)"},
        {"value": "89", "unit": "%", "label": "of the same dangerous command auto mode caught (937 of 1,053)"},
        {"value": "17 → 5", "unit": "%", "label": "human catch rate early in a session vs. after 50+ prior prompts"},
        {"value": "6.3 vs 2.4", "unit": "%", "label": "manual vs. auto-mode sessions with unintended production-severity harm"},
        {"value": "12 → 7", "unit": "% miss rate", "label": "classifier's miss rate on held-out attacks, before and after Apollo Research hardening"},
        {"value": "25", "unit": "% more PRs", "label": "shipped by Teams & Enterprise auto mode adopters"},
        {"value": "0 vs 7.87", "unit": "%", "label": "attack success on browser-use tasks: Claude auto mode vs. GPT-5.6 Sol Auto-review"},
        {"value": "0 vs 2.00", "unit": "%", "label": "attack success on tool-calling tasks: Claude auto mode vs. GPT-5.6 Sol Auto-review"},
    ],

    "analogy": None,

    "practice": [
        "Treat 97% approval rates on your own prompts as a warning sign, not reassurance — that's"
        " exactly the habituation the data shows.",
        "Still review high-stakes changes to production infrastructure yourself; auto mode reduces"
        " risk, it doesn't eliminate it.",
        "Don't rely on broad allow-rules like Bash(python:*) — they're set aside entirely while in"
        " auto mode, since they'd let a command skip the classifier.",
        "Use hard-deny rules for anything your org should never approve, even on request.",
    ],

    "diagrams": [
        {
            "title": "Catch rate over a session: human fatigue vs. a classifier that doesn't tire",
            "caption": "Same dangerous command, same testers. Human review degrades as the session"
                       " goes on; auto mode's rate doesn't move.",
            "svg": '''<svg viewBox="0 0 520 200" role="img"
  aria-label="Line chart. Human catch rate of a dangerous command starts around 17 percent early in a session and falls to about 5 percent after fifty or more prior prompts. Auto mode's catch rate stays flat around 89 percent regardless of session length.">
  <line x1="40" y1="20" x2="40" y2="160" stroke="var(--line)" stroke-width="1"/>
  <line x1="40" y1="160" x2="500" y2="160" stroke="var(--line)" stroke-width="1"/>
  <text x="10" y="36" class="d-label">89%</text>
  <text x="10" y="106" class="d-label">17%</text>
  <text x="10" y="150" class="d-label">5%</text>

  <path d="M60 34 L480 34" stroke="var(--signal)" stroke-width="2.5" fill="none"/>
  <text x="480" y="26" class="d-fix" text-anchor="end">auto mode &#8212; flat</text>

  <path d="M60 100 Q 270 108 480 148" stroke="var(--interference)" stroke-width="2.5" fill="none"/>
  <text x="480" y="164" class="d-node" text-anchor="end">human review &#8212; degrades</text>

  <text x="60" y="180" class="d-label">early in session</text>
  <text x="480" y="180" class="d-label" text-anchor="end">50+ prior prompts</text>
</svg>''',
        },
        {
            "title": "Prompt injection risk concentrates in one channel: the screenshot",
            "caption": "Same two systems, split by task type. Reading tool results as text is"
                       " already close to safe for both; reading a rendered screenshot is where"
                       " the gap between them opens up.",
            "svg": '''<svg viewBox="0 0 520 230" role="img"
  aria-label="Grouped bar chart, attack success rate by task type. Tool-calling tasks, where results return as text: Claude auto mode 0 percent, Codex Auto-review 2.00 percent. Browser-use tasks, where the model reads a screenshot: Claude auto mode still 0 percent, Codex Auto-review 7.87 percent.">
  <line x1="40" y1="170" x2="480" y2="170" stroke="var(--line)" stroke-width="1"/>

  <rect x="20" y="8" width="10" height="10" fill="var(--signal)"/>
  <text x="36" y="17" class="d-label">Claude &#183; auto mode</text>
  <rect x="200" y="8" width="10" height="10" fill="var(--interference)"/>
  <text x="216" y="17" class="d-label">Codex &#183; Auto-review</text>

  <rect x="90" y="168" width="34" height="2" fill="var(--signal)"/>
  <text x="107" y="158" class="d-num" text-anchor="middle">0%</text>
  <rect x="134" y="150" width="34" height="20" fill="var(--interference)"/>
  <text x="151" y="144" class="d-num" text-anchor="middle">2.00%</text>
  <text x="129" y="196" class="d-node" text-anchor="middle">tool-calling</text>
  <text x="129" y="212" class="d-label" text-anchor="middle">results return as text</text>

  <rect x="330" y="168" width="34" height="2" fill="var(--signal)"/>
  <text x="347" y="158" class="d-num" text-anchor="middle">0%</text>
  <rect x="374" y="91" width="34" height="79" fill="var(--interference)"/>
  <text x="391" y="85" class="d-num" text-anchor="middle">7.87%</text>
  <text x="369" y="196" class="d-node" text-anchor="middle">browser-use</text>
  <text x="369" y="212" class="d-label" text-anchor="middle">model reads a screenshot</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://claude.com/blog/auto-mode-default-in-claude-code",
        "channel": "Anthropic / Claude blog",
        "title": "Auto mode is now the default in Claude Code for Pro, Max, and Team plans",
        "duration": "article, ~5 min read",
    },
}
