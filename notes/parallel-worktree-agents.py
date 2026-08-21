NOTE = {
    "id": "parallel-worktree-agents",
    "concept": "One session, one assignment",
    "one_liner": "Worktree-isolated sessions let several agents work at once without their"
                 " changes mixing — but only if each session gets one clear job, or you end up"
                 " with a pile of tangled work to sort out at the end of the day."
                 ,

    "prerequisites": [],
    "related": ["ticket-scoping", "skill-hell"],

    "skeleton": [
        "Separate sessions, separate worktrees — changes stay isolated instead of mixing.",
        "One session, one clear assignment, one specific handoff format.",
        "Different job types in parallel: a bug fix, a copy change, a sales asset.",
        "The goal is small packets you can review, not one big pile to untangle.",
    ],

    "mechanism": [
        "Running several agent sessions at once is only useful if the isolation is real: with"
        " worktree isolation, each session gets its own context and its own set of changes,"
        " so a debugging session and a copy-editing session don't collide on the same files."
        " That mechanical guarantee is what makes parallel work safe to attempt at all.",

        "What makes it actually productive is scoping each session like a separate hire: the bug"
        " session gets the root cause, the files touched, and what to check in the diff; the"
        " copy session gets a before/after and why the new version is clearer; the sales session"
        " gets the objection it was solving for and what to review before recording. Different"
        " job, same project context, one specific handoff shape per session.",

        "The failure mode this avoids is spraying work across a repo and ending the day with a"
        " single giant, tangled set of changes nobody wants to review. Isolation plus a scoped"
        " handoff turns 'several things happened' into several small packets you can inspect,"
        " accept, revise, or reject independently.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Before starting parallel sessions, write one specific handoff format per session — what"
        " it should come back with, not just what it should do.",
        "Mix job types across sessions (bug fix, copy, sales asset) rather than three variations"
        " on the same task — that's what actually benefits from isolation.",
        "Review and merge each session's output separately; don't let three sessions' changes"
        " pile up before you look at any of them.",
    ],

    "diagrams": [
        {
            "title": "Three jobs, three isolated sessions",
            "caption": "Same project context, separate worktrees — each comes back as one"
                       " reviewable packet instead of one tangled pile.",
            "svg": '''<svg viewBox="0 0 460 180" role="img"
  aria-label="Three parallel agent sessions, each in its own worktree, working on different jobs: a bug fix, a landing page hero rewrite, and a sales demo script. Each returns a separate reviewable packet.">
  <rect x="150" y="4" width="160" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="230" y="21" class="d-label" text-anchor="middle">same project context</text>
  <path d="M230 30 V44" stroke="var(--line)" stroke-width="1.2"/>
  <path d="M230 44 H70 M230 44 H390" stroke="var(--line)" stroke-width="1.2"/>
  <path d="M70 44 V58 M230 44 V58 M390 44 V58" stroke="var(--line)" stroke-width="1.2"/>

  <rect x="10" y="58" width="120" height="30" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="70" y="77" class="d-label" text-anchor="middle">bug fix</text>
  <rect x="170" y="58" width="120" height="30" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="230" y="77" class="d-label" text-anchor="middle">hero rewrite</text>
  <rect x="330" y="58" width="120" height="30" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="390" y="77" class="d-label" text-anchor="middle">demo script</text>

  <path d="M70 88 V102 M230 88 V102 M390 88 V102" stroke="var(--line)" stroke-width="1"/>
  <rect x="15" y="102" width="110" height="52" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="70" y="120" class="d-fix" text-anchor="middle">root cause,</text>
  <text x="70" y="134" class="d-fix" text-anchor="middle">files, checks</text>

  <rect x="175" y="102" width="110" height="52" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="230" y="120" class="d-fix" text-anchor="middle">before/after,</text>
  <text x="230" y="134" class="d-fix" text-anchor="middle">why clearer</text>

  <rect x="335" y="102" width="110" height="52" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="390" y="120" class="d-fix" text-anchor="middle">objection,</text>
  <text x="390" y="134" class="d-fix" text-anchor="middle">script draft</text>

  <text x="0" y="176" class="d-label">three separate packets &#8212; reviewed and merged independently</text>
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
