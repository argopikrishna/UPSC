"""
LangGraph workflow for UPSC essay evaluation
"""

from langgraph.graph import StateGraph, START, END
from src.models import UPSCState
from src.evaluators import evaluate_language, evaluate_analysis, evaluate_thought, final_evaluation


class UPSCEvaluationWorkflow:
    """UPSC Essay Evaluation Workflow using LangGraph"""
    
    def __init__(self):
        self.workflow = self._build_workflow()
    
    def _build_workflow(self):
        """Build the evaluation workflow graph"""
        graph = StateGraph(UPSCState)
        
        # Add nodes
        graph.add_node('evaluate_language', evaluate_language)
        graph.add_node('evaluate_analysis', evaluate_analysis)
        graph.add_node('evaluate_thought', evaluate_thought)
        graph.add_node('final_evaluation', final_evaluation)
        
        # Add edges - parallel evaluation of three criteria
        graph.add_edge(START, 'evaluate_language')
        graph.add_edge(START, 'evaluate_analysis')
        graph.add_edge(START, 'evaluate_thought')
        
        # All evaluations feed into final evaluation
        graph.add_edge('evaluate_language', 'final_evaluation')
        graph.add_edge('evaluate_analysis', 'final_evaluation')
        graph.add_edge('evaluate_thought', 'final_evaluation')
        graph.add_edge('final_evaluation', END)
        
        return graph.compile()
    
    def evaluate_essay(self, essay: str):
        """Evaluate an essay and return results"""
        initial_state = {'essay': essay}
        result = self.workflow.invoke(initial_state)
        return result
