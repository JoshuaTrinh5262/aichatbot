import openai
import dotenv

class ChatGPT: 
    vopenai = openai
    
    # Constructor (initialize instance)
    def __init__(self):
        # Instance attributes
        config = dotenv.dotenv_values(".env")
        self.vopenai.api_key = config['OPENAI_API_KEY']

    # print(store_conversation)
    def CustomChatGPT(self, user_input, store_conversation):
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
        self.saveChatHistory(store_conversation)
        return ChatGPT_reply

    def saveChatHistory(self, conversation):
        with open("./store/chat_history.txt", "w") as file:
            file.write("\n".join(conversation))


    def testapi(self):
        return "AAAA"