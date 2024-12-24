from models import load_openai_model, load_claude_model, load_gemini_model
from debate_manager import conduct_debate

if __name__ == "__main__":
    # Load models
    openai_model = load_openai_model()
    claude_model = load_claude_model()
    gemini_model = load_gemini_model()
    
    # Set debate topic
    topic = "Is luigi mangione objectively hot?"
    
    print(f"\nThe topic of this debate is: \n\t{topic}\n")

    # Start the debate
    conduct_debate(openai_model, gemini_model, claude_model, topic)
