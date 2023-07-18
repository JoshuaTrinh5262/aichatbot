from flask import Flask, jsonify, request
from flask_cors import CORS

from server.CoreAI.chat_gpt import ChatGPT
from CoreAI.telegram_bot import telegram_bot

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

chat = ChatGPT()

#  Post chatgpt by index
@app.route('/api/chatgptbyindex', methods = ['POST'])
def post_chatgptbyindex():
    requestData = request.get_json()  # Get JSON data from the request body
    data = chat.CustomChatGptByIndex(requestData['prompt'], index_store_conversation)
    return str(data)

# Post chatgpt
@app.route('/api/chatgpt', methods=['POST'])
def post_chatgpt():
    data = request.get_json()  # Get JSON data from the request body
    data = chat.CustomChatGPT(data['prompt'], store_conversation)
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

# Post bard
@app.route('/api/bard', methods=['POST'])
def post_bard():
    data = request.get_json()  # Get JSON data from the request body
    data = chat.customBard(data['prompt'])
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

if __name__ == '__main__':
    app.run(debug = True)