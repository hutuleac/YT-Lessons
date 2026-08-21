NOTE = {
    "id": "agent-eyes",
    "concept": "Give the agent eyes",
    "one_liner": "An agent that only edits files can't tell you a form is awkward or a headline"
                 " misses the buyer's pain — having it open, click through, and judge its own"
                 " work closes a loop that reading code alone can't."
                 ,

    "prerequisites": [],
    "related": ["review-triage"],

    "skeleton": [
        "A landing page can load fine and still feel confusing. Code review won't catch that.",
        "Eyes means: open it, click through it, check console and network, judge it as a user.",
        "Ask it to judge from a named persona's first five seconds, not just \"does it work.\"",
        "Then make one focused pass on the highest-impact issue it finds — not a rewrite.",
    ],

    "mechanism": [
        "Most of what makes a product page bad is invisible to a diff: a form that submits but"
        " feels awkward, a button that's present but easy to miss, a headline that's accurate but"
        " misses the buyer's actual pain. None of that shows up by reading changed lines — it only"
        " shows up by using the thing the way a customer would.",

        "The fix is to have the agent run its own QA pass after it builds: open the page in"
        " preview, test the empty-submit case, check what happens after a real submission,"
        " inspect console and network for errors, and — this is the part reading code can't"
        " do — evaluate the experience from a named perspective, like 'a med spa owner seeing"
        " this for the first time.' That framing is what surfaces something like a form asking"
        " for an email with no reassurance about spam, which is a trust problem, not a bug.",

        "The instruction that keeps this useful rather than open-ended is to end with one focused"
        " fix on the single highest-impact issue found, not a general cleanup pass — the same"
        " discipline that makes a ticket reviewable applies to the fix that comes out of testing"
        " it.",
    ],

    "numbers": [],

    "analogy": None,

    "practice": [
        "After a build, have the agent open the app and use it — not just check that it compiles.",
        "Frame the check as a specific persona's first experience, not a generic \"does this work.\"",
        "Ask it to check console and network errors alongside the visual walkthrough.",
        "Limit the follow-up fix to the single highest-impact issue it surfaces.",
    ],

    "diagrams": [
        {
            "title": "What a diff can't see",
            "caption": "The code is correct on both sides — only using the product surfaces the"
                       " real problem.",
            "svg": '''<svg viewBox="0 0 460 150" role="img"
  aria-label="A code diff shows the form code is correctly added, marked as passing. Only opening the app and testing as a first-time visitor surfaces the actual issue: no reassurance about spam next to the email field, the real friction point.">
  <text x="0" y="14" class="d-label">CODE DIFF</text>
  <rect x="0" y="24" width="200" height="40" rx="4" fill="var(--surface-2)" stroke="var(--line)"/>
  <text x="10" y="42" class="d-label">+ &lt;form&gt; email field</text>
  <text x="10" y="56" class="d-label">+ &lt;button&gt; join waitlist</text>
  <text x="0" y="82" class="d-fix">reads clean &#8212; nothing wrong here</text>

  <text x="260" y="14" class="d-label">USING THE PAGE</text>
  <rect x="260" y="24" width="200" height="40" rx="4" fill="var(--interference)" opacity="0.4"/>
  <text x="270" y="42" class="d-label">email field, no context</text>
  <text x="270" y="56" class="d-label">"will I get spam?"</text>
  <text x="260" y="82" class="d-fix">the actual friction point</text>

  <text x="0" y="118" class="d-label">Same commit &#8212; only one of these catches the real problem.</text>
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
