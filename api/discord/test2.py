import requests
import credential as c

# Replace with your webhook URL
WEBHOOK_URL = c.webhook_url

# The message to send
message = {
    "content": "Hello from your webhook!"
}

# Send the message
response = requests.post(WEBHOOK_URL, json=message)

# Check the response
if response.status_code == 204:
    print("Message sent successfully")
else:
    print(f"Failed to send message: {response.status_code}, {response.text}")
