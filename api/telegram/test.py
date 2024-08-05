import requests
import credential as c

# Replace with your bot token and chat ID
BOT_TOKEN = c.bot_token
CHAT_ID = c.chat_id
MESSAGE = 'Hello from your Telegram bot!'

# The URL for sending messages via the Telegram bot
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

# The payload to send to the API
payload = {
    'chat_id': CHAT_ID,
    'text': MESSAGE
}

# Send the message
response = requests.post(URL, data=payload)

# Check the response
if response.status_code == 200:
    print("Message sent successfully")
else:
    print(f"Failed to send message: {response.status_code}, {response.text}")
