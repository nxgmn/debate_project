from anthropic import Anthropic
from formatting import format_response_openai, format_response_claude, format_response_gemini
from judge import get_judge_response

def conduct_debate(openai_model, gemini_model, claude_model, topic):
    """Handles the interaction between OpenAI GPT and Gemini AI debating a topic with Claude as the judge"""
    side1, side2 = "Pro", "Con"
    turn_limit = 3  # Number of turns in the debate
    returning_transcript = ""
    # Initial prompts
    input1 = f"You are debating the topic: {topic}. Argue from the perspective of {side1}."
    input2 = f"You are debating the topic: {topic}. Argue from the perspective of {side2}."

    # Store arguments for evaluation
    debate_transcript = []

    for turn in range(turn_limit):
        returning_transcript += f"Turn {turn + 1}:\n"

        # OpenAI GPT generates a response
        response1 = openai_model.invoke([ {"role": "system", "content": "You are a debater arguing from the 'Pro' perspective."}, {"role": "system", "content": input1}])
        returning_transcript += "OpenAI GPT (Pro):" + format_response_openai(response1)

        # Claude AI generates a response
        input2 = f"OpenAI GPT argued: {response1}. Now argue from the {side2} perspective. Rebut this argument by highlighting logical flaws, ethical concerns, or alternative perspectives. Provide a thoughtful counterargument and end with a statement that strengthens your original stance."

        response2 = gemini_model.invoke(input2)

        returning_transcript += "\nGemini AI (Con):" + format_response_gemini(response2)

        # Store arguments for judging
        debate_transcript.append({"Pro": response1, "Con": response2})

        # OpenAI GPT counters Claude AI
        input1 = f"Gemini AI argued: {response2}. Now rebut from the {side1} perspective. Rebut this argument by highlighting logical flaws, ethical concerns, or alternative perspectives. Provide a thoughtful counterargument and end with a statement that strengthens your original stance."

    judge_response = get_judge_response(claude_model, debate_transcript, topic)

    returning_transcript += "\nClaude AI (Judge):" + format_response_claude(judge_response)

    return returning_transcript