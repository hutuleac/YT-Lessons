NOTE = {
    "id": "strategic-load",
    "concept": "AI ate the tactical layer",
    "one_liner": "Coding used to alternate between strategic thinking and tactical work that gave"
                 " your brain a rest; agents took the tactical half, so the day is now strategy"
                 " end to end — which is why it is exhausting.",
    "prerequisites": [],
    "related": ["review-checkpoints", "codebase-as-environment"],

    "skeleton": [
        "Writing code used to be the break in the day.",
        "That tactical layer is the part AI took.",
        "What is left is strategic thinking, all day.",
        "Everyone has effectively been promoted to lead developer.",
    ],

    "mechanism": [
        "Programming used to alternate between two modes. Strategic thinking — what to build, how"
        " it fits — and tactical work, where you sat down and wrote the code. The tactical stretch"
        " was almost non-verbal: moving things around, close to playing a game, and a rest for the"
        " part of your brain that had been deciding things.",

        "Agents took that half. The grunt work is gone, which sounds like pure gain, but the rest"
        " period went with it. What remains is the strategic layer, and you are in it all day"
        " because you have to operate one level above whatever the agent is doing.",

        "That is the promotion nobody asked for: everyone has effectively become a lead developer."
        " The work is higher up the chain and it demands high-level thinking continuously, which"
        " is a different kind of tiring than writing a lot of code.",

        "Pocock does not offer a fix, and says so — he thinks it is baked in. He also says he likes"
        " making the high-level decisions and still ends each day knackered. Both things are true"
        " at once, and naming the cause is most of the value here.",
    ],

    "numbers": [],

    "analogy": {
        "text": "We've all turned into lead developers.",
        "note": "It explains the fatigue better than 'AI is tiring' does: the exhaustion is the"
                " normal cost of a role, and it arrived without the title or the expectation.",
    },

    "practice": [
        "Budget the strategic day like a lead's day, not a maker's day — it has no built-in rest.",
        "Schedule breaks deliberately; the tactical work that used to provide them is gone.",
        "Batch the decisions that need you and let the agent run between them.",
        "Notice when fatigue is the load, not the tooling — swapping tools won't fix a role change.",
    ],

    "diagrams": [
        {
            "title": "Where the day used to go, and where it goes now",
            "caption": "The same hours. The tactical block that used to break up the decisions is"
                       " the block the agent absorbed.",
            "svg": '''<svg viewBox="0 0 460 176" role="img"
  aria-label="Two bars representing a working day. Before AI, alternating strategic and tactical blocks. After AI, one continuous strategic block with the tactical work moved to the agent.">
  <text x="0" y="12" class="d-label">BEFORE &#183; strategy alternating with tactical work</text>
  <rect x="0" y="22" width="70" height="34" rx="3" fill="var(--interference)" opacity="0.45"/>
  <rect x="72" y="22" width="120" height="34" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="132" y="43" class="d-label" text-anchor="middle">writing code</text>
  <rect x="194" y="22" width="70" height="34" rx="3" fill="var(--interference)" opacity="0.45"/>
  <rect x="266" y="22" width="120" height="34" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="326" y="43" class="d-label" text-anchor="middle">writing code</text>
  <rect x="388" y="22" width="72" height="34" rx="3" fill="var(--interference)" opacity="0.45"/>
  <text x="0" y="74" class="d-label">the shaded blocks are decisions &#8212; the gaps were the rest</text>

  <text x="0" y="116" class="d-label">NOW &#183; decisions end to end</text>
  <rect x="0" y="126" width="460" height="34" rx="3" fill="var(--interference)" opacity="0.45"/>
  <text x="230" y="147" class="d-node" text-anchor="middle">strategic thinking</text>
  <text x="0" y="172" class="d-label">the tactical block moved to the agent, and took the break with it</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/e-pFrQ_Rh0s",
        "channel": "Matt Pocock",
        "title": "AI Coding is exhausting",
        "duration": "1:15",
    },
}
