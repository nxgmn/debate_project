from models import load_openai_model, load_gemini_model, load_claude_model
from debate_manager import conduct_debate
import sys

def generate_debate(topic):
    # load models
    openai_model = load_openai_model()
    gemini_model = load_gemini_model()
    claude_model = load_claude_model()

    transcript = f"The topic of this debate is: {topic}\n"

    transcript = conduct_debate(openai_model, gemini_model, claude_model, topic)

    transcript += f"This concludes the debate on, {topic}\n\n\n"

    return transcript


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No topic provided.")
        sys.exit(1)

    topic = sys.argv[1]
    result = generate_debate(topic)
    print(result)

