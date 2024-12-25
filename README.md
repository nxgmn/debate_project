# Debate Project

This project is a multi-model debate application designed to showcase familiarity with LangChain and LLMs (Large Language Models). Users can input a debate topic, and different AI models argue for or against it. Additionally, users can adjust debate settings, customize the behavior of each participating model, and even judge debates themselves.

---

## **Features**

### **Core Functionality**
1. **Multi-Model Debate System**
   - Leverages OpenAI GPT, Gemini, and Claude models to simulate debates on user-defined topics.
   - Each model presents arguments in a structured manner, including Pro and Con sides.

2. **Adjustable Global Settings**
   - Universal settings (e.g., temperature, formality, argument length) can be applied across all models.

3. **Model-Specific Overrides**
   - Allows customization of individual models’ behavior for fine-tuned debate scenarios.

4. **Third-Party AI Judge**
   - Claude AI acts as a neutral judge, evaluating arguments and determining the debate’s winner based on logical consistency, relevance, and overall persuasiveness.

5. **CLI-Driven Topics**
   - Users input debate topics directly via the command line interface.

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.9+
- API keys for OpenAI, Gemini, and Claude models
- Necessary Python libraries (see `requirements.txt`)

### **Installation Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/username/debate-project.git
   cd debate-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for API keys:
   - Create a `.env` file in the project root:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     GEMINI_API_KEY=your_gemini_api_key
     CLAUDE_API_KEY=your_claude_api_key
     ```

4. Run the application:
   ```bash
   python main.py --topic "Your debate topic here"
   ```

---

## **Project Structure**
```
.
├── main.py                # Entry point of the application
├── models.py              # Model initialization and settings integration
├── debate_manager.py      # Core logic for managing debates
├── judge.py               # Handles third-party AI judging functionality
├── settings.py            # Global settings and model-specific overrides
├── formatting.py          # Formatting responses for display
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .env                   # Environment variables (not included in the repo)
```

---

## **Current Settings Features**
1. **Global Settings**
   - Control universal parameters like temperature, formality, and argument length.
2. **Model-Specific Overrides**
   - Customize behavior for individual models without affecting global settings.
3. **Final Settings Management**
   - Combines global and overridden settings for each model during debates.

---

## **Planned Features**

### **1. Pull Debate Topics from News APIs**
Automatically generate debate topics from trending news stories, ensuring relevance and variety.

- **Suggested APIs**: NewsAPI, Google News
- **Implementation Steps**:
  1. Integrate API calls to fetch trending headlines.
  2. Parse and format headlines into debate-worthy topics.
  3. Add an option for users to select between predefined and news-driven topics.

### **2. Personal Debate Tool**
Enable users to input personal or whimsical questions (e.g., "Should I wear blue or yellow today?").

- **Settings Adjustments**:
  - Allow lightweight debates with shorter arguments and informal tones.
  - Enable user-driven customization for Pro/Con stances.

### **3. Adjustable AI Settings**
Enhance customization by allowing users to control:
- **Temperature**: Creativity of responses.
- **Formality**: Casual vs. formal tones.
- **Argument Length**: Short, medium, or long responses.

### **4. User as Judge**
Replace the third-party AI judge with the user themselves.
- **Features**:
  - Users can manually rate each argument on clarity, logic, and persuasiveness.
  - Provide a verdict through a simple interactive interface.

### **5. Choose Arguing LLMs**
Let users pick which AI models participate in debates.
- **Purpose**: Add humor or variety by combining models with distinct styles.

---

## **Suggested Implementation Order**

1. **Adjustable AI Settings**
   - Implement temperature, formality, and argument length customization.
   - Foundational for other features.

2. **Personal Debate Tool**
   - Complement adjustable settings by allowing users to ask quirky or personal questions.

3. **Pull Debate Topics from News APIs**
   - Expand the pool of debate topics dynamically.

4. **User as Judge**
   - Increase interactivity by letting users decide the winner.

5. **Choose Arguing LLMs**
   - Finalize by adding a layer of customization for humor and diversity.

---

## **Future Enhancements**
- **Multilingual Support**: Expand debates to include arguments in multiple languages.
- **Improved Front-End Interface**: Replace CLI with a web-based or graphical user interface.
- **Real-Time Debate Scoring**: Display live scoring metrics during debates.
- **Integration with Speech-to-Text**: Enable verbal input for debate topics.

---

## **Contributing**
Contributions are welcome! To get started:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.

---

## **License**
This project is licensed under the MIT License. See `LICENSE` for more details.

