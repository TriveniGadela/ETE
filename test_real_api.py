import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_openai_api():
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key or api_key == 'sk-your-openai-api-key-here':
        print("ERROR: Please update your .env file with a real OpenAI API key")
        print("Your current key:", api_key)
        return False
    
    print(f"API Key found: {api_key[:10]}...{api_key[-4:]}")
    
    # Test the API
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': 'gpt-4o-mini',
        'messages': [{'role': 'user', 'content': 'Say hello'}],
        'max_tokens': 10
    }
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("SUCCESS: OpenAI API is working!")
            print("Response:", result['choices'][0]['message']['content'])
            return True
        else:
            print(f"ERROR: API returned status {response.status_code}")
            print("Response:", response.text)
            return False
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    test_openai_api()