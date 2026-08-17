LESSON = {
    "id": "token-economics",
    "title": "The bill is mostly about timing, not brevity",
    "subject": "Token economics",
    "standfirst": "A tip to \"be brief\" saves you output tokens. The real 20x swing in what you"
                  " pay lives somewhere most people never look: whether your message lands inside"
                  " an hour-long cache window or misses it.",
    "audience": "You use Claude Code or a similar agent regularly and have noticed usage costs"
                " spike without an obvious reason — long idle gaps, model switches, or long"
                " sessions that suddenly get expensive.",

    "notes": [
        "prompt-caching",
        "cache-loss-recovery",
        "advisor-mode",
    ],

    "bridges": {
        "cache-loss-recovery": "The cache is the whole game, and it has a 1-hour fuse. So what do"
                               " you actually do once it's burned — or before it burns?",
        "advisor-mode": "Those three options all deal with a cache after the fact. The other"
                        " lever is not creating as much expensive history in the first place —"
                        " by not routing every token through the expensive model to begin with.",
    },

    "closing": {
        "title": "Timing beats trimming",
        "body": "A concise-output rule shaves output tokens, which are one line item. Prompt"
                " caching is the whole conversation's input cost, and it swings 20x on whether"
                " you sent your next message inside the hour or outside it — or whether you"
                " switched models, effort, or MCPs mid-session without meaning to. Protect the"
                " cache while you're using it, have a deliberate plan for when it's gone, and"
                " keep the expensive model out of steps a cheaper one can execute.",
    },
}
