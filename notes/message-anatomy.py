NOTE = {
    "id": "message-anatomy",
    "concept": "What a conversation actually is",
    "one_liner": "A conversation with an LLM is a list of messages with roles — system, user,"
                 " assistant — and each message can carry several parts, which is how reasoning,"
                 " files and tool calls all fit into the same structure.",
    "prerequisites": ["tokens"],
    "related": ["context-window", "tool-loop"],

    "skeleton": [
        "A conversation is a list of messages, each with a role.",
        "User messages are yours; the model's are called assistant messages.",
        "A system prompt is a message at the very start, usually hidden from the user.",
        "One message can hold several parts: text, reasoning, files, tool calls.",
    ],

    "mechanism": [
        "The bare structure is a list. User messages are the ones you send; the model's replies"
        " are assistant messages. That is the whole conversation when you talk to a raw model.",

        "A system prompt is not a separate mechanism — it is just a message placed at the very"
        " start of the history, visible to the model but usually not to the user. It is also"
        " where customisation lives, and in a conflict the model will usually follow the system"
        " prompt over the user: told to answer in Morse code, it keeps answering in Morse code"
        " even when you ask it to stop. Pocock is careful to hedge this — jailbreaks are common,"
        " so this is the theory rather than a guarantee.",

        "The part that unlocks everything else is that a message can contain multiple parts."
        " Reasoning tokens, where the model appears to think before answering, are simply another"
        " part of the assistant message. File parts work the same way in both directions: attach a"
        " PDF to a user message and ask for a summary, or receive a generated image back as a part"
        " of the reply.",

        "Tool calls reuse the same idea. The assistant emits a tool call part carrying an id and"
        " arguments; your system executes it and sends back a tool result with the matching id."
        " Nothing new is added to the protocol — it is still a list of messages made of parts,"
        " which is why one mental model covers chat, reasoning, files and agents alike.",
    ],

    "numbers": [],

    "analogy": {
        "text": "A tool call is the LLM asking your system for something, and the tool result is"
                " you giving it the information it needed.",
        "note": "Framing it as a conversation rather than a function call explains why the ids"
                " have to match and why results go back into the history rather than into the"
                " model directly.",
    },

    "practice": [
        "Put behaviour you want to persist in the system prompt, not in a first user message.",
        "Expect the system prompt to win conflicts with the user — design for that, don't rely on it.",
        "Treat reasoning, files and tool calls as message parts; they all cost context.",
        "Match tool result ids to tool call ids — the pairing is what makes the loop work.",
    ],

    "diagrams": [
        {
            "title": "One structure, four kinds of part",
            "caption": "System first, then an alternating history. Reasoning, files and tool calls"
                       " are parts inside a message rather than separate channels.",
            "svg": '''<svg viewBox="0 0 460 236" role="img"
  aria-label="A message list: a system message at the top, then a user message, then an assistant message containing a reasoning part and a text part, then a user message with a file part, then an assistant message with a tool call part.">
  <rect x="0" y="0" width="460" height="34" rx="4" fill="var(--interference)" opacity="0.25" stroke="var(--line)"/>
  <text x="12" y="22" class="d-label">SYSTEM</text>
  <text x="96" y="22" class="d-node">you are a helpful assistant &#183; tool definitions</text>

  <rect x="0" y="44" width="300" height="30" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="12" y="64" class="d-label">USER</text>
  <text x="72" y="64" class="d-node">summarise this</text>
  <rect x="204" y="50" width="88" height="18" rx="3" fill="var(--sand)" opacity="0.5"/>
  <text x="248" y="63" class="d-label" text-anchor="middle">file part</text>

  <rect x="70" y="84" width="390" height="48" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="82" y="104" class="d-label">ASSISTANT</text>
  <rect x="172" y="92" width="120" height="18" rx="3" fill="var(--signal)" opacity="0.4"/>
  <text x="232" y="105" class="d-label" text-anchor="middle">reasoning part</text>
  <rect x="300" y="92" width="90" height="18" rx="3" fill="var(--signal)" opacity="0.4"/>
  <text x="345" y="105" class="d-label" text-anchor="middle">text part</text>
  <text x="82" y="124" class="d-node">"here is the summary&#8230;"</text>

  <rect x="70" y="142" width="390" height="34" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="82" y="164" class="d-label">ASSISTANT</text>
  <rect x="172" y="150" width="140" height="18" rx="3" fill="var(--signal)" opacity="0.4"/>
  <text x="242" y="163" class="d-label" text-anchor="middle">tool call &#183; id_42</text>

  <rect x="0" y="186" width="300" height="34" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="12" y="208" class="d-label">TOOL</text>
  <rect x="72" y="194" width="150" height="18" rx="3" fill="var(--sand)" opacity="0.5"/>
  <text x="147" y="207" class="d-label" text-anchor="middle">result &#183; same id_42</text>

  <text x="0" y="232" class="d-label">the history is one list &#8212; everything above is a message with parts</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/WwRE-SKdmKs",
        "channel": "Matt Pocock",
        "title": "What messages you send to the LLM actually look like",
        "duration": "2:19",
    },
}
