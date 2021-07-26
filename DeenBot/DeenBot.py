import discord
from discord import message
import requests
from discord.ext import commands
import json
import random
client = discord.Client()

sedih = ["sedih", "stress", "depresi", "pusing"]
janganSedih = ["Janganlah kamu bersedih, sesungguhnya Allah bersama kita.— At-Taubah: 40",
    "Ingatlah, hanya dengan mengingat Allah-lah hati menjadi tenteram.– QS Ar Ra’d: 28", 
    "Ya Allah, aku memohon perlindungan denganMu daripada keluh kesah dan kesedihan, rasa lemah dan kemalasan Aku memohon perlindungan denganMu daripada sifat penakut dan kebakhilam dan aku mohon perlindungan denganMu dari bebanan hutang dan dikuasai seseorang (Hadith riwayat Abu Daud)"
        ]
senang = ["senang"]
Bersyukur = ["Karena itu, ingatlah kamu kepada-Ku niscaya Aku ingat (pula) kepadamu, dan bersyukurlah kepada-Ku, dan janganlah kamu mengingkari (nikmat)-Ku. -QS Al baqarah: 152"]

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
    if any(word in pesan.content for word in senang):
        await pesan.channel.send(random.choice(Bersyukur))



client.run('TOKEN')
