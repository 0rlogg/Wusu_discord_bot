import discord
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('.hello'):
            await message.channel.send('Hello_human')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('.meme'):
            await message.channel.send(get_meme())    

intents = discord.Intents.default()
intents.message_content = True
client = Client (intents=intents)
client.run(#token
    )