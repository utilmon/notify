import requests
from . import credential as c

# Replace with your bot token and chat ID
BOT_TOKEN = c.bot_token
CHAT_ID = c.chat_id

# The URL for sending messages via the Telegram bot
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def test():
    MESSAGE = "Hello from your Telegram bot!"
    # The payload to send to the API
    payload = {"chat_id": CHAT_ID, "text": MESSAGE}

    # Send the message
    response = requests.post(URL, data=payload)

    # Check the response
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")


def send_message(message: str):
    # The payload to send to the API
    payload = {"chat_id": CHAT_ID, "text": message}

    # Send the message
    return requests.post(URL, data=payload)


if __name__ == "__main__":
    test()
