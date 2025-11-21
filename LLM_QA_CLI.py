"""
LLM Question-and-Answering CLI Application
Author: Somade Toluwani
Matric: 22CH032062
"""

import os
import re
import string
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def preprocess_question(question):
    """
    Preprocess the user's question:
    - Lowercasing
    - Tokenization
    - Punctuation removal (partial - keeping question marks for context)
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
        # Keep question marks, remove other punctuation
        if token.endswith('?'):
            cleaned_tokens.append(token)
        else:
            cleaned_token = token.translate(str.maketrans('', '', string.punctuation))
            if cleaned_token:  # Only add non-empty tokens
                cleaned_tokens.append(cleaned_token)
    
    # Reconstruct the processed question
    processed_question = ' '.join(cleaned_tokens)
    
    return processed_question, tokens

def query_llm(question, api_key=None):
    """
    Send the question to Groq API and get the answer
    """
    if not api_key:
        api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        return "Error: GROQ_API_KEY not found. Please set it in your .env file."
    
    try:
        # Initialize Groq client
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

def main():
    """
    Main CLI application loop
    """
    print("=" * 60)
    print("LLM Question-and-Answering System (CLI)")
    print("Author: Somade Toluwani | Matric: 22CH032062")
    print("=" * 60)
    print("\nType 'exit' or 'quit' to end the session.\n")
    
    while True:
        # Get user input
        question = input("\nEnter your question: ").strip()
        
        # Check for exit command
        if question.lower() in ['exit', 'quit', 'q']:
            print("\nThank you for using the LLM Q&A System. Goodbye!")
            break
        
        # Skip empty questions
        if not question:
            print("Please enter a valid question.")
            continue
        
        # Preprocess the question
        processed_question, tokens = preprocess_question(question)
        
        print(f"\n[Original Question]: {question}")
        print(f"[Processed Question]: {processed_question}")
        print(f"[Tokens]: {tokens}")
        print("\n[Querying LLM API...]")
        
        # Query the LLM
        answer = query_llm(question)
        
        # Display the answer
        print("\n" + "=" * 60)
        print("ANSWER:")
        print("=" * 60)
        print(answer)
        print("=" * 60)

if __name__ == "__main__":
    main()
