NOTE = {
    "id": "hallucination-types",
    "concept": "Factuality vs faithfulness",
    "one_liner": "One question splits every hallucination into two kinds with two different"
                 " fixes: was the information in the context window at all?",
    "prerequisites": ["dumb-zone"],
    "related": ["dumb-zone"],

    "skeleton": [
        "Hallucinations are probably inherent to LLMs. Diagnose, don't hope.",
        "Ask one question: was the information in context?",
        "It wasn't → factuality. The model was recalling. Load the information.",
        "It was → faithfulness. The model drifted. Get out of the dumb zone.",
    ],

    "mechanism": [
        "The diagnosis starts with a correction about what a model is. People treat them as"
        " databases that store and retrieve, and that is the wrong model entirely.",

        "If the information was never in context, this is a factuality hallucination — the model"
        " was reaching for something you never gave it, and failed. The fix is the obvious one:"
        " load the information into context. The rule this implies is blunt. Never trust an"
        " unsourced LLM.",

        "The harder case is when you did pass the right context and it still went wrong. That is a"
        " faithfulness hallucination: the model was unfaithful to material it actually had. The"
        " usual cause is attention degradation — the window grew long, the attention relationships"
        " got strained, and it lost the thread.",

        "Which makes the cure structural rather than a matter of prompting harder. You are in the"
        " dumb zone, so the fix is to leave it: clear the context, run compact, or hand the work"
        " to a fresh session. And it works in reverse as a diagnostic — persistent faithfulness"
        " hallucinations are good evidence you are already deep in the window.",
    ],

    "numbers": [],

    "analogy": {
        "text": "It's more like they have a fuzzy JPEG of the entirety of human knowledge.",
        "note": "They know the basic shapes of things and cannot give you specifics — which is"
                " exactly the failure mode you see when a model invents a plausible API that"
                " does not exist.",
    },

    "practice": [
        "Before fixing anything, check whether the information was ever in the context window.",
        "Factuality: load the source. Never trust an unsourced answer.",
        "Faithfulness: clear, compact, or hand off — don't re-prompt into the same long window.",
        "Read repeated faithfulness failures as a dumb-zone signal, not a model-quality signal.",
    ],

    "diagrams": [
        {
            "title": "One question, two hallucinations",
            "caption": "The split is diagnostic, not academic — the two branches have entirely"
                       " different fixes, and re-prompting only helps on the left.",
            "svg": '''<svg viewBox="0 0 420 232" role="img"
  aria-label="Decision tree. Starting from a hallucination, ask whether the information was in the context window. If no, it is a factuality hallucination, fixed by loading the information. If yes, it is a faithfulness hallucination, fixed by leaving the dumb zone.">
  <rect x="128" y="4" width="164" height="34" rx="17" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="210" y="26" class="d-node" text-anchor="middle">a hallucination</text>

  <path d="M210 38 L210 58" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="104" y="58" width="212" height="34" rx="6" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>
  <text x="210" y="80" class="d-node" text-anchor="middle">was it in the context window?</text>

  <path d="M120 92 L120 118 M120 92 L210 92" stroke="var(--line)" stroke-width="1.5" fill="none"/>
  <path d="M300 92 L300 118 M300 92 L210 92" stroke="var(--line)" stroke-width="1.5" fill="none"/>
  <text x="104" y="110" class="d-label" text-anchor="end">no</text>
  <text x="316" y="110" class="d-label">yes</text>

  <rect x="14" y="118" width="196" height="42" rx="6" fill="var(--surface-2)" stroke="var(--interference)"/>
  <text x="112" y="136" class="d-node" text-anchor="middle">factuality</text>
  <text x="112" y="152" class="d-label" text-anchor="middle">it was recalling, and failed</text>

  <rect x="212" y="118" width="196" height="42" rx="6" fill="var(--surface-2)" stroke="var(--interference)"/>
  <text x="310" y="136" class="d-node" text-anchor="middle">faithfulness</text>
  <text x="310" y="152" class="d-label" text-anchor="middle">it had the material, drifted</text>

  <path d="M112 160 L112 180" stroke="var(--signal)" stroke-width="1.5"/>
  <path d="M310 160 L310 180" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="14" y="180" width="196" height="40" rx="6" fill="none" stroke="var(--signal)"/>
  <text x="112" y="205" class="d-fix" text-anchor="middle">load the information</text>
  <rect x="212" y="180" width="196" height="40" rx="6" fill="none" stroke="var(--signal)"/>
  <text x="310" y="199" class="d-fix" text-anchor="middle">leave the dumb zone</text>
  <text x="310" y="213" class="d-label" text-anchor="middle">clear · compact · hand off</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/H-JHumbpORI",
        "channel": "Matt Pocock",
        "title": "My agent hallucinated - what do I do?",
        "duration": "1:32",
    },
}
