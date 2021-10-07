import discord
import asyncio

client = discord.Client()

token = "ODk1NTY4MzM5MzE1ODU5NDY3.YV6dAg.JTEiTjkiqzQixpxbTAgnDcoFQyM"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('Galaxy Bot')
    await client.change_presence(status=discord.Status.online, activity=game)


client.run(token)