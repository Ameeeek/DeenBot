import discord
from discord import message
import requests
from discord.ext import commands
import json
import random
from keep_alive import keep_alive
import os
#main
client = discord.Client()


# sutan lab api
def get_hadiths():
    response = requests.get("https://api.hadith.sutanlab.id/books/muslim?range=1-150")
    json_data = json.load(response.text)
    hadith = json_data["data"]["id"]
    return(hadith)

#word list
sedih = ["sedih", "stress", "depresi", "pusing"]
janganSedih = ["Janganlah kamu bersedih, sesungguhnya Allah bersama kita.— At-Taubah: 40",
    "Ingatlah, hanya dengan mengingat Allah-lah hati menjadi tenteram.– QS Ar Ra’d: 28", 
    "Ya Allah, aku memohon perlindungan denganMu daripada keluh kesah dan kesedihan, rasa lemah dan kemalasan Aku memohon perlindungan denganMu daripada sifat penakut dan kebakhilam dan aku mohon perlindungan denganMu dari bebanan hutang dan dikuasai seseorang (Hadith riwayat Abu Daud)"
        ]
senang = ["senang"]
Bersyukur = ["Karena itu, ingatlah kamu kepada-Ku niscaya Aku ingat (pula) kepadamu, dan bersyukurlah kepada-Ku, dan janganlah kamu mengingkari (nikmat)-Ku.-QS Al baqarah: 152"]
#main loop
@client.event
async def on_ready():
    print('{0.user} is now on'.format(client))
#embed message


# features
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
    if pesan.content.startswith('hadith'):
        hadith = get_hadiths()
        await pesan.channel.send(hadith)
    if pesan.content.startswith('--version'):
        myEmbed = discord.Embed(title="DeenBot", description="Version 0.1.3", color=0x00ff00)
        myEmbed.add_field(name="date released", value="26/7/2021", inline="false")
        myEmbed.set_footer(text="dunia is temporary, deen is forever")
        myEmbed.set_author(name="Amek, Bluxe")
        await pesan.channel.send(embed=myEmbed)


keep_alive()
client.run(os.getenv('token'))
