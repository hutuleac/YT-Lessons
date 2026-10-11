NOTE = {
    "id": "goal-judge",
    "concept": "The /goal judge only reads the chat",
    "one_liner": "/goal keeps Claude taking turns until a separate small model rules the goal met —"
                 " but that judge sees only the conversation, never your files or commands, so a"
                 " goal it can't verify from the transcript ends the loop early.",

    "prerequisites": ["checkable-oracle"],
    "related": ["ralph-loop", "ticket-scoping"],

    "skeleton": [
        "/goal types \"continue\" for you until the goal is met.",
        "A small model, like Haiku, decides whether it's met — after every turn.",
        "The judge reads only the chat. It never opens a file or runs a command.",
        "A vague goal gets judged on Claude's own claim — and ends early.",
        "A good goal: one end state, the proof, what mustn't change, a turn cap.",
    ],

    "mechanism": [
        "A check Claude can run is only half of an unattended loop. The other half is something"
        " that keeps Claude going until the check passes — otherwise you sit there typing"
        " \"continue\" to get it to fix its own evidence. /goal is that half: after every turn, a"
        " separate small model reads the goal you set and decides whether the condition is met."
        " If not, Claude takes another turn.",

        "The catch is what the judge can see. It doesn't run commands or read files"
        " independently; it gets the conversation — your goal and Claude's output — and nothing"
        " else. So it can only rule on evidence that has been printed into the transcript. Set a"
        " goal like \"the report is finished\" and the only evidence available is Claude saying"
        " the report is finished, which the judge has no way to contradict. The loop stops on a"
        " claim, not a result.",

        "That is why the goal has to name the proof, not just the end state. \"The check_report"
        " script passes and you show me the output\" forces the evidence into the chat where the"
        " judge can read it, and it ties the goal to the check written from your definition of"
        " done ([[checkable-oracle]]). Anthropic's guidance, as relayed in the video: one end"
        " state, how to prove it, what mustn't change, and a turn limit so a goal that can never"
        " be met doesn't run indefinitely.",

        "The speaker frames this as how it works today, and hopes the explicit command goes away"
        " — that you'll eventually set the done criteria and the loop will simply run until"
        " they're validated. The judge-sees-only-the-transcript constraint is the part to check"
        " again before relying on it.",
    ],

    "numbers": [
        {"value": "15", "unit": "turns", "label": "the turn cap in the example goal — a stop"
                                                  " condition, not a target"},
    ],

    "analogy": None,

    "practice": [
        "Write the goal as: end state, how to prove it, what mustn't change, turn cap.",
        "Make the proof something printed into the chat — \"show me the output\" — not a file"
        " the judge will never open.",
        "Point the goal at the check you already wrote, not at a description of being done.",
        "Example: /goal check_report passes and you show me the output; the template is"
        " unchanged; stop after 15 turns.",
    ],

    "diagrams": [
        {
            "title": "What the judge can see",
            "caption": "The judge rules on the transcript alone. Anything that only exists on"
                       " disk — a test result, a file diff — counts only once Claude prints it.",
            "svg": '''<svg viewBox="0 0 500 236" role="img"
  aria-label="A loop. Claude works, its turn lands in the transcript, which holds your goal, Claude's reply and any printed output. A small judge model reads only the transcript. If the goal is met the loop stops; if not, Claude takes another turn. Files, commands and disk sit outside the loop with a dashed line to the judge marked never read.">
  <path d="M410 46 V18 H60 V46" fill="none" stroke="var(--interference)" stroke-width="1.4"/>
  <text x="235" y="12" class="d-label" text-anchor="middle">not met &#8594; another turn</text>

  <rect x="0" y="46" width="120" height="40" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="60" y="70" class="d-node" text-anchor="middle">Claude works</text>
  <path d="M120 66 H170" stroke="var(--line)" stroke-width="1.5"/>

  <rect x="170" y="36" width="140" height="74" rx="5" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="240" y="54" class="d-fix" text-anchor="middle">transcript</text>
  <text x="182" y="72" class="d-label">your goal</text>
  <text x="182" y="86" class="d-label">Claude's reply</text>
  <text x="182" y="100" class="d-label">printed output</text>
  <path d="M310 66 H350" stroke="var(--signal)" stroke-width="1.5"/>

  <rect x="350" y="46" width="120" height="40" rx="5" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="410" y="64" class="d-node" text-anchor="middle">judge</text>
  <text x="410" y="78" class="d-label" text-anchor="middle">small model</text>
  <path d="M450 86 V112" stroke="var(--signal)" stroke-width="1.5"/>
  <text x="450" y="126" class="d-fix" text-anchor="middle">met &#8594; stop</text>

  <rect x="170" y="150" width="140" height="46" rx="5" fill="none" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="240" y="170" class="d-label" text-anchor="middle">files &#183; commands</text>
  <text x="240" y="184" class="d-label" text-anchor="middle">disk</text>
  <path d="M310 173 H380 V86" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="3 3"/>
  <text x="380" y="134" class="d-num" text-anchor="middle">&#10005;</text>
  <text x="370" y="148" class="d-label" text-anchor="end">never read</text>

  <text x="0" y="226" class="d-fix">a goal it can't verify from the chat ends on Claude's word</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=J9NQTYUP6k0",
        "channel": "Simon Scrapes",
        "title": "How the Top 1% Use Claude Code Differently",
        "duration": "18:09",
    },
}
