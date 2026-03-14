import os
from dotenv import load_dotenv
from shared.utils.openai_client import generate_explanation

# Load environment variables
load_dotenv()

def test_openai_setup():
    """Test OpenAI API configuration"""
    print("🔍 Testing OpenAI Setup...")
    print("-" * 50)
    
    # Check environment variables
    print("📋 Environment Variables:")
    print(f"OPENAI_API_KEY: {'Set' if os.getenv('OPENAI_API_KEY') else 'Not set'}")
    print(f"OPENAI_MODEL: {os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')}")
    print()
    
    # Test explanation generation
    print("🤖 Testing AI Explanation Generation:")
    print("-" * 50)
    
    test_topic = "stacks in DSA"
    test_level = "high_school"
    
    print(f"Topic: {test_topic}")
    print(f"Academic Level: {test_level}")
    print()
    
    try:
        explanation = generate_explanation(test_topic, test_level)
        print("✅ Explanation Generated Successfully!")
        print("📝 Response:")
        print(explanation[:300] + "..." if len(explanation) > 300 else explanation)
        
    except Exception as e:
        print("❌ Error generating explanation:")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_openai_setup()