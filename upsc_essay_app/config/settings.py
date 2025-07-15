"""
Configuration management for the UPSC essay evaluation app
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.models import EvaluationSchema

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""
    
    # Model configuration
    MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/mistral-small-3.2-24b-instruct:free")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    
    # API configuration - supports both OpenAI and OpenRouter
    API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
    BASE_URL = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    
    @classmethod
    def get_model(cls):
        """Get configured model (works with OpenRouter)"""
        if not cls.API_KEY:
            raise ValueError("API key not found. Please set OPENAI_API_KEY or OPENROUTER_API_KEY in environment variables")
        
        return ChatOpenAI(
            model=cls.MODEL_NAME,
            temperature=cls.TEMPERATURE,
            openai_api_key=cls.API_KEY,
            openai_api_base=cls.BASE_URL,
        )
    
    @classmethod
    def get_structured_model(cls):
        """Get model with structured output"""
        base_model = cls.get_model()
        return base_model.with_structured_output(EvaluationSchema)
