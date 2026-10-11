NOTE = {
    "id": "skill-from-corrections",
    "concept": "A skill is the corrections, not the process",
    "one_liner": "Run the job without a skill first and write down only where Claude went wrong"
                 " — those corrections are the skill, because anything Claude already does right"
                 " costs tokens without changing the output.",

    "prerequisites": [],
    "related": ["skills-connectors-hooks", "skill-hell", "claude-md-as-index",
                "skill-description-routing"],

    "skeleton": [
        "Most skills document a process before Claude has ever tried the job.",
        "Run it without a skill first. Write down only what you had to correct.",
        "Those corrections are the skill. The rest Claude does anyway.",
        "In one test, 2 of 9 popular skill packs beat a same-length dummy file.",
        "Run skill vs no skill. Same score means the skill is decoration.",
    ],

    "mechanism": [
        "A skill changes the output only where it tells Claude something it wouldn't have done"
        " on its own. Write a skill from the process in your head and most of it describes steps"
        " Claude already gets right — each one paid for in tokens, none of them moving the"
        " result. Anthropic's skill guide, as the speaker relays it, runs it the other way round: complete the task without"
        " a skill, run it on real tasks, and write down where it actually went wrong. The skill"
        " is then reverse-engineered from real failures rather than imagined ones, and Anthropic's"
        " team say most of their own best skills started as a few lines and a single gotcha.",

        "The evidence that this matters is a placebo test. One developer (unnamed in the video)"
        " ran nine widely-starred skill packs — 450 runs on Opus 5.5, at the end of September —"
        " and only two of the nine beat a dummy file of the same length. The same-length dummy is"
        " the point: it controls for \"any extra text changes behaviour,\" so what's left is"
        " whether the skill's content did anything. For seven of nine, it didn't.",

        "Corrections are also model-specific. What a model gets wrong out of the box is a"
        " property of that model, so the skill has to be built on the model you'll actually run"
        " it on — another model will need more or fewer instructions. This refines rather than"
        " contradicts capturing a skill from one clean run ([[skills-connectors-hooks]]): capture"
        " from the run, but keep only the corrections that got it to your definition of done.",
    ],

    "numbers": [
        {"value": "2 of 9", "unit": "skill packs", "label": "that beat a same-length dummy file"
                                                           " in one developer's test"},
        {"value": "450", "unit": "runs", "label": "in that test, on Opus 5.5"},
    ],

    "analogy": None,

    "practice": [
        "Do the job with Claude and no skill first; log every correction you make.",
        "Write the skill from the corrections only — not from the process.",
        "Build and test it on the model you'll actually run it on.",
        "Run `claude plugin eval` with and without the skill; delete it if the scores match.",
        "Run /skill-doctor to see what each skill costs and how often it fires; cut the unused"
        " ones first, then eval the rest.",
        "Treat an installed skill pack as unproven until it beats no skill on your task.",
    ],

    "diagrams": [
        {
            "title": "Where a skill's tokens go",
            "caption": "Written from the process, most of a skill restates what Claude does"
                       " anyway. Written from the corrections, it is only the part that changes"
                       " the output.",
            "svg": '''<svg viewBox="0 0 460 246" role="img"
  aria-label="Two skills compared as stacked columns. A skill written from the process is a tall column, mostly steps Claude already does right, with a thin slice of corrections at the top. A skill written from corrections is only that thin slice. Only the corrections change the output; the rest costs tokens.">
  <text x="70" y="14" class="d-label" text-anchor="middle">FROM THE PROCESS</text>
  <rect x="20" y="24" width="100" height="22" rx="3" fill="var(--signal)" opacity="0.55"/>
  <rect x="20" y="48" width="100" height="142" rx="3" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="70" y="110" class="d-label" text-anchor="middle">steps Claude</text>
  <text x="70" y="124" class="d-label" text-anchor="middle">does anyway</text>
  <text x="70" y="208" class="d-num" text-anchor="middle">all of it costs tokens</text>

  <text x="250" y="14" class="d-label" text-anchor="middle">FROM CORRECTIONS</text>
  <rect x="200" y="24" width="100" height="22" rx="3" fill="var(--signal)" opacity="0.55"/>
  <rect x="200" y="48" width="100" height="142" rx="3" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="250" y="122" class="d-label" text-anchor="middle">left out</text>

  <path d="M300 35 H330" stroke="var(--signal)" stroke-width="1.5"/>
  <text x="336" y="32" class="d-fix">the corrections &#8212;</text>
  <text x="336" y="46" class="d-fix">the only part that</text>
  <text x="336" y="60" class="d-fix">changes the output</text>

  <text x="0" y="240" class="d-fix">same score with and without it = decoration</text>
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
