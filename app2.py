from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot5 import rag_response  # Import your chatbot code

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_question = data.get('question', '').strip()  # Ensure there is no leading/trailing whitespace
    print("data:", data)
        
    if not user_question:
        raise ValueError("User question is missing or empty.")
    response = rag_response(user_question)
    print("gave:", response)
    return jsonify({'response': response.content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
