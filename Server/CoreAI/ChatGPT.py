import openai
import dotenv
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

class ChatGPT: 
    vopenai = openai
    index = []
    # Constructor (initialize instance)
    def __init__(self):
        # Instance attributes
        config = dotenv.dotenv_values("./.env")
        self.vopenai.api_key = config['OPENAI_API_KEY']
        os.environ["OPENAI_API_KEY"] = config['OPENAI_API_KEY']
        self.documentsIndex()

    def CustomChatGptByIndex(self, user_input, store_conversation):
        
        query_engine = self.index.as_query_engine()
        store_conversation.append("User: " + user_input)
        response = query_engine.query(user_input)
        print(response)
        store_conversation.append("Ai: " + response.response.replace("\n", ""))
        print(store_conversation)
        self.saveChatHistory(store_conversation, 'index_chat_history')
        return response

    def CustomChatGPT(self, user_input, store_conversation):
        print(self.vopenai.api_key)
        store_conversation.append("User: " + user_input)
        response = self.vopenai.Completion.create(
            model = "text-davinci-003",
            prompt = "\n".join(store_conversation),
            max_tokens = 500,
            n = 1,
            stop = None,
            temperature = 0.5,
        )

        ChatGPT_reply = response.choices[0].text.strip()
        store_conversation.append(ChatGPT_reply)
        self.saveChatHistory(store_conversation, 'chat_history')
        return ChatGPT_reply

    def saveChatHistory(self, conversation, file_name):
        file_path = "./server/logs/" + file_name + ".txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(conversation))


    def testapi(self):
        return "AAAA"
    
    def documentsIndex(self):
        documents = SimpleDirectoryReader('./server/store').load_data()
        self.index = GPTVectorStoreIndex.from_documents(documents)