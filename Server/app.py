from urllib import response
from CoreAI.ChatGPT import ChatGPT
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Open the text file in read mode
with open("server/store/chat_history.txt", "r") as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Open the text file in read mode
with open("server/store/index_chat_history.txt", "r") as file:
    # Read all lines from the file into a list
    index_lines = file.readlines()

#load chat_history here
store_conversation = [line.strip() for line in lines]
index_store_conversation = [line.strip() for line in index_lines]

chat = ChatGPT()

@app.route('/')
def index():
    # response = Response('Hello, World!')
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

#  Post chatgpt by index
@app.route('/api/chatgptbyindex', methods=['Post'])
def post_chatgptbyindex():
    data = request.get_json()  # Get JSON data from the request body
    print(data['prompt'])
    data = chat.CustomChatGptByIndex(data['prompt'], index_store_conversation)
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

# Post chatgpt
@app.route('/api/chatgpt', methods=['Post'])
def post_chatgpt():
    data = request.get_json()  # Get JSON data from the request body
    print(data['prompt'])
    data = chat.CustomChatGPT(data['prompt'], store_conversation)
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

# Post chatgpt
@app.route('/api/testchatgpt', methods=['Post'])
def post_testchatgpt():
    data = request.get_json()  # Get JSON data from the request body
    # print(data['prompt'])
    # data = chat.CustomChatGPT(data['prompt'], store_conversation)
    # data = chat.testapi()
    print(data)
    response = jsonify(data)
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response    

if __name__ == '__main__':
    app.run(debug=True) 