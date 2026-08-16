NOTE = {
    "id": "structured-output",
    "concept": "Structured outputs",
    "one_liner": "The second thing models are good at is returning data that matches a schema you"
                 " supply, which turns an unstructured document into something you can put in a"
                 " database.",
    "prerequisites": ["tool-loop"],
    "related": ["message-anatomy"],

    "skeleton": [
        "Models produce structured data, not just text.",
        "You supply a schema; the model fills it.",
        "The schema goes to the model as JSON schema and validates the reply on the way back.",
        "Result: runtime-safe and type-safe in one step.",
    ],

    "mechanism": [
        "Most people only ask models for prose, which leaves the more useful half unused. Pocock's"
        " example is an invoice PDF: a text summary reads nicely but you cannot query it, so"
        " asking \"when did I last buy oranges\" is impossible until the data has a shape.",

        "The change is small in code — swap the generate-text call for a generate-object call and"
        " pass a schema describing what you want back: an array of items with name, quantity and"
        " price, a total, a currency. The schema does double duty. It is converted to JSON schema"
        " and handed to the model so the model's structured-output feature can constrain the"
        " reply, and it validates the response when it arrives.",

        "That is what makes the result trustworthy in two different senses at once. Validation"
        " gives runtime safety, so a malformed reply fails loudly instead of flowing into your"
        " database. Inference from the same schema gives compile-time types, so the object you"
        " handle downstream is typed without you writing the type twice.",
    ],

    "numbers": [],
    "analogy": None,

    "practice": [
        "Reach for structured output whenever the answer is going into storage, not onto a screen.",
        "Define the shape once and derive both the model's schema and your types from it.",
        "Validate the reply — structured output is a strong constraint, not a guarantee.",
        "Keep schemas narrow: ask for the fields you will use, not everything the document holds.",
    ],

    "diagrams": [
        {
            "title": "Same PDF, same model, two shapes of answer",
            "caption": "The schema is sent to the model as JSON schema and used again to validate"
                       " the reply, so one definition buys both runtime and type safety.",
            "svg": '''<svg viewBox="0 0 520 218" role="img"
  aria-label="An invoice PDF sent to a model twice. The generate-text path returns a paragraph that cannot be queried. The generate-object path, given a schema, returns a validated object with items, total and currency.">
  <rect x="0" y="70" width="86" height="52" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="43" y="92" class="d-node" text-anchor="middle">invoice</text>
  <text x="43" y="110" class="d-label" text-anchor="middle">.pdf</text>

  <path d="M86 84 H150" stroke="var(--line)" stroke-width="1.4" fill="none"/>
  <path d="M86 108 H150" stroke="var(--line)" stroke-width="1.4" fill="none"/>

  <rect x="152" y="18" width="140" height="72" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="222" y="44" class="d-label" text-anchor="middle">generateText</text>
  <text x="222" y="68" class="d-node" text-anchor="middle">"you spent &#8230;"</text>
  <text x="300" y="58" class="d-label">reads well, cannot be queried</text>

  <rect x="152" y="112" width="140" height="86" rx="4" fill="var(--surface-2)" stroke="var(--signal)"/>
  <text x="222" y="136" class="d-label" text-anchor="middle">generateObject</text>
  <rect x="164" y="144" width="116" height="18" rx="3" fill="var(--signal)" opacity="0.4"/>
  <text x="222" y="157" class="d-label" text-anchor="middle">items[ ]</text>
  <rect x="164" y="166" width="56" height="18" rx="3" fill="var(--signal)" opacity="0.4"/>
  <text x="192" y="179" class="d-label" text-anchor="middle">total</text>
  <rect x="224" y="166" width="56" height="18" rx="3" fill="var(--signal)" opacity="0.4"/>
  <text x="252" y="179" class="d-label" text-anchor="middle">currency</text>

  <rect x="330" y="112" width="190" height="40" rx="4" fill="var(--sand)" opacity="0.35"/>
  <text x="425" y="137" class="d-label" text-anchor="middle">out: schema as JSON schema</text>
  <rect x="330" y="158" width="190" height="40" rx="4" fill="var(--sand)" opacity="0.35"/>
  <text x="425" y="183" class="d-label" text-anchor="middle">back: schema validates it</text>

  <text x="0" y="14" class="d-label">one schema, used twice &#8212; once going out, once coming back</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/shorts/AFM2N9ifYFI",
        "channel": "Matt Pocock",
        "title": "Yes, LLM's can produce more than just text",
        "duration": "1:19",
    },
}
