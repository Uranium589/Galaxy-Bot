import discord
import asyncio
import os

client = discord.Client()

token = "ODk1NTY4MzM5MzE1ODU5NDY3.YV6dAg.wUKpFF9j_4J5DOVZ1Mt0bsvKfBYODk1NTY4MzM5MzE1ODU5NDY3.YV6dAg.wUKpFF9j_4J5DOVZ1Mt0bsvKfBY"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('Galaxy Bot')
    await client.change_presence(status=discord.Status.online, activity=game)


client.run(token)
