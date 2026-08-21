NOTE = {
    "id": "agent-thresholds",
    "concept": "Thresholds, not disciplines",
    "one_liner": "Agents can safely tolerate more complexity than the numbers in a human style"
                 " guide assume, but a workflow discipline built around human working memory —"
                 " like strict test-driven development — doesn't transfer to them at all.",

    "prerequisites": ["deterministic-gauntlet"],
    "related": ["strategic-load"],

    "skeleton": [
        "CRAP score under 4 is Uncle Bob's human ceiling; agents get 6, maybe 8.",
        "The reason: agents carry more accurate short-term memory than people do.",
        "He won't force strict test-driven development on an agent.",
        "Impose your values on an agent. Don't impose your workflow.",
    ],

    "mechanism": [
        "The CRAP score is a mix of test coverage and cyclomatic complexity — roughly, the number"
        " of tested pathways through a function. For human-written code Uncle Bob keeps that"
        " number below 4. For agent-written code he's deliberately widened it to 6, and is"
        " considering pushing it to 8. His reasoning is memory, not laxity: agents carry a much"
        " larger and more accurate short-term memory than a human does, so the complexity ceiling"
        " that keeps a human's head straight isn't the ceiling that keeps an agent's head"
        " straight.",

        "Test-driven development is a sharper case. He is, by his own book, a committed advocate"
        " of strict TDD — one line of test, one line of code, repeat — for himself. He refuses to"
        " impose that same discipline on his agents. Even when he explicitly instructs an agent"
        " to do strict TDD, it keeps falling back to writing a whole function and then its test,"
        " the way John Ousterhout would write it. He's stopped fighting that and lets it happen,"
        " because the agents do it anyway regardless of the instruction.",

        "His own framing of the distinction: \"it's probably a mistake to impose a human"
        " discipline on an agent. It is not a mistake to impose human values on the agent, but"
        " there may be thresholds that we need to change.\" TDD-as-ritual is a discipline, built"
        " for a working memory an agent doesn't have. Testing everything, keeping complexity"
        " bounded, refusing to ship unverified code — those are values, and they still hold.",

        "He's careful to flag his own uncertainty here too: the specific numbers came partly from"
        " debating the agents themselves about where the line should sit, and he says so plainly —"
        " \"you can't trust any debate you have with an agent, but I still have them anyway.\" The"
        " threshold is a live experiment, not a settled constant.",
    ],

    "numbers": [
        {"value": "<4", "unit": "CRAP score", "label": "his own ceiling for human-written code"},
        {"value": "6", "unit": "CRAP score", "label": "his current ceiling for agent-written code — considering pushing to 8"},
    ],

    "analogy": None,

    "practice": [
        "Don't carry your human quality thresholds over to an agent unexamined — check whether"
        " the reason for the number still applies.",
        "Ask whether a discipline exists because of human working-memory limits before you"
        " enforce it on an agent.",
        "If an agent keeps reverting to its own approach despite instruction, treat it as a"
        " signal worth investigating, not just disobedience to correct.",
        "Keep the underlying value (test everything, bound complexity) even as you loosen the"
        " specific numeric threshold that enforces it.",
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
