NOTE = {
    "id": "deletion-test",
    "concept": "The deletion test",
    "one_liner": "To find out if a function still earns its place, delete it and run the tests —"
                 " if nothing breaks, it wasn't load-bearing."
                 ,

    "prerequisites": [],
    "related": ["one-door", "docs-drift"],

    "skeleton": [
        "Pick a function the main program depends on.",
        "Delete it. Run the full test suite.",
        "Tests fail: it was a real dependency — keep it.",
        "Tests still pass: nothing needed it — delete it for real.",
    ],

    "mechanism": [
        "A codebase accumulates functions that stop being called anywhere except by a chain that"
        " no longer matters, and no amount of reading the code tells you for certain whether one"
        " of them is safe to remove — a reference could be hiding somewhere unglamorous. The"
        " deletion test turns that uncertainty into a fact by running an experiment instead of"
        " reasoning about it: delete the function, run every test, and see what happens.",

        "If the test suite fails, the function was a real dependency of the main program and goes"
        " back in — the failure itself is the proof it was doing work. If every test still passes"
        " with the function gone, that is proof in the other direction: nothing in the program's"
        " observable behaviour needed it, so it is dead weight kept alive only by its presence in"
        " the file, and it should be deleted for real, not just deleted in the experiment.",

        "This is the mechanical core of the architecture-review skill described alongside it: it"
        " walks a project's hot files, runs this test against candidate functions, and surfaces"
        " what to cut or unify — including duplicate functions that turned out to do the same"
        " thing and can be merged into one. It only works with a test suite that actually exercises"
        " the behaviour in question; a deletion test against thin or missing tests just proves the"
        " tests were incomplete, not that the function was unused.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Before deleting a function you suspect is dead, delete it and run the full suite rather"
        " than trusting a manual read of call sites.",
        "Treat a passing suite after deletion as the actual proof, not a hunch confirmed.",
        "If the deletion test doesn't feel trustworthy, that's a signal your test coverage has a"
        " gap, not that the function is safe.",
    ],

    "diagrams": [
        {
            "title": "Delete, then let the tests answer",
            "caption": "The experiment settles what reading the code can't.",
            "svg": '''<svg viewBox="0 0 520 170" role="img"
  aria-label="Flow: delete the function, run the test suite. If tests fail, keep the function because it was a real dependency. If tests still pass, delete it for real because nothing needed it.">
  <rect x="30" y="10" width="140" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="100" y="32" class="d-node" text-anchor="middle">delete function</text>
  <path d="M174 27 H216" stroke="var(--line)" stroke-width="1.4"/>
  <rect x="220" y="10" width="140" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="290" y="32" class="d-node" text-anchor="middle">run test suite</text>

  <path d="M290 44 V64" stroke="var(--line)" stroke-width="1.2"/>
  <path d="M290 64 H120 M290 64 H425" stroke="var(--line)" stroke-width="1.2"/>
  <path d="M120 64 V84 M425 64 V84" stroke="var(--line)" stroke-width="1.2"/>

  <rect x="40" y="84" width="160" height="36" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="120" y="103" class="d-label" text-anchor="middle">tests fail</text>
  <text x="120" y="134" class="d-fix" text-anchor="middle">keep it &#8212; real dependency</text>

  <rect x="350" y="84" width="150" height="36" rx="4" fill="var(--signal)" opacity="0.4"/>
  <text x="425" y="103" class="d-label" text-anchor="middle">tests pass</text>
  <text x="425" y="134" class="d-fix" text-anchor="middle">delete it &#8212; unused</text>
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
