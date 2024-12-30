## add settings

length = 0      # 0 for short, 1 for medium, 2 for long ?


def debate_prompt(topic, side):
    """Generates a prompt for a debate on a given topic."""
    return f"""
You are an AI debating on the topic: "{topic}". Your role is to argue from the perspective of {side}.
Focus on providing three strong points to support your argument, backed by logic, ethical considerations, and real-world examples.
Be concise and avoid repeating arguments already presented.
"""
