NOTE = {
    "id": "deterministic-gauntlet",
    "concept": "The deterministic gauntlet",
    "one_liner": "A rules document decays the moment it stops fitting in the model's priority zone;"
                 " a tool the agent must satisfy in a loop does not, so verification beats"
                 " instruction once the rules get long.",

    "prerequisites": ["context-window"],
    "related": ["dumb-zone", "review-checkpoints", "tool-overload"],

    "skeleton": [
        "Prompted rules compete for space in a shrinking priority zone.",
        "Long enough, and the model treats them as guidelines, not law.",
        "A deterministic tool doesn't fade — it passes or it doesn't.",
        "Trim the prompt to the minimum. Enforce the rest with a loop.",
    ],

    "mechanism": [
        "Uncle Bob's first instinct with agents was the obvious one: write down the rules. His"
        " prompts grew into five-to-ten-page documents covering test-driven development, clean"
        " code, style — everything he wanted respected. The agents read them and then didn't"
        " follow them. His own line for it: they treat those rules \"in the Pirates of the"
        " Caribbean sense — they're more like guidelines.\"",

        "The cause is the same lost-in-the-middle effect that shapes the context window generally:"
        " content at the very start and very end of a long prompt keeps priority, and everything"
        " else gets buried as the document grows. Rule fifty of a fifty-rule document is,"
        " functionally, gone.",

        "So he stopped competing for that space. The fix is to trim the initial prompt to the"
        " absolute minimum it needs to stay in the priority zone, then push everything else out"
        " of the prompt entirely and into deterministic tools — his revived CRAP score and"
        " mutation testing — run in a loop: the agent must keep changing the code until the tool"
        " reports pass, not until it feels finished. A tool outside the context window can't be"
        " lost in the middle of it.",

        "This isn't free. Every check in the loop slows the agent down, trading raw speed for"
        " quality, and he's honest that he hasn't found the point where that trade stops paying"
        " off. What he has found is a floor: even heavily constrained by checks, the agent still"
        " runs roughly two to four times faster than doing the work himself.",
    ],

    "numbers": [
        {"value": "5-10", "unit": "pages", "label": "length his early instruction documents grew to before he abandoned steering"},
        {"value": "2-4x", "unit": "productivity", "label": "his estimated margin over doing the work himself, even slowed by the check loop"},
    ],

    "analogy": {
        "text": "They treat those rules in the Pirates of the Caribbean sense — they're more like"
                " guidelines.",
        "note": "Explains why prose rules decay with length: the model isn't disobeying on"
                " purpose, it has genuinely lost the instruction somewhere in the middle of its"
                " own context.",
    },

    "practice": [
        "Keep the system prompt to the handful of sentences you actually need obeyed.",
        "Move every other rule into a deterministic tool the agent must satisfy, not a paragraph"
        " it might read.",
        "Run the tool in a loop — change the code until the tool passes, not until the agent"
        " says it's done.",
        "Revive checks you once rejected for being too slow for a human. An agent doesn't mind"
        " the wait.",
    ],

    "diagrams": [
        {
            "title": "A rule you write versus a rule you enforce",
            "caption": "A prompted rule fades once it's buried mid-document. A tool sits outside"
                       " the context window entirely, so the agent can't lose track of it — it"
                       " just loops until the tool says pass.",
            "svg": '''<svg viewBox="0 0 480 210" role="img"
  aria-label="Diagram contrasting a prompted rule, which fades as it is buried in a long document, with a deterministic tool loop, where the agent edits code and re-checks until the tool passes.">
  <defs>
    <marker id="dg-arrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0 0 L8 4 L0 8 z" fill="var(--muted)"/>
    </marker>
  </defs>

  <text x="0" y="14" class="d-label">PROMPTED RULE</text>
  <rect x="0" y="24" width="220" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="110" y="43" class="d-label" text-anchor="middle">rule 1 (kept)</text>
  <rect x="0" y="60" width="220" height="30" rx="4" fill="var(--interference)" opacity="0.18" stroke="var(--line)"/>
  <text x="110" y="79" class="d-label" text-anchor="middle" opacity="0.6">rule 25 (lost in the middle)</text>
  <rect x="0" y="96" width="220" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="110" y="115" class="d-label" text-anchor="middle">rule 50 (kept)</text>

  <text x="260" y="14" class="d-label">DETERMINISTIC LOOP</text>
  <rect x="260" y="24" width="90" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="305" y="45" class="d-node" text-anchor="middle">agent</text>
  <rect x="380" y="24" width="90" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="425" y="41" class="d-node" text-anchor="middle">crap +</text>
  <text x="425" y="53" class="d-node" text-anchor="middle">mutation</text>
  <line x1="350" y1="41" x2="378" y2="41" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#dg-arrow)"/>
  <path d="M425 60 C 425 100, 305 100, 305 60" fill="none" stroke="var(--signal)" stroke-width="1.5" marker-end="url(#dg-arrow)"/>
  <text x="365" y="96" class="d-fix" text-anchor="middle">fail &#8594; fix &#8594; recheck</text>
  <text x="425" y="80" class="d-label" text-anchor="middle">pass &#8594; done</text>

  <text x="0" y="150" class="d-label">A tool never lives in the middle of the prompt, so it never fades.</text>
  <text x="0" y="170" class="d-label">The agent loops on it directly until the check itself says stop.</text>
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
