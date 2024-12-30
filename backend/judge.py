

def get_judge_response(claude_model, debate_transcript, topic):
    """
    Gets a response from Claude to judge the debate.
    
    Args:
        api_key (str): The API key for Anthropic.
        debate_transcript (str): The debate transcript.
        topic (str): The topic of the debate.

    Returns:
        str: The judgment response from Claude.
    """

    # Define the system's evaluation instructions
    messages = [
        {
            "role": "assistant",
            "content": "You are an impartial judge evaluating debates based on logical soundness, relevance, and persuasion."
        },
        {
            "role": "user",
            "content": f"""
The following is a transcript of a debate between Pro and Con about the topic: "{topic}".
Evaluate the arguments made by both sides, considering logical soundness, relevance, and persuasion.
Provide a verdict on which side presented the stronger case, and explain your reasoning.

Debate Transcript:
{debate_transcript}

Which side presented the stronger argument and why?
"""
        },
    ]

    # Send the request to Claude
    response = claude_model.messages.create(
        model="claude-3-5-sonnet-20241022",  # Replace with your desired Claude model
        max_tokens=1024,
        messages=messages,
    )

    return response
