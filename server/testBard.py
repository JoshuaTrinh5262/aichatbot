from bardapi import Bard
import requests
import dotenv
import csv
import os

config = dotenv.dotenv_values("./.env")
bard_token = config['BARD_TOKEN']

file_path = './server/logs/bard_history'

# Open the file in write mode
with open(file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row
    header = ['Promp', 'Response']
    csvwriter.writerow(header)

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", bard_token) 
bard = Bard(token = bard_token, session = session, timeout = 30)

with open(file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    while True:
        user_input = input('User: ')
        if user_input == 'quit':
            print("Exiting the program.")
            break
        
        response = bard.get_answer(user_input)['content']

        csvwriter.writerow([user_input, response])

        print(response)