from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler




SLACK_BOT_TOKEN=""
SLACK_APP_TOKEN=""

app = App(token=SLACK_BOT_TOKEN)

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()