# UPSC Essay Evaluation System

A comprehensive AI-powered essay evaluation system designed specifically for UPSC aspirants. This Streamlit application uses LangGraph and OpenRouter to provide detailed feedback on essays across multiple criteria.

## 🌟 Features

- **Multi-Criteria Evaluation**: Evaluates essays on three key dimensions:
  - Language Quality (Grammar, vocabulary, sentence structure)
  - Depth of Analysis (Critical thinking, evidence, reasoning)
  - Clarity of Thought (Organization, coherence, logical flow)

- **Parallel Processing**: Uses LangGraph for efficient parallel evaluation of all criteria

- **Interactive Interface**: Clean, user-friendly Streamlit interface

- **Sample Essays**: Includes sample essays for testing and comparison

- **Detailed Feedback**: Provides specific, actionable feedback for improvement

- **Scoring System**: 1-10 scale scoring for each evaluation criterion

- **OpenRouter Integration**: Access to multiple AI models through OpenRouter API

## 📁 Project Structure

```
upsc_essay_app/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (template)
├── README.md              # This file
├── src/                   # Source code
│   ├── __init__.py
│   ├── models.py          # Data models and schemas
│   ├── evaluators.py      # Evaluation functions
│   └── workflow.py        # LangGraph workflow
├── config/                # Configuration
│   ├── __init__.py
│   └── settings.py        # App configuration
└── utils/                 # Utility functions
    ├── __init__.py
    └── helpers.py         # Helper functions for UI
```

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- OpenRouter API key (get one at [OpenRouter](https://openrouter.ai/))

### 2. Installation

```bash
# Clone or navigate to the project directory
cd upsc_essay_app

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

1. Copy the `.env` file and add your OpenRouter API key:
```bash
cp .env .env.local
```

2. Edit `.env.local` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_actual_openrouter_api_key_here
OPENAI_BASE_URL=https://openrouter.ai/api/v1
MODEL_NAME=mistralai/mistral-small-3.2-24b-instruct:free
TEMPERATURE=0.7
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser at `http://localhost:8501`

## 💡 How to Use

1. **Configure API Key**: Enter your OpenRouter API key in the sidebar
2. **Input Essay**: Either paste your essay or select a sample essay
3. **Evaluate**: Click "Evaluate Essay" to get comprehensive feedback
4. **Review Results**: Analyze the scores and detailed feedback provided

## 🧩 Architecture

The application uses:

- **Streamlit**: For the web interface
- **LangGraph**: For orchestrating the evaluation workflow
- **OpenRouter**: For AI-powered essay evaluation with access to multiple models
- **Pydantic**: For data validation and modeling

The evaluation workflow runs three assessments in parallel:
1. Language Quality Assessment
2. Depth of Analysis Assessment  
3. Clarity of Thought Assessment

Results are then combined into a comprehensive final evaluation.

## 📊 Evaluation Criteria

### Language Quality (Score: 0-10)
- Grammar and syntax correctness
- Vocabulary usage and variety
- Sentence structure and flow
- Overall linguistic competence

### Depth of Analysis (Score: 0-10)
- Critical thinking and reasoning
- Evidence and examples provided
- Analytical depth and insight
- Logical argumentation

### Clarity of Thought (Score: 0-10)
- Clear presentation of ideas
- Logical flow and organization
- Coherence and consistency
- Conclusion and synthesis

## 🔧 Customization

You can customize the evaluation by:

1. **Modifying Prompts**: Edit the evaluation prompts in `src/evaluators.py`
2. **Adding Criteria**: Extend the evaluation workflow in `src/workflow.py`
3. **Changing Models**: Update model configuration in `config/settings.py`

## 📝 Sample Essays

The application includes two sample essays:
- **Good Essay**: Well-structured essay on "India in the Age of AI"
- **Poor Essay**: Poorly written essay for comparison

## 🐛 Troubleshooting

### Common Issues:

1. **API Key Errors**:
   - Ensure your OpenRouter API key is valid
   - Check you have sufficient API credits on OpenRouter

2. **Import Errors**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Ensure you're in the correct virtual environment

3. **Long Response Times**:
   - The evaluation process involves multiple AI model calls
   - Expect 30-60 seconds for complete evaluation

## 🤝 Contributing

Feel free to contribute by:
- Adding new evaluation criteria
- Improving the UI/UX
- Adding more sample essays
- Optimizing the evaluation workflow

## 📄 License

This project is for educational purposes. Please ensure compliance with OpenRouter's usage policies when using their API.

## 🙏 Acknowledgments

- Built for UPSC aspirants seeking quality essay feedback
- Uses OpenRouter's powerful language models
- Powered by LangGraph for workflow orchestration
- Created with Streamlit for an intuitive interface
