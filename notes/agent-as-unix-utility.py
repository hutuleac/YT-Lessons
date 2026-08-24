NOTE = {
    "id": "agent-as-unix-utility",
    "concept": "A super intelligent Unix utility",
    "one_liner": "Run the agent headless with a prompt in and structured data out, and it stops"
                 " being an app you sit in front of — it becomes a filter you can put in the"
                 " middle of any pipeline.",

    "prerequisites": [],
    "related": ["structured-output", "scheduled-routines", "single-job-agents"],

    "skeleton": [
        "Non-interactive mode takes a prompt and returns an answer, no session, no UI.",
        "Ask for JSON and the output is parseable by whatever runs next.",
        "It reads stdin, so anything you can pipe becomes its input.",
        "That makes it composable: CI steps, incident response, log triage.",
        "The allowed tool list is what makes an unattended run safe to leave alone.",
    ],

    "mechanism": [
        "The interactive terminal session is the visible half of the product. The other half is"
        " the same engine with no interface: a prompt goes in as an argument, the answer comes"
        " back on stdout. Boris Cherny points out this is not a lesser mode — it is exactly what"
        " the interactive tool is built on, exposed for you to build on too.",

        "Two properties turn that into composability. It reads standard input, so the output of"
        " any command — git status, a log pulled from a bucket, the output of a Sentry CLI — can"
        " be piped in as material. And it can emit structured output rather than prose, so"
        " whatever runs next can parse it instead of scraping it. Prose out would make the agent"
        " a terminus; JSON out makes it a stage.",

        "That is the whole Unix argument applied to a model: a program that reads a stream and"
        " writes a stream can be inserted anywhere in a chain without the chain knowing what it"
        " is. Cherny's examples are the ones you would expect from that framing — running it in"
        " CI, using it in incident response, handing it a giant log and asking what is"
        " interesting about it — and he is explicit that this is unexplored ground rather than a"
        " settled pattern.",

        "The constraint that makes it usable unattended is the allowed tool list. A headless run"
        " has nobody to approve anything, so what it is permitted to do has to be decided up"
        " front and passed in with the prompt. (The flags and the SDK's packaging have changed"
        " since the talk; the prompt-in, structured-data-out shape is the durable part.)",
    ],

    "numbers": [],

    "analogy": {
        "text": "It's sort of this new idea. It's like a super intelligent Unix utility. You give"
                " it a prompt, it gives you JSON.",
        "note": "It sets the expectation correctly: not an assistant you converse with, but a"
                " filter with a contract — and filters are things you compose, schedule, and put"
                " in CI without watching them.",
    },

    "practice": [
        "Run the agent headless with a prompt argument the next time you would have opened a REPL"
        " for a one-shot question.",
        "Ask for structured output whenever something downstream will read the result.",
        "Pipe the input in rather than describing it — a log, a diff, a status output.",
        "Pass an explicit allowed-tools list for anything running unattended.",
        "Look at your existing scripts for a step that fails because it needs judgment; that step"
        " is the candidate.",
    ],

    "diagrams": [
        {
            "title": "Terminus versus stage",
            "caption": "Prose output ends the chain. Structured output puts the agent in the"
                       " middle of one.",
            "svg": '''<svg viewBox="0 0 520 210" role="img"
  aria-label="Two pipelines. In the first, a command feeds an interactive agent session which produces prose that a human reads, ending the chain. In the second, a command pipes into a headless agent run with an allowed tool list, which emits JSON that flows into jq and then into a downstream job such as CI or an alert.">
  <text x="0" y="14" class="d-label">INTERACTIVE</text>
  <rect x="0" y="24" width="90" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="8" y="44" class="d-node">a command</text>
  <path d="M90 39 H120" fill="none" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="120" y="24" width="75" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="128" y="44" class="d-node">session</text>
  <path d="M195 39 H225" fill="none" stroke="var(--line)" stroke-width="1.5"/>
  <rect x="225" y="24" width="130" height="30" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="233" y="44" class="d-node">prose &#8594; a human</text>
  <text x="370" y="44" class="d-fix">chain ends</text>

  <text x="0" y="104" class="d-label">HEADLESS</text>
  <rect x="0" y="114" width="110" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="8" y="134" class="d-node">stdin: a log</text>
  <path d="M110 129 H140" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="140" y="114" width="125" height="30" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="148" y="134" class="d-node">prompt + tools</text>
  <path d="M265 129 H295" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="295" y="114" width="65" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="303" y="134" class="d-node">JSON</text>
  <path d="M360 129 H390" fill="none" stroke="var(--signal)" stroke-width="1.5"/>
  <rect x="390" y="114" width="115" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="398" y="134" class="d-node">CI, next job</text>

  <text x="0" y="180" class="d-fix">same engine &#8212; the difference is who reads the output</text>
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
