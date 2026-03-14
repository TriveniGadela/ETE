print("Please paste your OpenAI API key below:")
print("(It should start with 'sk-' and be about 51+ characters long)")
print()

api_key = input("Enter your API key: ").strip()

if not api_key:
    print("No API key entered. Exiting.")
    exit()

if not api_key.startswith('sk-'):
    print("Warning: API key should start with 'sk-'")
    confirm = input("Continue anyway? (y/n): ")
    if confirm.lower() != 'y':
        exit()

# Update the .env file
env_content = f"""SECRET_KEY=your-secret-key-here
OPENAI_API_KEY={api_key}
OPENAI_MODEL=gpt-4o-mini
MONGODB_URI=mongodb://localhost:27017/learning_platform
"""

try:
    with open('.env', 'w') as f:
        f.write(env_content)
    print("SUCCESS: .env file updated!")
    print(f"API key set to: {api_key[:10]}...{api_key[-4:]}")
except Exception as e:
    print(f"ERROR: Could not update .env file: {e}")