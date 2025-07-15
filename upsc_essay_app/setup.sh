#!/bin/bash

# UPSC Essay Evaluation App Setup Script

echo "🚀 Setting up UPSC Essay Evaluation App..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Add your OpenAI API key to the .env file"
echo "3. Run the app: streamlit run app.py"
echo ""
echo "📖 For detailed instructions, see README.md"
