LESSON = {
    "id": "llm-fundamentals",
    "title": "What is actually happening when you talk to an LLM",
    "subject": "LLM fundamentals",
    "standfirst": "Six shorts that take the whole stack apart in order: tokens, then messages,"
                  " then the window they live in, then tools, then the two ways of chaining calls"
                  " together. Nothing here is magic once you have seen the list.",
    "audience": "You use LLMs daily through an API or a coding agent and have never seen the raw"
                " request that goes over the wire.",

    "notes": [
        "tokens",
        "message-anatomy",
        "context-window",
        "tool-loop",
        "structured-output",
        "agents-vs-workflows",
        "prompt-injection",
    ],

    "bridges": {
        "message-anatomy": "Tokens are the unit. The next question is what shape they arrive in —"
                           " because a conversation is a data structure, not a chat.",
        "context-window": "Messages accumulate, and they all compete for the same pool. That pool"
                          " has a hard edge and a soft one, and the soft one hurts more.",
        "tool-loop": "So far the model only produces text. Tools are how it reaches your machine"
                     " — and they are built out of the same messages you have just seen.",
        "structured-output": "Tools make the model ask for things. The mirror image is making the"
                             " model hand things back in a shape you specified.",
        "prompt-injection": "Everything so far assumes the messages say what you think they"
                             " say. Retrieved content is a message part too, and it can carry"
                             " instructions of its own.",
        "agents-vs-workflows": "One call is one call. Chain several and you have built either a"
                               " workflow or an agent, and the difference is smaller than the"
                               " vocabulary suggests.",
    },

    "closing": {
        "title": "It is a list of messages, all the way down",
        "body": "Encode to tokens, append messages, watch the pool, let the model ask for things,"
                " give it results. Reasoning, files, tool calls and agents are all the same"
                " structure with different parts in it. Once that clicks, the interesting"
                " questions stop being 'how does this work' and start being 'what should I put in"
                " the window'.",
    },
}
