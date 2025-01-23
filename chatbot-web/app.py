from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()

app = Flask(__name__)
# Configure CORS to allow requests from your Netlify domain
CORS(app, resources={r"/api/*": {"origins": ["https://craigdoesdata-chatbot.netlify.app", "http://localhost:3000"], "methods": ["POST", "OPTIONS"], "allow_headers": ["Content-Type"]}})

# Initialize the OpenAI client with Deepseek base URL
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com/v1"  # Updated with /v1 endpoint
)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
        # Add your system message to the beginning if it's not there
        if not messages or messages[0]['role'] != 'system':
            messages.insert(0, {
                "role": "system",
                "content": """You are the world's smartest and most talented coder.
                You are incredible at explaining python and SQL code and analysing it and identifying bugs.
                You have a passion for helping others to see and understand the beauty of code, and you love to help solve programming problems."""
            })

        completion = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.0,
        )
        
        response = completion.choices[0].message.content
        return jsonify({'response': response})

    except Exception as e:
        print(f"Error details: {str(e)}")  # Added detailed error logging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)