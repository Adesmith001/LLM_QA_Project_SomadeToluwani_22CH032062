"""
LLM Question-and-Answering Web GUI Application
Author: Somade Toluwani
Matric: 22CH032062
"""

from flask import Flask, render_template, request, jsonify
import os
import string
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

def preprocess_question(question):
    """
    Preprocess the user's question:
    - Lowercasing
    - Tokenization
    - Punctuation removal (partial)
    """
    # Lowercase
    question_lower = question.lower()
    
    # Remove extra whitespace
    question_clean = ' '.join(question_lower.split())
    
    # Tokenization (split into words)
    tokens = question_clean.split()
    
    # Remove punctuation except question marks
    cleaned_tokens = []
    for token in tokens:
        if token.endswith('?'):
            cleaned_tokens.append(token)
        else:
            cleaned_token = token.translate(str.maketrans('', '', string.punctuation))
            if cleaned_token:
                cleaned_tokens.append(cleaned_token)
    
    # Reconstruct the processed question
    processed_question = ' '.join(cleaned_tokens)
    
    return processed_question, tokens

def query_llm(question):
    """
    Send the question to Groq API and get the answer
    """
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        return "Error: GROQ_API_KEY not found. Please configure your environment variables."
    
    try:
        # Configure Groq API
        client = Groq(api_key=api_key)
        
        # Construct prompt
        prompt = f"Please answer the following question concisely and accurately:\n\nQuestion: {question}\n\nAnswer:"
        
        # Make API call
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        # Extract answer
        answer = chat_completion.choices[0].message.content.strip()
        return answer
        
    except Exception as e:
        return f"Error querying LLM: {str(e)}"

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle question submission and return answer"""
    data = request.get_json()
    question = data.get('question', '').strip()
    
    if not question:
        return jsonify({
            'error': 'Please enter a valid question.'
        }), 400
    
    # Preprocess the question
    processed_question, tokens = preprocess_question(question)
    
    # Query the LLM
    answer = query_llm(question)
    
    # Return results
    return jsonify({
        'original_question': question,
        'processed_question': processed_question,
        'tokens': tokens,
        'answer': answer
    })

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)
