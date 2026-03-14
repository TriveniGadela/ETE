import openai
import os
from dotenv import load_dotenv

load_dotenv()

def test_openai():
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ No OpenAI API key found in .env file")
            return
            
        openai.api_key = api_key
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Explain photosynthesis in simple terms for a high school student."}
            ],
            max_tokens=100
        )
        
        print("✅ OpenAI is working!")
        print("Response:", response.choices[0].message.content.strip())
        
    except Exception as e:
        print("❌ OpenAI test failed:")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_openai()