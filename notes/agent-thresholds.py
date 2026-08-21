NOTE = {
    "id": "agent-thresholds",
    "concept": "Thresholds, not disciplines",
    "one_liner": "Agents can handle more complexity than the numbers in a human style guide"
                 " allow. But a work method built for human memory, such as strict"
                 " test-driven development, does not work the same way for an agent.",

    "prerequisites": ["deterministic-gauntlet"],
    "related": ["strategic-load"],

    "skeleton": [
        "A CRAP score under 4 is Uncle Bob's human limit. Agents get 6, maybe 8.",
        "The reason: agents hold a more exact short-term memory than people do.",
        "He will not force strict test-driven development on an agent.",
        "Give the agent your values. Do not give it your exact work method.",
    ],

    "mechanism": [
        "The CRAP score mixes test coverage with code complexity. In simple terms, it counts the"
        " number of tested paths through a function. For code written by a human, Uncle Bob"
        " keeps that number below 4. For code written by an agent, he raised it to 6. He may"
        " raise it to 8. His reason is memory, not carelessness. Agents hold a much larger and"
        " more exact short-term memory than a human does. So the complexity limit that suits a"
        " human does not suit an agent.",

        "Test-driven development is a clearer case. In his own book, Uncle Bob argues for strict"
        " TDD: write one line of a test, then one line of code, and repeat. He follows this rule"
        " himself. He will not force this same rule on his agents. He once told an agent to use"
        " strict TDD. The agent still wrote a whole function first, then its test, in the style"
        " John Ousterhout uses. Uncle Bob has stopped fighting this. The agents do it their own"
        " way regardless of the instruction, so he lets them.",

        "His own words state the difference plainly: \"it's probably a mistake to impose a human"
        " discipline on an agent. It is not a mistake to impose human values on the agent, but"
        " there may be thresholds that we need to change.\" Strict TDD is a discipline. It fits a"
        " working memory an agent does not have. Test everything. Keep complexity within limits."
        " Do not ship code with no checks. These are values, and they still apply.",

        "He also states his own doubt. Some of these numbers came from talks with the agents"
        " themselves about where the limit should sit. He says so directly: \"you can't trust any"
        " debate you have with an agent, but I still have them anyway.\" The threshold is a live"
        " test, not a fixed rule.",
    ],

    "numbers": [
        {"value": "<4", "unit": "CRAP score", "label": "his own ceiling for human-written code"},
        {"value": "6", "unit": "CRAP score", "label": "his current ceiling for agent-written code — considering pushing to 8"},
    ],

    "analogy": None,

    "practice": [
        "Do not copy your human quality limits to an agent without a check. Ask if the reason"
        " for the number still applies.",
        "Ask if a rule exists because of human memory limits, before you force it on an agent.",
        "If an agent keeps going back to its own method despite the instruction, treat this as a"
        " signal to look at, not just disobedience to fix.",
        "Keep the value behind the rule (test everything, limit complexity). You can still loosen"
        " the exact number that enforces it.",
    ],

    "diagrams": [
        {
            "title": "Same score, different ceiling",
            "caption": "The CRAP score doesn't change meaning between a human and an agent — the"
                       " tolerable ceiling does, because the memory backing it does.",
            "svg": '''<svg viewBox="0 0 420 170" role="img"
  aria-label="Bar chart comparing CRAP score ceilings: below 4 for human-written code, 6 for agent-written code, with 8 marked as a value Uncle Bob is considering.">
  <line x1="40" y1="140" x2="400" y2="140" stroke="var(--line)" stroke-width="1"/>
  <line x1="40" y1="20" x2="40" y2="140" stroke="var(--line)" stroke-width="1"/>

  <rect x="90" y="92" width="70" height="48" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="125" y="86" class="d-num" text-anchor="middle">&lt;4</text>
  <text x="125" y="158" class="d-label" text-anchor="middle">human</text>

  <rect x="220" y="68" width="70" height="72" fill="var(--signal)" opacity="0.22" stroke="var(--signal)"/>
  <text x="255" y="62" class="d-num" text-anchor="middle">6</text>
  <text x="255" y="158" class="d-label" text-anchor="middle">agent (now)</text>

  <rect x="320" y="44" width="70" height="96" fill="none" stroke="var(--muted)" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="355" y="38" class="d-num" text-anchor="middle">8?</text>
  <text x="355" y="158" class="d-label" text-anchor="middle">agent (maybe)</text>

  <text x="14" y="82" class="d-label" text-anchor="middle" transform="rotate(-90 14 82)">tolerable pathways</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=zcLPGC-tvgk",
        "channel": "Matt Pocock",
        "title": "LIVE: Uncle Bob on Software Fundamentals in the Age of AI",
        "duration": "56:39",
    },
}
