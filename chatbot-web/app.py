from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

# Set up logging to help us debug issues
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure CORS to allow requests from your Netlify domain
CORS(app, resources={r"/api/*": {
    "origins": ["https://craigdoesdata-chatbot.netlify.app", "http://localhost:3000"],
    "methods": ["POST", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})

# Initialize the OpenAI client - using a simpler configuration
try:
    client = OpenAI(
        api_key=os.getenv('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com/v1",
        default_headers={"Content-Type": "application/json"}
    )
    logger.info("OpenAI client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {str(e)}")
    raise

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
        # Add system message if not present
        if not messages or messages[0]['role'] != 'system':
            messages.insert(0, {
                "role": "system",
                "content": """You are the world's smartest and most talented coder.
                You are incredible at explaining python and SQL code and analysing it and identifying bugs.
                You have a passion for helping others to see and understand the beauty of code, and you love to help solve programming problems."""
            })

        logger.info("Making request to DeepSeek API")
        completion = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.0
        )
        
        response = completion.choices[0].message.content
        return jsonify({'response': response})

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True)
