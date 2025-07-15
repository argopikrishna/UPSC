# UPSC Essay Evaluation System

A comprehensive AI-powered essay evaluation system designed specifically for UPSC aspirants. This repository contains both a Jupyter notebook prototype and a full-featured Streamlit web application.

## 🌟 Features

- **Multi-Criteria Evaluation**: Evaluates essays on three key dimensions:
  - Language Quality (Grammar, vocabulary, sentence structure)
  - Depth of Analysis (Critical thinking, evidence, reasoning)
  - Clarity of Thought (Organization, coherence, logical flow)

- **Parallel Processing**: Uses LangGraph for efficient parallel evaluation of all criteria

- **Interactive Web Interface**: Clean, user-friendly Streamlit application

- **Sample Essays**: Includes sample essays for testing and comparison

- **Detailed Feedback**: Provides specific, actionable feedback for improvement

- **OpenRouter Integration**: Compatible with multiple AI models through OpenRouter API

## 📁 Repository Structure

```
UPSC/
├── UPSC_essay_workflow.ipynb    # Original Jupyter notebook prototype
├── upsc_essay_app/              # Streamlit web application
│   ├── app.py                   # Main Streamlit application
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment variables (template)
│   ├── README.md                # Detailed app documentation
│   ├── setup.sh                 # Setup script
│   ├── src/                     # Source code
│   │   ├── models.py            # Data models and schemas
│   │   ├── evaluators.py        # Evaluation functions
│   │   └── workflow.py          # LangGraph workflow
│   ├── config/                  # Configuration
│   │   └── settings.py          # App configuration
│   └── utils/                   # Utility functions
│       └── helpers.py           # Helper functions for UI
└── README.md                    # This file
```

## 🚀 Quick Start

### Option 1: Streamlit Web Application (Recommended)

1. **Navigate to the app directory:**
   ```bash
   cd upsc_essay_app
   ```

2. **Run the setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure your API key:**
   - Edit the `.env` file and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

4. **Run the application:**
   ```bash
   source venv/bin/activate
   streamlit run app.py
   ```

### Option 2: Jupyter Notebook

1. **Open the notebook:**
   ```bash
   jupyter notebook UPSC_essay_workflow.ipynb
   ```

2. **Install required dependencies:**
   ```bash
   pip install langgraph langchain-openai python-dotenv pydantic
   ```

3. **Configure your API key in the notebook**

## 🔧 Configuration

### API Key Setup

This application uses OpenRouter for AI model access. You can get an API key from [OpenRouter](https://openrouter.ai/).

**For Streamlit App:**
- Add your API key to the `.env` file or enter it directly in the app sidebar

**For Jupyter Notebook:**
- Add your API key to the notebook environment or use a `.env` file

### Supported Models

The application is configured to use:
- Default: `mistralai/mistral-small-3.2-24b-instruct:free`
- Customizable through configuration

## 💡 How to Use

### Streamlit Application

1. **Configure API Key**: Enter your OpenRouter API key in the sidebar
2. **Input Essay**: Either paste your essay or select a sample essay
3. **Evaluate**: Click "Evaluate Essay" to get comprehensive feedback
4. **Review Results**: Analyze the scores and detailed feedback provided

### Jupyter Notebook

1. **Run the cells sequentially** to set up the evaluation pipeline
2. **Replace the sample essay** with your own content
3. **Execute the evaluation workflow** to get detailed feedback

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

## 🧩 Architecture

The system uses:

- **LangGraph**: For orchestrating the evaluation workflow
- **OpenRouter**: For AI model access with multiple provider support
- **Streamlit**: For the web interface
- **Pydantic**: For data validation and modeling

The evaluation workflow runs three assessments in parallel, then combines results into a comprehensive final evaluation.

## 📝 Sample Essays

The application includes sample essays demonstrating different quality levels:
- **High Quality**: Well-structured essay on "India in the Age of AI"
- **Low Quality**: Poorly written essay for comparison

## 🔧 Development

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key

### Installation

```bash
# Clone the repository
git clone https://github.com/argopikrishna/UPSC.git
cd UPSC

# For Streamlit app
cd upsc_essay_app
pip install -r requirements.txt

# For Jupyter notebook
pip install langgraph langchain-openai python-dotenv pydantic jupyter
```

### Customization

You can customize the evaluation by:

1. **Modifying Prompts**: Edit evaluation prompts in `upsc_essay_app/src/evaluators.py`
2. **Adding Criteria**: Extend the evaluation workflow in `upsc_essay_app/src/workflow.py`
3. **Changing Models**: Update model configuration in `upsc_essay_app/config/settings.py`

## 🐛 Troubleshooting

### Common Issues:

1. **API Key Errors**:
   - Ensure your OpenRouter API key is valid
   - Check you have sufficient API credits

2. **Import Errors**:
   - Make sure all dependencies are installed
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

This project is for educational purposes. Please ensure compliance with OpenRouter's and respective AI model providers' usage policies.

## 🙏 Acknowledgments

- Built for UPSC aspirants seeking quality essay feedback
- Uses OpenRouter for multi-model AI access
- Powered by LangGraph for workflow orchestration
- Created with Streamlit for an intuitive interface

---

**Note**: Both the Jupyter notebook and Streamlit app provide the same core functionality. The Streamlit app offers a more user-friendly interface, while the notebook is better for experimentation and customization.
