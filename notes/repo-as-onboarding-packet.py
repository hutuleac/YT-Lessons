NOTE = {
    "id": "repo-as-onboarding-packet",
    "concept": "The repo as an onboarding packet",
    "one_liner": "Give an agent the same things you'd give a new hire — a workspace, and written"
                 " context about the business — instead of re-explaining the project in every"
                 " prompt."
                 ,

    "prerequisites": [],
    "related": ["grooming-skill", "codebase-as-environment"],

    "skeleton": [
        "A repo is a workspace. Folders and files are what an employee gets on day one.",
        "/context, /customers, /demos, /routines — the business, not just the code.",
        "claude.md: how to work. roadmap.md: what matters now. review.md: what good looks like.",
        "The project explains itself, so you stop re-explaining it every session.",
    ],

    "mechanism": [
        "An agent that only sees code has no way to know who the product is for, what's already"
        " been tried, or what counts as done. The fix demonstrated here is structural, not"
        " conversational: a folder layout that separates product code (/app) from business"
        " context (/context), sales input (/customers), and recurring work (/routines), plus"
        " three root files that carry the parts a codebase alone can't — claude.md for working"
        " style, roadmap.md for the current goal and what's explicitly out of scope, and review.md"
        " for the standard changes get judged against.",

        "The payoff is that this context persists across sessions without being retyped. A prompt"
        " like 'improve the landing page hero' can point at claude.md, roadmap.md, review.md and"
        " the latest customer notes instead of re-explaining the buyer, the pain, and the quality"
        " bar from scratch — the files carry that weight instead of the prompt.",

        "The scaffolding itself is meant to be set up by the agent, not typed out by hand: describe"
        " the product, the buyer, the pain, the promise, and the current goal in one message, and"
        " let it draft the files and ask clarifying questions for anything that would materially"
        " change the setup.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "Before asking an agent to build anything, give it a claude.md, roadmap.md, and review.md"
        " — even a rough first draft beats none.",
        "Put customer language, objections, and notes in a dedicated folder the agent can read,"
        " not just in your head.",
        "State what's explicitly out of scope in roadmap.md — it keeps the agent from padding a"
        " small task with unrequested features.",
    ],

    "diagrams": [
        {
            "title": "The workspace an agent actually needs",
            "caption": "Product code is one folder among several — the rest is what a new hire"
                       " would otherwise have to ask you for.",
            "svg": '''<svg viewBox="0 0 460 230" role="img"
  aria-label="A repo tree with five folders — app, context, customers, demos, routines — and three root files — claude.md for working style, roadmap.md for current goal, review.md for quality standard.">
  <text x="0" y="14" class="d-label">/repo</text>

  <rect x="20" y="24" width="120" height="26" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="80" y="41" class="d-node" text-anchor="middle">/app</text>
  <text x="150" y="41" class="d-label">the product code</text>

  <rect x="20" y="56" width="120" height="26" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="80" y="73" class="d-node" text-anchor="middle">/context</text>
  <text x="150" y="73" class="d-label">the business brain</text>

  <rect x="20" y="88" width="120" height="26" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="80" y="105" class="d-node" text-anchor="middle">/customers</text>
  <text x="150" y="105" class="d-label">calls, notes, objections</text>

  <rect x="20" y="120" width="120" height="26" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="80" y="137" class="d-node" text-anchor="middle">/demos</text>
  <text x="150" y="137" class="d-label">loom scripts, screenshots</text>

  <rect x="20" y="152" width="120" height="26" rx="4" fill="var(--signal)" opacity="0.35"/>
  <text x="80" y="169" class="d-node" text-anchor="middle">/routines</text>
  <text x="150" y="169" class="d-label">recurring prompts</text>

  <text x="20" y="196" class="d-fix">claude.md &#8594; how to work</text>
  <text x="20" y="212" class="d-fix">roadmap.md &#8594; what matters now</text>
  <text x="20" y="228" class="d-fix">review.md &#8594; what good looks like</text>
</svg>''',
        },
    ],

    "source": {
        "url": "https://www.youtube.com/watch?v=SkY-tR9kf-k",
        "channel": "Greg Isenberg",
        "title": "Claude Code New Features, Explained",
        "duration": "48:10",
    },
}
