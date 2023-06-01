import openai
import dotenv
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

class ChatGPT: 
    vopenai = openai

    # Constructor (initialize instance)
    def __init__(self):
        # Instance attributes
        config = dotenv.dotenv_values("./.env")
        self.vopenai.api_key = config['OPENAI_API_KEY']
        os.environ["OPENAI_API_KEY"] = config['OPENAI_API_KEY']

    def CustomChatGptByIndex(self, user_input, store_conversation):
        documents = SimpleDirectoryReader('./server/store').load_data()
        index = GPTVectorStoreIndex.from_documents(documents)
        
        query_engine = index.as_query_engine()
        store_conversation.append("User: " + user_input)
        response = query_engine.query(user_input)
        store_conversation.append(response)
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
        with open("./server/store/"+ file_name + ".txt", "w", encoding="utf-8") as file:
            file.write("\n".join(conversation))


    def testapi(self):
        return "AAAA"