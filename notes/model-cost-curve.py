NOTE = {
    "id": "model-cost-curve",
    "concept": "Read the cost-quality curve",
    "one_liner": "Plotting models and effort levels as quality against cost per completed task"
                 " shows what a single benchmark number hides: the same score is available at"
                 " wildly different prices, and the top effort levels often buy nothing.",
    "prerequisites": ["effort-levels"],
    "related": ["tokens"],

    "skeleton": [
        "Plot quality against average cost per task, not quality alone.",
        "Each model traces a curve as its effort level rises.",
        "The curve flattens — extra-high and max can be indistinguishable.",
        "The same score is often available far cheaper from another model.",
    ],

    "mechanism": [
        "The chart Pocock recommends puts average cost per task along the bottom and quality — the"
        " share of tasks solved — up the side, then plots each model at each of its effort levels."
        " One model becomes a curve rather than a number, which is what makes it useful.",

        "Read across a curve and you see where effort stops paying. A model can differ sharply"
        " between low, medium and high, then show no meaningful difference between extra-high and"
        " max while costing considerably more. That flat top is money spent on nothing.",

        "Read across curves and you see the substitution. On the benchmark he shows, one model at"
        " high effort lands around $13 per completed task, while another reaches roughly the same"
        " quality at about $3.50. Another sits near 40% at medium and only about 54% at max —"
        " where max costs more than the stronger model's high setting.",

        "His caveat is not decoration. All benchmarks are flawed because they do not represent"
        " your day-to-day work, so this is a starting point for choosing an effort level rather"
        " than an answer — most useful, he notes, for seeing the differences at the low end, which"
        " is where the cheap wins are.",
    ],

    "numbers": [
        {"value": "$13", "unit": "per task", "label": "one model at high effort on the benchmark shown"},
        {"value": "$3.50", "unit": "per task", "label": "comparable quality from a different model at high effort"},
        {"value": "40%", "unit": "of tasks", "label": "a mid-tier model at medium effort"},
        {"value": "54%", "unit": "of tasks", "label": "the same model at max — for more than the stronger model's high"},
    ],

    "analogy": None,

    "practice": [
        "Compare models on cost per completed task, not on the headline benchmark score.",
        "Find where your model's curve flattens and stop paying past that point.",
        "Check the low end first — that is where effort levels differ most and cost least.",
        "Re-test on your own work; a benchmark is a starting point, not a decision.",
    ],

    "diagrams": [
        {
            "title": "Quality against cost, one curve per model",
            "caption": "Shape of the chart, not exact figures. The flat top is effort you are"
                       " paying for and not receiving; the horizontal gap is the same quality at"
                       " a different price.",
            "svg": '''<svg viewBox="0 0 460 216" role="img"
  aria-label="A scatter chart with cost per task on the horizontal axis and quality on the vertical axis. One model's curve rises steeply then flattens at high cost; a second model reaches similar quality at much lower cost; a third plateaus at a lower quality despite high cost.">
  <line x1="38" y1="168" x2="450" y2="168" stroke="var(--line)" stroke-width="1"/>
  <line x1="38" y1="16" x2="38" y2="168" stroke="var(--line)" stroke-width="1"/>
  <text x="18" y="96" class="d-label" text-anchor="middle" transform="rotate(-90 18 96)">quality</text>
  <text x="244" y="196" class="d-label" text-anchor="middle">average cost per completed task &#8594;</text>

  <path d="M60 140 C 120 96, 180 60, 300 48 C 360 44, 400 42, 430 41"
        fill="none" stroke="var(--interference)" stroke-width="2" stroke-linecap="round"/>
  <g fill="var(--interference)">
    <circle cx="60" cy="140" r="4"/><circle cx="150" cy="80" r="4"/>
    <circle cx="300" cy="48" r="4"/><circle cx="430" cy="41" r="4"/>
  </g>
  <text x="330" y="34" class="d-label">extra-high and max: no gain</text>

  <path d="M52 150 C 80 120, 110 70, 150 56" fill="none" stroke="var(--signal)"
        stroke-width="2" stroke-linecap="round"/>
  <g fill="var(--signal)"><circle cx="52" cy="150" r="4"/><circle cx="100" cy="92" r="4"/><circle cx="150" cy="56" r="4"/></g>
  <text x="60" y="44" class="d-fix">same quality, a fraction of the cost</text>

  <path d="M56 160 C 120 140, 220 122, 380 116" fill="none" stroke="var(--muted)"
        stroke-width="2" stroke-dasharray="4 4" stroke-linecap="round"/>
  <g fill="var(--muted)"><circle cx="56" cy="160" r="4"/><circle cx="200" cy="126" r="4"/><circle cx="380" cy="116" r="4"/></g>
  <text x="256" y="136" class="d-label">expensive max, mid quality</text>

  <line x1="150" y1="56" x2="300" y2="48" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="0" y="212" class="d-label">shape only &#8212; benchmarks don't represent your work, so re-test on it</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/SF1Ab0Y-9BY",
        "channel": "Matt Pocock",
        "title": "Don't know which model to choose? *taps the graph*",
        "duration": "1:37",
    },
}
