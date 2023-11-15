import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv('.env') 


SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)

@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")

def run_slack_app():
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()