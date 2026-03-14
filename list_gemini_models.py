import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure API
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

print("Available Gemini Models:\n")
print("-" * 80)

# List all models
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model: {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Description: {model.description}")
        print(f"  Supported Methods: {model.supported_generation_methods}")
        print("-" * 80)
