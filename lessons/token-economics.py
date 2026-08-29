LESSON = {
    "id": "token-economics",
    "title": "The bill is mostly about timing, not brevity",
    "subject": "Token economics",
    "standfirst": "A rule to \"be brief\" only trims output tokens. The real 20x swing in your"
                  " bill comes from something else: did your message land inside the 1-hour cache"
                  " window, or miss it.",
    "audience": "You use Claude Code or a similar agent, and your usage cost has spiked without a"
                " clear reason: a long idle gap, a model switch, or a long session that suddenly"
                " gets expensive.",

    "notes": [
        "prompt-caching",
        "cache-loss-recovery",
        "rewind-not-forward",
        "advisor-mode",
    ],

    "bridges": {
        "cache-loss-recovery": "The cache has a 1-hour fuse. What do you send once it burns out"
                               " — or before it does?",
        "rewind-not-forward": "Those three moves are for when the cache is already gone. A"
                              " broken output is a different problem, and it has the same"
                              " answer: go back, don't build forward on top of the mistake.",
        "advisor-mode": "Those moves all deal with a cache or a bad turn after the fact. The"
                        " other lever stops expensive history from building up in the first"
                        " place: send fewer turns through the expensive model to begin with.",
    },

    "closing": {
        "title": "Timing beats trimming",
        "body": "A \"be brief\" rule only trims output tokens, a small line item. Prompt caching"
                " sets the price of your whole input history, and it swings 20x on timing alone:"
                " inside the hour, or outside it. Keep the cache warm while you work. Have a plan"
                " for when it is gone. Send cheap steps to a cheap model.",
    },
}
