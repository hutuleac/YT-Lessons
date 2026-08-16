NOTE = {
    "id": "tokens",
    "concept": "Tokens, encoding and decoding",
    "one_liner": "A model never sees your text — it is encoded into numeric tokens, thought about"
                 " as tokens, and decoded back into text, which is why tokens are also the unit"
                 " you are billed in.",
    "prerequisites": [],
    "related": ["context-window", "message-anatomy"],

    "skeleton": [
        "The model never reads your text. It reads numbers.",
        "Input text is encoded into tokens before the model sees it.",
        "Output tokens are decoded back into text as they are produced.",
        "You are billed in input and output tokens because that is the real unit.",
    ],

    "mechanism": [
        "Pass the word \"hello\" to an LLM and the model does not receive those five letters. The"
        " text is encoded into a token — a number — and it is the number that enters the model."
        " Everything the model does downstream happens in that numeric space.",

        "The return trip is the mirror image. The model produces output tokens, which are decoded"
        " back into text, and the decoding happens as they arrive rather than at the end. So the"
        " whole loop is: text in, encode, model, tokens out, decode, text out.",

        "That is why billing is denominated in input and output tokens rather than words or"
        " characters. Tokens are the closest available representation of what is actually"
        " happening inside the model, so they are the honest unit to count — and the unit every"
        " other limit in this lesson is expressed in.",
    ],

    "numbers": [],
    "analogy": None,

    "practice": [
        "Count tokens, not words, when you estimate cost or fit — they are what the API meters.",
        "Expect input and output tokens to be priced differently; check both before optimising.",
        "Treat any limit you meet (context window, rate limit, price) as a token limit.",
    ],

    "diagrams": [
        {
            "title": "Text in, tokens through the middle, text out",
            "caption": "Encoding and decoding are the only places text exists. The model itself"
                       " works entirely in numbers, which is what you are billed for.",
            "svg": '''<svg viewBox="0 0 520 132" role="img"
  aria-label="A pipeline: input text is encoded into input tokens, passed through the LLM, which produces output tokens that are decoded back into output text.">
  <rect x="0" y="30" width="92" height="44" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="46" y="57" class="d-node" text-anchor="middle">"hello"</text>
  <text x="46" y="92" class="d-label" text-anchor="middle">input text</text>

  <text x="104" y="57" class="d-label">encode &#8594;</text>

  <rect x="158" y="30" width="76" height="44" rx="4" fill="var(--signal)" opacity="0.45"/>
  <text x="196" y="57" class="d-num" text-anchor="middle">15339</text>
  <text x="196" y="92" class="d-label" text-anchor="middle">input tokens</text>

  <rect x="248" y="18" width="64" height="68" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="280" y="57" class="d-node" text-anchor="middle">LLM</text>

  <rect x="326" y="30" width="76" height="44" rx="4" fill="var(--signal)" opacity="0.45"/>
  <text x="364" y="57" class="d-num" text-anchor="middle">2748</text>
  <text x="364" y="92" class="d-label" text-anchor="middle">output tokens</text>

  <text x="412" y="57" class="d-label">decode &#8594;</text>

  <rect x="466" y="30" width="54" height="44" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="493" y="57" class="d-node" text-anchor="middle">"hi"</text>
  <text x="493" y="92" class="d-label" text-anchor="middle">text</text>

  <text x="0" y="122" class="d-label">billed on both token columns &#8212; the text at either end is just presentation</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/IVZ2OL8mU8c",
        "channel": "Matt Pocock",
        "title": "Most devs don't know how LLM tokens work",
        "duration": "0:49",
    },
}
