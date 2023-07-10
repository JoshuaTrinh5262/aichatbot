import dotenv
import slack_sdk
from flask import Flask
# from flask_ngrok import run_with_ngrok
from slackeventsapi import SlackEventAdapter

# Create a Flask app
app = Flask(__name__)
# run_with_ngrok(app)   # Start ngrok when app is run

# Initialize the Slack Web API client
config = dotenv.dotenv_values("./.env")
slack_token = config['SLACK_API_TOKEN']
signing_secret = config['SIGNING_SECRET']

slack_event_adapter = SlackEventAdapter(signing_secret, '/slack/events', app)

client = slack_sdk.WebClient(token = slack_token)

# Event handler for incoming messages
def event_handler():
    # Respond to the user
    response = client.chat_postMessage(channel = '#test', text = "Hello World")

@app.route('/')
def helloworld():
    return "hello world"    

if __name__ == '__main__':
    app.run(
        # debug = True,
        # port = 5000, # Run the Flask app on port 5000
        # host = '0.0.0.0'
    )