from bardapi import Bard
import dotenv
import requests

class ChatBard: 
    def __init__(self):
        config = dotenv.dotenv_values("./.env")
        self.bard_token = config['BARD_TOKEN']
        self.bard_token_ts = config['BARD_TOKEN_TS']
        self.bard_token_cc = config['BARD_TOKEN_CC']

    def customBard(self, user_input):
        try:
            session = requests.Session()
            session.headers = {
                "Host": "bard.google.com",
                "X-Same-Domain": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Origin": "https://bard.google.com",
                "Referer": "https://bard.google.com/",
            }

            session.cookies.set("__Secure-1PSID", self.bard_token)
            # session.cookies.set("__Secure-1PSIDTS", self.bard_token_ts)
            # session.cookies.set("__Secure-1PSIDCC", self.bard_token_cc)
            bard = Bard(token = self.bard_token, session = session)
            response = bard.get_answer(user_input)['content']
            return response
        except Exception as e:
            return f"An error occurred: {str(e)}"
