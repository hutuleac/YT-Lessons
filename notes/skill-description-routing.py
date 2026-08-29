NOTE = {
    "id": "skill-description-routing",
    "concept": "The skill description is the router",
    "one_liner": "Claude picks which skill to load off the description field alone, before"
                 " reading the skill itself — so two similar descriptions mean the wrong one"
                 " fires, or none does.",

    "prerequisites": [],
    "related": ["skill-hell"],

    "skeleton": [
        "The description field decides which skill activates.",
        "Similar descriptions confuse the router or activate nothing.",
        "Write three things: what it does, when it triggers, when it doesn't.",
        "The anti-triggers matter as much as the triggers.",
    ],

    "mechanism": [
        "Claude never reads a skill's full body to decide whether to use it — it matches the"
        " request against the short description every skill exposes, and loads the body only"
        " after that match picks a winner. That makes the description the entire routing layer:"
        " a skill with a vague or overlapping description can be perfectly built and still never"
        " fire, or fire when it shouldn't, because the router never gets far enough to see the"
        " good part.",

        "The fix is a three-part description instead of a one-line label. State what the skill"
        " does in a single sentence — 'extracts or builds a brand voice, so every skill writes in"
        " their style.' State the triggers — the phrases and situations that should activate it,"
        " like 'writing style,' 'make this sound like me,' 'tone of voice.' Then state the"
        " anti-triggers explicitly: what this skill is not for, even though it sounds adjacent —"
        " 'does not trigger for positioning, audience research, or keyword work.'",

        "The anti-trigger line is the part people skip, and it's the one doing the"
        " disambiguation. Without it, two skills that both mention 'brand' or 'voice' compete for"
        " the same requests, and the router either guesses wrong or, worse, declines to activate"
        " either one because neither description stands out as the clear match.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Write the description as three lines: what it does, when it fires, when it doesn't.",
        "Before adding a new skill, check its description against existing ones for overlap.",
        "If two skills keep firing on the same requests, fix the anti-triggers first — not the body.",
    ],

    "diagrams": [
        {
            "title": "Routing happens before the body is ever read",
            "caption": "Only the description is matched against the request. The skill's own"
                       " content never gets a vote unless the description already won.",
            "svg": '''<svg viewBox="0 0 500 210" role="img"
  aria-label="A request is matched against three skill descriptions. Skill A has a vague description that overlaps skill B, so the router picks the wrong one or neither. Skill C has a three-part description (does, triggers, anti-triggers) and wins cleanly, only then loading its full body.">
  <rect x="0" y="10" width="130" height="36" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="65" y="33" class="d-node" text-anchor="middle">request</text>

  <path d="M130 28 H180" stroke="var(--line)" fill="none"/>

  <rect x="184" y="0" width="150" height="30" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="259" y="19" class="d-label" text-anchor="middle">skill A: "brand stuff"</text>

  <rect x="184" y="34" width="150" height="30" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="259" y="53" class="d-label" text-anchor="middle">skill B: "brand voice"</text>

  <text x="184" y="82" class="d-fix">overlap &#8594; wrong pick or no pick</text>

  <rect x="184" y="104" width="150" height="30" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="259" y="123" class="d-fix" text-anchor="middle" style="font-size:9px">does / triggers / not</text>

  <path d="M334 119 H400" stroke="var(--signal)" stroke-width="2" fill="none" marker-end="url(#sdr-a)"/>
  <rect x="404" y="98" width="90" height="42" rx="4" fill="var(--surface-2)" stroke="var(--signal)" stroke-width="2"/>
  <text x="449" y="123" class="d-node" text-anchor="middle">body loads</text>

  <text x="0" y="180" class="d-fix">the body is never a tiebreaker &#8212; the description already decided</text>

  <defs>
    <marker id="sdr-a" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="var(--signal)"/></marker>
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
