import discord
from chatterbot import ChatBot
import openai

client = discord.Client()

chatterbot = ChatBot("Discord ChatterBot")

openai.api_key = "openai-api-key"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = chatterbot.get_response(message.content)

    response = response.text
    prompt = f"{message.content}\n"

    openai_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    openai_response = openai_response.choices[0].text

    await message.channel.send(f"{response} {openai_response}")

client.run("your-discord-token")
