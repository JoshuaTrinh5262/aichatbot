from flask import Flask, jsonify, request
from flask_cors import CORS

from core_ai.chat_gpt import ChatGPT
from core_ai.chat_bard import ChatBard
from core_ai.telegram_bot import telegram_bot

app = Flask(__name__)
CORS(app)

# Open the text file in read mode
with open("server/logs/chat_history.txt", "r", encoding="utf-8") as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Open the text file in read mode
with open("server/logs/index_chat_history.txt", "r", encoding="utf-8") as file:
    # Read all lines from the file into a list
    index_lines = file.readlines()

#load chat_history here
store_conversation = [line.strip() for line in lines]
index_store_conversation = [line.strip() for line in index_lines]

#  Post chatgpt by index
@app.route('/api/chatgptbyindex', methods = ['POST'])
def post_chatgptbyindex():
    requestData = request.get_json()  # Get JSON data from the request body
    data = ChatGPT().CustomChatGptByIndex(requestData['prompt'], index_store_conversation)
    response = jsonify({"data": str(data)})
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

@app.route('/api/documentsindex', methods=['GET'])
def get_documents_index():
    # Call the documentsIndex function and get the result (success flag)
    success = ChatGPT().documentsIndex()
    # Return a JSON response with the success flag
    return jsonify({"status": "success" if success else "error"})

@app.route('/api/documentsgptindex', methods=['GET'])
def get_documents_gpt_index():
    # Call the documentsIndex function and get the result (success flag)
    success = ChatGPT().documentsGptIndex()
    # Return a JSON response with the success flag
    return jsonify({"status": "success" if success else "error"})

# Post chatgpt
@app.route('/api/chatgpt', methods=['POST'])
def post_chatgpt():
    data = request.get_json()  # Get JSON data from the request body
    data = ChatGPT().CustomChatGPT(data['prompt'], store_conversation)
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

# Post bard
@app.route('/api/bard', methods=['POST'])
def post_bard():
    data = request.get_json()  # Get JSON data from the request body
    data = ChatBard().customBard(data['prompt'])
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

if __name__ == '__main__':
    # telegram_bot()
    app.run(debug = True)