"""
Core models and schemas for UPSC essay evaluation
"""

from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
import operator


class EvaluationSchema(BaseModel):
    """Schema for individual evaluation criteria"""
    feedback: str = Field(description='Detailed feedback for the essay')
    score: int = Field(description='Score out of 10', ge=0, le=10)


class UPSCState(TypedDict):
    """State schema for UPSC essay evaluation workflow"""
    essay: str
    language_feedback: str
    analysis_feedback: str
    clarity_feedback: str
    overall_feedback: str
    individual_scores: Annotated[list[int], operator.add]
    avg_score: float
