"""
Evaluation functions for UPSC essay assessment
"""

from src.models import UPSCState
from config.settings import Config


def evaluate_language(state: UPSCState):
    """Evaluate the language quality of the essay"""
    structured_model = Config.get_structured_model()
    
    prompt = f'''Evaluate the language quality of the following essay and provide feedback and assign a score out of 10.
    
    Focus on:
    - Grammar and syntax correctness
    - Vocabulary usage and variety
    - Sentence structure and flow
    - Overall linguistic competence
    
    Essay:
    {state["essay"]}'''
    
    output = structured_model.invoke(prompt)
    return {'language_feedback': output.feedback, 'individual_scores': [output.score]}


def evaluate_analysis(state: UPSCState):
    """Evaluate the depth of analysis in the essay"""
    structured_model = Config.get_structured_model()
    
    prompt = f'''Evaluate the depth of analysis of the following essay and provide feedback and assign a score out of 10.
    
    Focus on:
    - Critical thinking and reasoning
    - Evidence and examples provided
    - Analytical depth and insight
    - Logical argumentation
    
    Essay:
    {state["essay"]}'''
    
    output = structured_model.invoke(prompt)
    return {'analysis_feedback': output.feedback, 'individual_scores': [output.score]}


def evaluate_thought(state: UPSCState):
    """Evaluate the clarity of thought in the essay"""
    structured_model = Config.get_structured_model()
    
    prompt = f'''Evaluate the clarity of thought of the following essay and provide feedback and assign a score out of 10.
    
    Focus on:
    - Clear presentation of ideas
    - Logical flow and organization
    - Coherence and consistency
    - Conclusion and synthesis
    
    Essay:
    {state["essay"]}'''
    
    output = structured_model.invoke(prompt)
    return {'clarity_feedback': output.feedback, 'individual_scores': [output.score]}


def final_evaluation(state: UPSCState):
    """Generate final evaluation summary"""
    model = Config.get_model()
    
    # Create summary feedback
    prompt = f'''Based on the following detailed feedbacks, create a comprehensive summarized evaluation for this UPSC essay:

    Language Quality Feedback: {state["language_feedback"]}
    
    Depth of Analysis Feedback: {state["analysis_feedback"]}
    
    Clarity of Thought Feedback: {state["clarity_feedback"]}
    
    Please provide a concise overall assessment highlighting key strengths and areas for improvement.'''
    
    overall_feedback = model.invoke(prompt).content
    
    # Calculate average score
    avg_score = sum(state['individual_scores']) / len(state['individual_scores'])
    
    return {'overall_feedback': overall_feedback, 'avg_score': avg_score}
