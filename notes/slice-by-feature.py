NOTE = {
    "id": "slice-by-feature",
    "concept": "Slice tickets by feature, not by layer",
    "one_liner": "Group tickets by feature — login, checkout — instead of by layer — database,"
                 " API, UI — so each ticket lands as something you can actually test end to end."
                 ,

    "prerequisites": [],
    "related": ["spec-without-code", "review-checkpoints"],

    "skeleton": [
        "Traditional slicing: ticket 1 database, ticket 2 API, ticket 3 UI.",
        "After ticket 1, all you have is a database — nothing to test.",
        "Feature slicing: ticket 1 is the whole login page, top to bottom.",
        "Each ticket finishes as a working, testable feature.",
    ],

    "mechanism": [
        "Once a spec exists, it has to be broken into tickets an agent can pick up one at a time."
        " The default most spec-driven frameworks use is to slice by layer: one ticket for the"
        " database schema, one for the API, one for the UI. That grouping mirrors how a team is"
        " often organised, but it has a specific cost for agent-driven work — after the database"
        " ticket ships, the only thing that exists is a database. There is nothing to run, click,"
        " or test until the API and UI tickets land too.",

        "Slicing by feature instead means ticket one is the login page end to end: its schema, its"
        " endpoint, its UI, all in one ticket. The payoff is that each ticket is a fully functional"
        " slice the moment it merges — it can be tested for real, not just reviewed as a diff. That"
        " also keeps the application modular: a later change to how login works touches one"
        " feature's ticket, not a layer shared by every feature in the app.",

        "This is the same shift in checkpoint placement as [[review-checkpoints]] applied to how"
        " work gets divided rather than when it gets reviewed — smaller, self-contained units are"
        " easier to verify and easier to change without touching everything else.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "When breaking a spec into tickets, ask \"can I test this alone once it's done?\" — if not,"
        " it's a layer slice, not a feature slice.",
        "Keep a feature's schema, endpoint, and UI in the same ticket rather than splitting them"
        " across a database ticket and a UI ticket.",
        "Expect each finished ticket to be runnable, not just reviewable.",
    ],

    "diagrams": [
        {
            "title": "What exists after ticket one ships",
            "caption": "By layer, one ticket in, you have a database and nothing to click. By"
                       " feature, one ticket in, you have a working login page.",
            "svg": '''<svg viewBox="0 0 480 200" role="img"
  aria-label="Two ways of slicing three tickets. By layer: ticket one is database, ticket two is API, ticket three is UI — after ticket one, only a database exists, nothing testable. By feature: ticket one is the full login feature end to end, immediately testable; ticket two and three are the next features.">
  <text x="0" y="14" class="d-label">BY LAYER</text>
  <rect x="0" y="24" width="90" height="34" rx="4" fill="var(--interference)" opacity="0.45"/>
  <text x="45" y="46" class="d-label" text-anchor="middle">database</text>
  <rect x="98" y="24" width="90" height="34" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="143" y="46" class="d-label" text-anchor="middle">API</text>
  <rect x="196" y="24" width="90" height="34" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="241" y="46" class="d-label" text-anchor="middle">UI</text>
  <text x="300" y="46" class="d-fix">nothing to test yet</text>

  <text x="0" y="98" class="d-label">BY FEATURE</text>
  <rect x="0" y="108" width="188" height="46" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="94" y="128" class="d-node" text-anchor="middle">login: db + API + UI</text>
  <text x="94" y="145" class="d-label" text-anchor="middle">ticket 1</text>
  <text x="200" y="132" class="d-fix">works end to end</text>

  <rect x="0" y="164" width="188" height="26" rx="4" fill="var(--surface-2)" stroke="var(--muted)" stroke-dasharray="3 3"/>
  <text x="94" y="181" class="d-label" text-anchor="middle">next feature: ticket 2</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=8D8ewFBJfFM",
        "channel": "Eric Tech",
        "title": "Matt Pocock's Claude Code Skills Beat Superpowers Now",
        "duration": "24:17",
    },
}
