LESSON = {
    "id": "brief-and-verify",
    "title": "Stop steering Claude: brief it, check it, and add only what it gets wrong",
    "subject": "Claude Code setup",
    "standfirst": "Most Claude Code advice from a year ago — plan first, think hard, write long"
                  " rules, install skill packs — patched models that no longer ship. The current"
                  " pattern inverts it: say what done looks like, give Claude a way to prove it,"
                  " and only add infrastructure where it actually fails.",
    "audience": "You've used Claude Code for months and your setup has grown by accretion —"
                " plan-mode habits, a long CLAUDE.md, a folder of skills — and you're not sure"
                " which of it still earns its tokens.",

    "notes": [
        "ticket-scoping",
        "effort-levels",
        "checkable-oracle",
        "goal-judge",
        "claude-md-as-index",
        "skill-from-corrections",
        "deterministic-gauntlet",
        "scheduled-routines",
    ],

    "bridges": {
        "effort-levels": "Once the brief carries the task, the guardrails and the finish line,"
                         " the next old habit to drop is steering how hard Claude thinks about"
                         " it.",
        "checkable-oracle": "Checking after instead of planning before only works if the check is"
                            " something Claude can run itself — so the definition of done has to"
                            " become one.",
        "goal-judge": "A check Claude can run still needs something to keep it going until the"
                      " check passes, and /goal's judge can only rule on what the check prints"
                      " into the chat.",
        "claude-md-as-index": "With the loop running unattended, what it reads before every turn"
                              " matters more — and most of an old CLAUDE.md was written for a"
                              " model you no longer use.",
        "skill-from-corrections": "CLAUDE.md holds what's always true about the workspace; a"
                                  " skill holds what's true about one process — and, like the"
                                  " index, only the part Claude can't do on its own.",
        "deterministic-gauntlet": "Corrections in a skill are still text the model can drop. For"
                                  " anything that must never happen, text is the wrong tool.",
        "scheduled-routines": "Brief, check, goal, a lean index, corrective skills, hooks for"
                              " the hard lines — that's a package that can run without you"
                              " starting it.",
    },

    "closing": {
        "title": "Leave it alone until it fails",
        "body": "Every move here is the same move: give Claude the outcome and a way to prove it,"
                " watch where it actually goes wrong, and add infrastructure — a line in"
                " CLAUDE.md, a correction in a skill, a hook — only there. Re-run that audit"
                " each time the model changes, because the failures are a property of the model,"
                " not of your process.",
    },
}
