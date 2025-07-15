"""
UPSC Essay Evaluation Streamlit App
"""

import streamlit as st
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.workflow import UPSCEvaluationWorkflow
from utils.helpers import format_feedback_display, get_sample_essays
from config.settings import Config


def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="UPSC Essay Evaluator",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Header
    st.title("📝 UPSC Essay Evaluation System")
    st.markdown("### AI-Powered Comprehensive Essay Assessment")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🔧 Configuration")
        
        # Check API key
        api_key = st.text_input("OpenRouter API Key", type="password", 
                               help="Enter your OpenRouter API key to use the evaluation service")
        
        if api_key:
            os.environ["OPENROUTER_API_KEY"] = api_key
            os.environ["OPENAI_API_KEY"] = api_key  # For compatibility
            st.success("✅ API Key configured!")
        else:
            st.warning("⚠️ Please enter your OpenRouter API key to continue")
            st.markdown("Get your API key from [OpenRouter](https://openrouter.ai/)")
        
        st.markdown("---")
        
        # Sample essays
        st.markdown("## 📄 Sample Essays")
        sample_essays = get_sample_essays()
        selected_sample = st.selectbox(
            "Choose a sample essay:",
            [""] + list(sample_essays.keys())
        )
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("## ✍️ Essay Input")
        
        # Essay input
        essay_text = ""
        if selected_sample and selected_sample in sample_essays:
            essay_text = sample_essays[selected_sample]
        
        essay_input = st.text_area(
            "Paste your UPSC essay here:",
            value=essay_text,
            height=400,
            placeholder="Enter your essay text here..."
        )
        
        # Evaluation criteria info
        st.markdown("### 📋 Evaluation Criteria")
        st.markdown("""
        Your essay will be evaluated on three key criteria:
        
        1. **🔤 Language Quality** - Grammar, vocabulary, sentence structure
        2. **🧠 Depth of Analysis** - Critical thinking, evidence, reasoning
        3. **💡 Clarity of Thought** - Organization, coherence, logical flow
        """)
        
        # Evaluate button
        evaluate_button = st.button(
            "🚀 Evaluate Essay",
            type="primary",
            disabled=not (api_key and essay_input.strip())
        )
    
    with col2:
        st.markdown("## 📊 Evaluation Results")
        
        if evaluate_button:
            if not api_key:
                st.error("❌ Please provide your OpenRouter API key in the sidebar")
            elif not essay_input.strip():
                st.error("❌ Please enter an essay to evaluate")
            else:
                try:
                    with st.spinner("🔄 Evaluating your essay... This may take a moment."):
                        # Initialize workflow
                        workflow = UPSCEvaluationWorkflow()
                        
                        # Evaluate essay
                        result = workflow.evaluate_essay(essay_input.strip())
                        
                        # Display results
                        format_feedback_display(result)
                        
                except Exception as e:
                    st.error(f"❌ An error occurred during evaluation: {str(e)}")
                    st.markdown("### Troubleshooting:")
                    st.markdown("""
                    - Check your OpenRouter API key is valid
                    - Ensure you have sufficient API credits on OpenRouter
                    - Try with a shorter essay if the text is very long
                    - Check your internet connection
                    """)
        else:
            st.info("👆 Enter your essay and click 'Evaluate Essay' to get started!")
            
            # Instructions
            st.markdown("### 📖 How to Use")
            st.markdown("""
            1. **Configure API Key**: Enter your OpenRouter API key in the sidebar
            2. **Choose Essay**: Either paste your own essay or select a sample
            3. **Evaluate**: Click the evaluate button to get comprehensive feedback
            4. **Review Results**: Get scores and detailed feedback on all criteria
            """)
            
            st.markdown("### ✨ Features")
            st.markdown("""
            - **Parallel Evaluation**: Simultaneous assessment of multiple criteria
            - **Detailed Feedback**: Specific suggestions for improvement
            - **Scoring System**: 1-10 scale for each evaluation criterion
            - **Sample Essays**: Compare different quality levels
            - **OpenRouter Integration**: Access to multiple AI models
            """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit, LangGraph, and OpenRouter</p>
        <p>For UPSC aspirants seeking comprehensive essay feedback</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
