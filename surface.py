import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import requests 
import json
from app.chatgpt_ai.openai import chatgpt_response 


load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)



class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as: ", self.user)

@bot.event
async def on_message(message):
    print(message.content)
    if message.author == bot.user:
        return
    command, user_message=None, None

    for text in ['/ai','/bot', '/chatgpt']:
        if message.content.startswith(text):
            command=message.content.split(' ')[0]
            user_message=message.content.replace(text, '')
            print(command, user_message)
    
    if command == '/ai' or command =='/bot' or command == '/chatgpt':
        bot_response = chatgpt_response(prompt=user_message)
        await message.channel.send(f"Answer: {bot_response}")

client = MyClient(intents=intents)

bot.run(TOKEN)
