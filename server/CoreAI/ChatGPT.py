import openai
import dotenv
import os
from bardapi import Bard
import requests
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

class ChatGPT: 
    vopenai = openai
    index = []
    # Constructor (initialize instance)
    def __init__(self):
        # Instance attributes
        config = dotenv.dotenv_values("./.env")
        self.vopenai.api_key = config['OPENAI_API_KEY']
        self.bard_token = config['BARD_TOKEN']
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

    def customBard(self, user_input):
        session = requests.Session()
        session.headers = {
                    "Host": "bard.google.com",
                    "X-Same-Domain": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Origin": " https://bard.google.com ",
                    "Referer": " https://bard.google.com/ ",
                }
        
        session.cookies.set("__Secure-1PSID", self.bard_token) 
        bard = Bard(token = self.bard_token, session = session, timeout = 30)
        response = bard.get_answer(user_input)['content']
        return response

    def saveChatHistory(self, conversation, file_name):
        file_path = "./server/logs/" + file_name + ".txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(conversation))


    def testapi(self):
        return "AAAA"
    
    def documentsIndex(self):
        documents = SimpleDirectoryReader('./server/store').load_data()
        self.index = GPTVectorStoreIndex.from_documents(documents)