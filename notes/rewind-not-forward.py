NOTE = {
    "id": "rewind-not-forward",
    "concept": "Rewind, don't patch forward",
    "one_liner": "A broken output is cheaper to undo than to fix — rewind to before it happened"
                 " and regenerate, instead of asking the agent to correct its own mistake.",

    "prerequisites": [],
    "related": ["cache-loss-recovery"],

    "skeleton": [
        "A broken output: rewind to before it, don't ask for a correction.",
        "Rewind restores the session's own context — nothing is lost by going back.",
        "It does not undo bash. A deleted file needs git, not rewind.",
        "Clearing context is also recoverable this way, contrary to how it feels.",
    ],

    "mechanism": [
        "Asking an agent to fix a broken output means it now has to reason about two things at"
        " once: the original task, and its own wrong attempt still sitting in the conversation as"
        " context. That wrong attempt doesn't just sit there neutrally — it's now part of the"
        " history the model conditions on, so the correction is built on top of the mistake"
        " rather than starting clean. Rewinding to the point before the bad turn removes that"
        " contamination instead of asking the model to reason around it.",

        "This works because a session's context isn't actually destroyed by moving backward"
        " through it — the turns are still there, they're just not the active point anymore."
        " That's also true of a context you thought you cleared: going back to a previous session"
        " point can recover history that felt gone, because clearing the active window doesn't"
        " erase the session's own record of what happened in it.",

        "The one thing rewind cannot touch is anything done through bash. If a turn ran a shell"
        " command that deleted a file, rewinding the conversation back past that turn does not"
        " bring the file back — the session's history and the filesystem are two different"
        " things, and only one of them has an undo. Git is the recovery path for the other one.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Broken output? Rewind to before it and regenerate — don't ask for a patch.",
        "Don't assume /clear destroyed anything permanently; check rewind before re-deriving context by hand.",
        "Before any turn that runs a destructive shell command, remember rewind won't save you from it — commit first.",
    ],

    "diagrams": [
        {
            "title": "Two ways to leave a bad turn",
            "caption": "Patching forward carries the mistake as context. Rewinding removes it"
                       " from the history entirely.",
            "svg": '''<svg viewBox="0 0 500 190" role="img"
  aria-label="A session timeline with a bad turn. Patching forward keeps the bad turn in history and adds a correction on top, so both remain in context. Rewinding moves the active point back to before the bad turn and regenerates from there, so the bad turn is no longer part of what the model conditions on.">
  <text x="0" y="14" class="d-label">PATCH FORWARD</text>
  <rect x="0" y="24" width="80" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="40" y="43" class="d-label" text-anchor="middle">good</text>
  <rect x="88" y="24" width="80" height="30" rx="4" fill="var(--interference)" opacity="0.5"/>
  <text x="128" y="43" class="d-label" text-anchor="middle">bad turn</text>
  <rect x="176" y="24" width="80" height="30" rx="4" fill="var(--sand)" opacity="0.6"/>
  <text x="216" y="43" class="d-label" text-anchor="middle">"fix it"</text>
  <text x="0" y="76" class="d-fix">bad turn stays in context &#8212; correction reasons around it</text>

  <text x="0" y="112" class="d-label">REWIND</text>
  <rect x="0" y="122" width="80" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="40" y="141" class="d-label" text-anchor="middle">good</text>
  <rect x="88" y="122" width="80" height="30" rx="4" fill="var(--muted)" opacity="0.3" stroke-dasharray="3 3" stroke="var(--line)"/>
  <text x="128" y="141" class="d-label" text-anchor="middle">bad turn</text>
  <path d="M128 156 C 128 176, 40 176, 40 156" stroke="var(--signal)" stroke-width="2" fill="none" marker-end="url(#rnf-a)"/>
  <rect x="176" y="122" width="80" height="30" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="216" y="141" class="d-label" text-anchor="middle">regenerate</text>
  <text x="0" y="188" class="d-fix">active point moves back &#8212; bad turn no longer conditions the model</text>

  <defs>
    <marker id="rnf-a" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="var(--signal)"/></marker>
  </defs>
</svg>''',
        },
    ],

    "source": {
        "url": "https://youtu.be/RDeofKimDxo",
        "channel": "Simon Scrapes",
        "title": "37 Cheat Codes to Level Up In Claude Code in 19 Minutes",
        "duration": "20:06",
    },
}
