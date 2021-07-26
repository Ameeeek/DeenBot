import discord
from discord import message
import requests
from discord.ext import commands
import json
import random
client = discord.Client()

sedih = ["sedih", "stress", "depresi"]
janganSedih = ["Janganlah kamu bersedih, sesungguhnya Allah bersama kita.— At-Taubah: 40",
    "Ingatlah, hanya dengan mengingat Allah-lah hati menjadi tenteram.– QS Ar Ra’d: 28",
        ]

@client.event
async def on_ready():
    print('{0.user} is now on'.format(client))

@client.event
async def on_message(pesan):
    if pesan.author == client.user:
        return
    if pesan.content.startswith('assalamualaikum'):
        await pesan.channel.send('Wa\'alaikumussalam')
    if any(word in pesan.content for word in sedih):
        await pesan.channel.send(random.choice(janganSedih))


client.run('ODY4OTI3MzkzOTYyODE1NTQ4.YP2xsg.QX8Cbr9zVKDqPAXejdgCd8kffNw')