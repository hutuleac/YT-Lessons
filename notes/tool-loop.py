NOTE = {
    "id": "tool-loop",
    "concept": "How a tool call actually runs",
    "one_liner": "A tool call is only a message asking for something — your code executes it and"
                 " sends the result back, and that four-step loop is the whole of how coding"
                 " agents touch your machine.",
    "prerequisites": ["message-anatomy"],
    "related": ["tool-overload", "agents-vs-workflows"],

    "skeleton": [
        "Tools are declared in the system prompt: name, description, JSON schema.",
        "The model emits a tool call — an instruction, not an action.",
        "Your code executes it. Nothing has happened until you do.",
        "Send the result back with the same id, errors included.",
    ],

    "mechanism": [
        "Tools reach the model through the system prompt. Each one supplies three things: a name,"
        " a description, and its parameters typed in JSON schema — so anything JSON schema"
        " supports, including objects and arrays. Those definitions are injected at the top and"
        " everything else in your system prompt sits below them. There is nothing clever"
        " happening: tool definitions are text in a message.",

        "When the user asks for something, the model replies with an assistant message containing"
        " a tool call: an id, the tool name, and the arguments. You never say which tool to use —"
        " the model chooses. And this is the step most people get wrong: at that point nothing has"
        " happened. The model has produced a message, not an effect.",

        "Execution is yours. For every tool named in the system prompt there must be a matching"
        " function in your codebase, and that function is what actually writes the file. You then"
        " send a result back carrying the same id as the call. Errors go back too, and Pocock is"
        " emphatic about that: the model can only do something different if it can see what went"
        " wrong.",

        "The model then reads the whole history — definitions, request, call, result — and replies"
        " with a summary. That loop is all a coding agent is. It explains both the power and the"
        " limits: the model can only ask, and your side decides what asking is allowed to do.",
    ],

    "numbers": [],

    "analogy": {
        "text": "The tool call is the LLM asking us for something, and the tool result is us"
                " giving it the information it needs.",
        "note": "Once tools are a conversation rather than a function call, error handling stops"
                " being an edge case — a failure is just another thing you tell it.",
    },

    "practice": [
        "Always return tool errors to the model; a swallowed error leaves it repeating the failure.",
        "Write tool descriptions for the model, not for your team — it picks from them.",
        "Keep one executable function per declared tool, or the model will call something that isn't there.",
        "Remember nothing runs until your code runs it — that boundary is where you put permissions.",
    ],

    "diagrams": [
        {
            "title": "The four-step loop",
            "caption": "Definitions go up in the system prompt; the call comes back; you execute;"
                       " the result returns with the same id. Everything else is repetition.",
            "svg": '''<svg viewBox="0 0 520 216" role="img"
  aria-label="A loop between the LLM and your machine: tool definitions in the system prompt, a tool call from the model, execution on your machine, and a tool result sent back with the same id.">
  <rect x="0" y="18" width="180" height="52" rx="6" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="90" y="42" class="d-node" text-anchor="middle">LLM</text>
  <text x="90" y="60" class="d-label" text-anchor="middle">decides which tool</text>

  <rect x="340" y="18" width="180" height="52" rx="6" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="430" y="42" class="d-node" text-anchor="middle">your machine</text>
  <text x="430" y="60" class="d-label" text-anchor="middle">executes it</text>

  <path d="M180 34 H336" stroke="var(--interference)" stroke-width="1.6" fill="none" marker-end="url(#ar)"/>
  <path d="M340 58 H184" stroke="var(--signal)" stroke-width="1.6" fill="none" marker-end="url(#ar2)"/>
  <defs>
    <marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto">
      <path d="M0 0 L6 3 L0 6 z" fill="var(--interference)"/>
    </marker>
    <marker id="ar2" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto">
      <path d="M0 0 L6 3 L0 6 z" fill="var(--signal)"/>
    </marker>
  </defs>
  <text x="258" y="28" class="d-label" text-anchor="middle">tool call &#183; id_42</text>
  <text x="258" y="76" class="d-label" text-anchor="middle">tool result &#183; id_42</text>

  <rect x="0" y="108" width="520" height="34" rx="4" fill="var(--interference)" opacity="0.22" stroke="var(--line)"/>
  <text x="12" y="130" class="d-label">SYSTEM PROMPT</text>
  <text x="150" y="130" class="d-node">write_file &#183; { path: string, content: string }</text>

  <text x="0" y="168" class="d-label">1. define &#8594; 2. model asks &#8594; 3. you execute &#8594; 4. you answer, errors included</text>
  <text x="0" y="192" class="d-label">nothing happens at step 2 &#8212; a tool call is a message, not an effect</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/V94BUC1kop8",
        "channel": "Matt Pocock",
        "title": "How LLM tools work under the hood",
        "duration": "2:51",
    },
}
