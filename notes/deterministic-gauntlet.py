NOTE = {
    "id": "deterministic-gauntlet",
    "concept": "The deterministic gauntlet",
    "one_liner": "A long list of written rules loses its power, because the model forgets rules in"
                 " the middle of the text. A tool that checks the code does not forget. Use a tool,"
                 " not a long list of rules.",

    "prerequisites": ["context-window"],
    "related": ["dumb-zone", "review-checkpoints", "tool-overload"],

    "skeleton": [
        "Written rules compete for space in a small area of full attention.",
        "A long list of rules becomes advice to the model, not law.",
        "A tool that checks the code does not lose strength. It passes or it fails.",
        "Keep the prompt short. Use a tool loop to enforce the rest.",
    ],

    "mechanism": [
        "Uncle Bob's first method with agents was simple: write down the rules. His prompts grew"
        " into documents of five to ten pages. They covered test-driven development, clean code,"
        " and style. He wanted the agents to follow all of it. The agents read the rules. Then"
        " they did not follow the rules. His own words for this: the agents treat the rules"
        " \"in the Pirates of the Caribbean sense — they're more like guidelines.\"",

        "The cause is the same effect that shapes the whole context window. Text at the start and"
        " the end of a long prompt keeps the model's attention. Text in the middle does not. A"
        " long document buries most of its own rules. Rule fifty of a fifty-rule document has, in"
        " practice, no effect at all.",

        "So he stopped writing long rule documents. His fix has two parts. First, cut the prompt"
        " down to the few words the agent must actually obey. Second, move every other rule out"
        " of the prompt and into a tool. He uses two tools for this: the CRAP score and mutation"
        " testing. The agent must run the tool and fix the code until the tool reports a pass. A"
        " tool sits outside the context window. It cannot get lost in the middle of a long"
        " document, because it is not part of the document.",

        "This method costs time. Each check in the loop slows the agent down. He trades speed for"
        " quality, and he says he has not found the point where this trade stops paying off. But"
        " he has found a floor. Even with many checks, the agent still works about two to four"
        " times faster than he does by hand.",
    ],

    "numbers": [
        {"value": "5-10", "unit": "pages", "label": "length his early instruction documents grew to before he abandoned steering"},
        {"value": "2-4x", "unit": "productivity", "label": "his estimated margin over doing the work himself, even slowed by the check loop"},
    ],

    "analogy": {
        "text": "They treat those rules in the Pirates of the Caribbean sense — they're more like"
                " guidelines.",
        "note": "This shows why long written rules lose strength. The model does not disobey on"
                " purpose. It has lost the rule somewhere in the middle of its own context.",
    },

    "practice": [
        "Keep the system prompt short. Use only the few sentences the agent must obey.",
        "Put every other rule into a tool the agent must pass, not into a paragraph it might"
        " read.",
        "Run the tool in a loop. Change the code until the tool passes, not until the agent"
        " says it is done.",
        "Bring back checks you once rejected as too slow for a human. An agent does not mind"
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
