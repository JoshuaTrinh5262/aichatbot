import dotenv
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

config = dotenv.dotenv_values("./.env")
os.environ["OPENAI_API_KEY"] = config['OPENAI_API_KEY']
store_conversation = []

while(input != 'quit'):
    documents = SimpleDirectoryReader('./server/store').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    user_input = input("Enter your question : ")
    store_conversation.append("User: " + user_input)
    response = query_engine.query(input)
    store_conversation.append("AI: " + user_input)
    print(response)

with open("./server/store/chat_history.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(store_conversation))