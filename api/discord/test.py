import discord
import asyncio
import credential as c

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = c.token

# Replace 'YOUR_CHANNEL_ID' with your Discord channel ID
CHANNEL_ID = c.channel_id

# Create a client instance
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Get the channel by ID and send a message
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send('Hello!')

    # Close the connection once the message is sent
    await client.close()

# Run the client
client.run(TOKEN)
