import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import datetime

client=commands.Bot(command_prefix=".")
while True:
    print("Input token:")
    token_input = input()
    if token_input != '':
        token = token_input
        break

user_id = 00000000000000000 #the user id of a person you want to get call history 

@client.event
async def on_ready():
    user = await client.fetch_user(user_id)
    channel = user.dm_channel
    messages = await channel.history(oldest_first= True, limit=99999).flatten() #adjust limit depending on how many messages you have with the user
    total = datetime.timedelta(0)
    for message in messages:
        if str(message.type) == "MessageType.call":
            if message.call.call_ended:
                total += message.call.duration
    print(f'You spend {str(total)} in call with {user.name}')
client.run(token, bot=False)