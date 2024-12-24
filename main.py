import argparse
from models import load_openai_model, load_gemini_model, load_claude_model
from debate_manager import conduct_debate

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Conduct a debate on a given topic.")
    parser.add_argument(
        "topic", 
        type=str, 
        help="The topic for the debate (e.g., 'Is AI beneficial to society?')"
    )
    
    # Parse arguments
    args = parser.parse_args()
    topic = args.topic

    # Load models
    openai_model = load_openai_model()
    gemini_model = load_gemini_model()
    claude_model = load_claude_model()

    print(f"The topic of this debate is: {topic}\n")

    # Conduct the debate
    conduct_debate(openai_model, gemini_model, claude_model, topic)

    print(f"This concludes the debate on, {topic}\n\n\n")

if __name__ == "__main__":
    main()
