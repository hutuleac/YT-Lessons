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
            "title": "Prompt injection: attack success by permission mode",
            "caption": "720 held-out attacks, tested 10x each. Auto mode blocked all of them;"
                       " unrestricted modes did not.",
            "svg": '''<svg viewBox="0 0 520 190" role="img"
  aria-label="Bar chart of prompt injection attack success rate by mode. Claude auto mode: 0 percent. Claude bypassPermissions mode, an unguarded baseline: 0.09 percent. Codex Auto-review mode: 5.83 percent. Codex Full Access mode: 19.03 percent.">
  <text x="0" y="16" class="d-label">attack success rate, third-party evaluation</text>

  <text x="0" y="46" class="d-label">Claude &#183; auto mode</text>
  <rect x="180" y="34" width="2" height="16" fill="var(--signal)"/>
  <text x="188" y="46" class="d-num">0%</text>

  <text x="0" y="76" class="d-label">Claude &#183; bypassPermissions</text>
  <rect x="180" y="64" width="3" height="16" fill="var(--signal)"/>
  <text x="188" y="76" class="d-num">0.09%</text>

  <text x="0" y="106" class="d-label">Codex &#183; Auto-review</text>
  <rect x="180" y="94" width="80" height="16" fill="var(--sand)"/>
  <text x="266" y="106" class="d-num">5.83%</text>

  <text x="0" y="136" class="d-label">Codex &#183; Full Access</text>
  <rect x="180" y="124" width="260" height="16" fill="var(--interference)"/>
  <text x="446" y="136" class="d-num">19.03%</text>

  <text x="0" y="170" class="d-label">source: Trajectory Labs, 72 scenarios x 10 runs, evaluated July 2026</text>
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
