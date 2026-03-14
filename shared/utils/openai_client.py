import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

def get_fallback_explanation(topic, academic_level):
    """Provide a sample explanation when API is unavailable"""
    level_explanations = {
        'elementary': f"""<div style='background: #fff3cd; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
            <p><strong>⚠️ Demo Mode:</strong> OpenAI API credits needed. Add credits at <a href='https://platform.openai.com/account/billing' target='_blank'>OpenAI Billing</a></p>
            </div>
            <h3>About {topic}</h3>
            <p><strong>{topic}</strong> is an interesting topic! Let me explain it in simple words.</p>
            <p>Think of it like something you use every day. It helps us understand how things work around us.</p>
            <p>For example, imagine you're learning about something new and exciting. That's what {topic} is all about!</p>""",
        'middle_school': f"""<div style='background: #fff3cd; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
            <p><strong>⚠️ Demo Mode:</strong> OpenAI API credits needed. Add credits at <a href='https://platform.openai.com/account/billing' target='_blank'>OpenAI Billing</a></p>
            </div>
            <h3>Understanding {topic}</h3>
            <p><strong>{topic}</strong> is an important concept that you'll find useful in your studies.</p>
            <p>This topic connects to many things you already know and helps explain how the world works.</p>
            <p>Key points to remember about {topic}:</p>
            <ul>
                <li>It's a fundamental concept in this subject area</li>
                <li>You can see examples of it in everyday life</li>
                <li>Understanding it will help you learn more advanced topics</li>
            </ul>""",
        'high_school': f"""<div style='background: #fff3cd; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
            <p><strong>⚠️ Demo Mode:</strong> OpenAI API credits needed. Add credits at <a href='https://platform.openai.com/account/billing' target='_blank'>OpenAI Billing</a></p>
            </div>
            <h3>{topic} - High School Level</h3>
            <p><strong>{topic}</strong> is a significant concept that requires understanding of key principles and technical details.</p>
            <p><strong>Overview:</strong> This topic encompasses several important aspects that are essential for your academic progress.</p>
            <p><strong>Key Concepts:</strong></p>
            <ul>
                <li>Fundamental principles and definitions</li>
                <li>Practical applications and real-world examples</li>
                <li>Relationships to other concepts in the field</li>
                <li>Problem-solving approaches</li>
            </ul>
            <p><strong>Why it matters:</strong> Understanding {topic} provides a foundation for more advanced studies and practical applications.</p>""",
        'undergraduate': f"""<div style='background: #fff3cd; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
            <p><strong>⚠️ Demo Mode:</strong> OpenAI API credits needed. Add credits at <a href='https://platform.openai.com/account/billing' target='_blank'>OpenAI Billing</a></p>
            </div>
            <h3>{topic} - Undergraduate Analysis</h3>
            <p><strong>{topic}</strong> represents a complex area of study requiring detailed theoretical understanding and practical application.</p>
            <p><strong>Theoretical Framework:</strong> This concept is grounded in established theories and principles that have been developed through extensive research.</p>
            <p><strong>Core Components:</strong></p>
            <ul>
                <li>Theoretical foundations and historical development</li>
                <li>Mathematical or logical frameworks</li>
                <li>Empirical evidence and research findings</li>
                <li>Practical applications across various domains</li>
                <li>Current debates and ongoing research</li>
            </ul>
            <p><strong>Academic Significance:</strong> Mastery of {topic} is essential for advanced coursework and research in this field.</p>""",
        'graduate': f"""<div style='background: #fff3cd; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
            <p><strong>⚠️ Demo Mode:</strong> OpenAI API credits needed. Add credits at <a href='https://platform.openai.com/account/billing' target='_blank'>OpenAI Billing</a></p>
            </div>
            <h3>{topic} - Graduate Level Analysis</h3>
            <p><strong>{topic}</strong> constitutes a sophisticated domain requiring critical analysis, research perspective, and advanced theoretical understanding.</p>
            <p><strong>Research Context:</strong> Contemporary scholarship on {topic} encompasses multiple theoretical frameworks and methodological approaches.</p>
            <p><strong>Advanced Considerations:</strong></p>
            <ul>
                <li>Epistemological foundations and paradigmatic assumptions</li>
                <li>Critical analysis of competing theoretical perspectives</li>
                <li>Methodological considerations and research design implications</li>
                <li>Interdisciplinary connections and cross-domain applications</li>
                <li>Current research frontiers and unresolved questions</li>
                <li>Implications for practice and policy</li>
            </ul>
            <p><strong>Research Implications:</strong> Advanced study of {topic} opens avenues for original research contributions and theoretical development.</p>"""
    }
    return level_explanations.get(academic_level, level_explanations['high_school'])

def get_prompt_for_level(topic, academic_level):
    """Generate appropriate prompts based on academic level"""
    level_prompts = {
        'elementary': f'Explain {topic} in very simple terms for an elementary school student. Use easy words and fun examples.',
        'middle_school': f'Explain {topic} for a middle school student. Use clear language and relatable examples.',
        'high_school': f'Explain {topic} for a high school student. Include key concepts and some technical details.',
        'undergraduate': f'Explain {topic} for an undergraduate student. Include detailed concepts, theories, and applications.',
        'graduate': f'Explain {topic} at a graduate level. Include advanced concepts, research perspectives, and critical analysis.'
    }
    return level_prompts.get(academic_level, level_prompts['high_school'])

def generate_explanation(topic, academic_level):
    """Generate AI explanation using Google Gemini API"""
    try:
        # Check if API key exists
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key or api_key == 'your-gemini-api-key-here':
            return """<p><strong>Error:</strong> Gemini API key not configured.</p>
            <p>Please add your valid Gemini API key to the .env file:</p>
            <p><code>GEMINI_API_KEY=your-actual-api-key</code></p>
            <p>Get your API key from: <a href="https://makersuite.google.com/app/apikey" target="_blank">Google AI Studio</a></p>"""
        
        # Configure Gemini API
        genai.configure(api_key=api_key)
        
        # Generate prompt based on academic level
        prompt = get_prompt_for_level(topic, academic_level)
        
        # Get model from environment or use default
        model_name = os.getenv('GEMINI_MODEL', 'gemini-pro')
        
        # Initialize the model
        model = genai.GenerativeModel(model_name)
        
        # Generate content
        response = model.generate_content(prompt)
        
        # Extract the explanation
        explanation = response.text.strip()
        return explanation
        
    except Exception as e:
        error_message = str(e)
        
        # Handle authentication errors
        if 'API_KEY_INVALID' in error_message or 'invalid api key' in error_message.lower():
            return """<p><strong>Error:</strong> Invalid Gemini API key.</p>
            <p>Please check your API key in the .env file and make sure it's valid.</p>
            <p>Get a new API key from: <a href="https://makersuite.google.com/app/apikey" target="_blank">Google AI Studio</a></p>"""
        
        # Handle quota/rate limit errors
        elif 'quota' in error_message.lower() or 'rate limit' in error_message.lower() or 'resource_exhausted' in error_message.lower():
            return """<p><strong>Error:</strong> Gemini API quota exceeded.</p>
            <p>You've exceeded your API usage quota. Please wait a moment and try again.</p>
            <p>Check your usage at: <a href="https://makersuite.google.com/" target="_blank">Google AI Studio</a></p>"""
        
        # Handle blocked content
        elif 'blocked' in error_message.lower() or 'safety' in error_message.lower():
            return """<p><strong>Error:</strong> Content was blocked by safety filters.</p>
            <p>Please try rephrasing your topic or choose a different subject.</p>"""
        
        # Generic error
        else:
            return f"""<p><strong>Error:</strong> Failed to generate explanation.</p>
            <p><em>Error: {error_message}</em></p>
            <p><em>Topic: {topic} | Level: {academic_level.replace('_', ' ').title()}</em></p>
            <p>Please check your internet connection and try again.</p>"""