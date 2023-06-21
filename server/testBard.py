from bardapi import Bard
import dotenv

config = dotenv.dotenv_values("./.env")
bard_token = config['BARD_TOKEN']

bard = Bard(token = bard_token)
while True:
    user_input = input('User: ')
    if user_input == 'quit':
        print("Exiting the program.")
        break
    response = bard.get_answer(user_input)['content']
    print(response)