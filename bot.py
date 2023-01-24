import discord
from discord.ext import commands
import time
from mcstatus import JavaServer
from discord.ext import tasks
from  config import token, serverip, onlinemessage, offlinemessage, channelid

bot = commands.Bot('!')
def isserveron(ip):
    try:
        server = JavaServer.lookup(ip)
        server.ping()
        return 1
    except:
        return 2
@bot.event
async def on_ready():
    print("Bot is online!")
    time.sleep(5)
    test.start()

@tasks.loop(minutes=5)
async def test():
    mamamia = isserveron(serverip)
    time.sleep(5)
    if mamamia  == 1:
        server2 = JavaServer.lookup(serverip)
        status2 = server2.status()
        channel = bot.get_channel(channelid)
        await channel.edit(name= onlinemessage +f" {status2.players.online}")
        print(f"Server stats updated, online players: {status2.players.online}")
    else:
        channel = bot.get_channel(1010605428700352728)
        await channel.edit(name= offlinemessage)
        print(f"Server stats updated, Server is offline :(")
bot.run(token)