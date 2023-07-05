import discord

token = {
    "TOKEN":"Put your Bot Token, just go to Discord Developer portal and create your bot and then copy his token!(If your not able to do this on your own please see some youtube videos)"
}

intents = discord.Intents.default()
intents.message_content = True  # Defining the intentions of your bot(In this case we just want to write messages

client = discord.Client(intents=intents)

TOKEN = token.get("TOKEN")

@client.event
async def on_ready():  # When the bot is ready print
    print(f"{client.user} READY!")

@client.event
async def on_message(message):  # If the bot gets a message then...
    channel = message.channel
    geral_channel_id = "Your general channel id(on discord click with the right button on the channel you want and copy id)"
    geral2_channel_id = "Your secondary channel id(on discord click with the right button on the channel you want and copy id)"
    geral_channel = client.get_channel(geral_channel_id)  # Getting the channel by the id
    geral2_channel = client.get_channel(geral2_channel_id)  # Getting the channel by the id

    if message.author == client.user:  # If the message author is the Bot then do nothing
        return

    if message.content.startswith("/hi"):  # If the message starts with "/hi" the print...
        await message.channel.send(f"Hi {message.author}!")

client.run(TOKEN)  # Runs the Bot