NOTE = {
    "id": "skill-hell",
    "concept": "Skill hell",
    "one_liner": "Stacking every agent framework you can find into one context window at once —"
                 " the same overload as tool bloat, arriving through process instead of tools.",

    "prerequisites": ["dumb-zone"],
    "related": ["tool-overload"],

    "skeleton": [
        "After framework hell and tutorial hell: skill hell.",
        "Cobbling several agent frameworks together until none of them works.",
        "The failure is mechanical — it is all one context window.",
        "Skills should empower the user, not the agent.",
    ],

    "mechanism": [
        "Pocock puts this in a lineage developers already recognise. There was framework hell,"
        " then tutorial hell, and now skill hell: trying several agent frameworks at once —"
        " he names GSD, Spec Kit, BMAD — and cobbling them into something that works, which it"
        " doesn't. He notes he has contributed to the problem himself, having published a set of"
        " skills.",

        "The failure is mechanical, not aesthetic. Loading a pile of skills at once means"
        " smacking a bunch of stuff into the same context window — often without reading any of"
        " it, just checking whether it works. That is the same overload as tool bloat, reached"
        " through process instead of tool definitions.",

        "His diagnosis of the cause is a control inversion. People are trying to take software"
        " development processes and encode them directly into the agent. He argues the opposite:"
        " skills should empower the user, not the agent — your hand stays on the steering wheel,"
        " and a skill is your process made repeatable rather than autonomy handed over.",

        "The practical difference is sequencing. When you drive the skills, you understand each"
        " stage, you can guide the agent, and only what the current stage needs is loaded. That"
        " does not mean staying in the loop for everything — you can still delegate and go AFK —"
        " but you own the shape of the process rather than hoping a stack of frameworks agrees.",
    ],

    "numbers": [],

    "analogy": {
        "text": "You should have your hand on the steering wheel.",
        "note": "The test for any skill or framework: does it give you a repeatable version of"
                " your own process, or does it hand the process to the agent and ask you to"
                " trust the result?",
    },

    "practice": [
        "Run one framework properly instead of three partially — overlap is what floods the window.",
        "Read a skill before installing it. Loading it to see if it works is the whole failure mode.",
        "Judge a skill by whether it makes your process repeatable, not by how autonomous it is.",
        "Sequence stages so each loads only what it needs, then delegate the stage and step away.",
    ],

    "diagrams": [
        {
            "title": "Same skills, two ways of loading them",
            "caption": "Stacked, they compete for one window and push the work into the dumb"
                       " zone. Sequenced, each stage gets a window that fits it.",
            "svg": '''<svg viewBox="0 0 520 214" role="img"
  aria-label="Top: five skills loaded into a single context window that overflows. Bottom: the same skills run as three sequential stages, each in its own small context window.">
  <text x="0" y="12" class="d-label">ALL AT ONCE</text>
  <rect x="0" y="22" width="520" height="40" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <rect x="4" y="26" width="98" height="32" rx="3" fill="var(--interference)" opacity="0.5"/>
  <rect x="106" y="26" width="98" height="32" rx="3" fill="var(--interference)" opacity="0.5"/>
  <rect x="208" y="26" width="98" height="32" rx="3" fill="var(--interference)" opacity="0.5"/>
  <rect x="310" y="26" width="98" height="32" rx="3" fill="var(--interference)" opacity="0.5"/>
  <rect x="412" y="26" width="98" height="32" rx="3" fill="var(--interference)" opacity="0.5"/>
  <text x="260" y="47" class="d-node" text-anchor="middle">skills</text>
  <text x="0" y="80" class="d-label">no room left for the actual task &#8594; dumb zone</text>

  <text x="0" y="126" class="d-label">YOU DRIVE</text>
  <rect x="0" y="136" width="150" height="40" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <rect x="4" y="140" width="60" height="32" rx="3" fill="var(--signal)" opacity="0.45"/>
  <text x="103" y="160" class="d-label" text-anchor="middle">room</text>
  <text x="163" y="160" class="d-node">&#8594;</text>
  <rect x="185" y="136" width="150" height="40" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <rect x="189" y="140" width="60" height="32" rx="3" fill="var(--signal)" opacity="0.45"/>
  <text x="288" y="160" class="d-label" text-anchor="middle">room</text>
  <text x="348" y="160" class="d-node">&#8594;</text>
  <rect x="370" y="136" width="150" height="40" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <rect x="374" y="140" width="60" height="32" rx="3" fill="var(--signal)" opacity="0.45"/>
  <text x="473" y="160" class="d-label" text-anchor="middle">room</text>
  <text x="0" y="196" class="d-label">one stage at a time, each in a window that fits it</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/32LyZyFQhCQ",
        "channel": "Matt Pocock",
        "title": "Framework Hell, Tutorial Hell... now Skill Hell",
        "duration": "1:30",
    },
}
