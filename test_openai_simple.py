import os
from dotenv import load_dotenv
from shared.utils.openai_client import generate_explanation

load_dotenv()

def test_openai_setup():
    """Test OpenAI API configuration"""
    print("Testing OpenAI Setup...")
    print("-" * 50)
    
    # Check environment variables
    print("Environment Variables:")
    print(f"OPENAI_API_KEY: {'Set' if os.getenv('OPENAI_API_KEY') else 'Not set'}")
    print(f"OPENAI_MODEL: {os.getenv('OPENAI_MODEL', 'gpt-4o-mini')}")
    print()
    
    # Test explanation generation
    print("Testing AI Explanation Generation:")
    print("-" * 50)
    
    test_topic = "photosynthesis"
    test_level = "high_school"
    
    print(f"Topic: {test_topic}")
    print(f"Academic Level: {test_level}")
    print()
    
    try:
        explanation = generate_explanation(test_topic, test_level)
        print("SUCCESS: Explanation Generated!")
        print("Response:")
        print(explanation[:200] + "..." if len(explanation) > 200 else explanation)
        
    except Exception as e:
        print("ERROR: Failed to generate explanation")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_openai_setup()