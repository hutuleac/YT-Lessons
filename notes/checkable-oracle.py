NOTE = {
    "id": "checkable-oracle",
    "concept": "Give it a way to check its work",
    "one_liner": "Hand the agent something that can objectively score its own output — a test"
                 " suite, a screenshot, a simulator — and it stops needing you between attempts,"
                 " because it can tell for itself whether the last one was closer.",

    "prerequisites": [],
    "related": ["agent-eyes", "deterministic-gauntlet", "ralph-loop"],

    "skeleton": [
        "One pass with no feedback signal gets you \"pretty good\" and stops there.",
        "An objective check — tests, screenshot, simulator — lets it grade its own attempt.",
        "Two or three self-graded iterations is where pretty good becomes almost perfect.",
        "The check must be machine-readable, not a matter of taste.",
        "Pick the check that fits the domain; any domain has one.",
    ],

    "mechanism": [
        "Boris, who built Claude Code, describes this as the workflow that separates a"
        " good result from a nearly correct one. Give the agent a mock and ask for the web UI and"
        " it gets close on the first attempt. The gap between close and right is not more"
        " instruction — it is more attempts, and attempts are only worth anything if something"
        " tells the agent which direction it moved in.",

        "That something has to be objective. A unit test run, a Puppeteer screenshot of the page,"
        " a screenshot from the iOS simulator: each produces evidence the model can read back on"
        " the next turn and compare against the target. Without one, the agent has already"
        " emitted its best single guess, and asking it to try again just resamples the same"
        " guess. With one, it has a gradient — this failed, that passed, the layout is off by"
        " this much — and it can walk it without you in the loop. His number is two or"
        " three iterations to go from good to almost perfect.",

        "The practical consequence is that setting up the check is the work. Whatever the domain"
        " is — unit tests, integration tests, browser screenshots, native app screenshots — the"
        " job is to hand the agent a way to see its own result, and then let it iterate. This is"
        " why a Puppeteer MCP server checked into a repo is worth more than any prompt written"
        " about the UI: it converts a single-shot request into a loop.",

        "It is a narrower thing than having the agent judge a product as a user would. Taste"
        " questions — is this headline persuasive, is this flow confusing — are not oracles,"
        " because there is no pass/fail to read back. Those still need a human, or an explicit"
        " persona framing.",
    ],

    "numbers": [
        {"value": "2-3", "unit": "iterations", "label": "from \"pretty good\" to \"almost"
                                                        " perfect\", given a check"},
    ],

    "analogy": None,

    "practice": [
        "Before prompting, ask what would tell the agent it got this wrong — then wire it up.",
        "Give UI work a screenshot tool (browser or simulator), not a written description.",
        "Give logic work a test command it can run itself, not a request to be careful.",
        "Say explicitly to iterate until the check passes, not to make one attempt.",
        "Check in the tooling — an MCP server or script in the repo — so the loop is shared.",
    ],

    "diagrams": [
        {
            "title": "Why one shot plateaus",
            "caption": "Without a check, every extra attempt is another sample of the same"
                       " guess. With one, each attempt starts from evidence about the last.",
            "svg": '''<svg viewBox="0 0 460 230" role="img"
  aria-label="A chart with attempts on the horizontal axis (1, 2, 3) and closeness to the target on the vertical axis. Without a check, the curve rises to pretty good on the first attempt and stays flat across attempts two and three. With a check, it starts at the same point and climbs on each attempt, reaching almost perfect by the third.">
  <line x1="46" y1="26" x2="46" y2="170" stroke="var(--line)" stroke-width="1.5"/>
  <line x1="46" y1="170" x2="420" y2="170" stroke="var(--line)" stroke-width="1.5"/>
  <text x="0" y="34" class="d-label">target</text>
  <text x="0" y="174" class="d-label">rough</text>
  <text x="120" y="190" class="d-label">attempt 1</text>
  <text x="230" y="190" class="d-label">attempt 2</text>
  <text x="340" y="190" class="d-label">attempt 3</text>

  <path d="M46 158 L140 92 L250 88 L360 86" fill="none" stroke="var(--interference)" stroke-width="2"/>
  <circle cx="140" cy="92" r="4" fill="var(--interference)"/>
  <circle cx="250" cy="88" r="4" fill="var(--interference)"/>
  <circle cx="360" cy="86" r="4" fill="var(--interference)"/>
  <text x="250" y="112" class="d-label">no check &#8212; flat</text>

  <path d="M46 158 L140 92 L250 62 L360 42" fill="none" stroke="var(--signal)" stroke-width="2"/>
  <circle cx="140" cy="92" r="4" fill="var(--signal)"/>
  <circle cx="250" cy="62" r="4" fill="var(--signal)"/>
  <circle cx="360" cy="42" r="4" fill="var(--signal)"/>
  <text x="250" y="34" class="d-num">tests / screenshots</text>

  <text x="46" y="216" class="d-fix">the check is what turns a second attempt into progress</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=pQ6G9TQfGIA",
        "channel": "frugle",
        "title": "Anthropic's FREE 24-Min Prompt Engineering Workshop (Beats Every $500 Course)",
        "duration": "27:55",
    },
}
