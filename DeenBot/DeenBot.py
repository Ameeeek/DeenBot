import discord
from discord import message
import requests
import json
import random
from keep_alive import keep_alive
import os
#main
client = discord.Client()
#api SutanLab
def get_quote():
  response = requests.get("https://api.hadith.sutanlab.id/books/ibnu-majah?range=1-150")
  json_data = json.loads(response.text)
  quote = json_data["data"]["hadiths"]
  return(quote)
def get_perawi():
  response = requests.get("https://api.hadith.sutanlab.id/books/ibnu-majah?range=1-300")
  json_data = json.loads(response.text)
  perawi = json_data["data"]["name"] 
  return(perawi)

#word list
sara = ["Yshoes", "awloch"]
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


# features
# ban

# wordlist
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
    if pesan.content.startswith('--version'):
        myEmbed = discord.Embed(title="DeenBot", description="Version 0.1.5", color=0x00ff00)
        myEmbed.add_field(name="date released", value="26/7/2021", inline="false")
        myEmbed.set_footer(text="dunia is temporary, deen is forever")
        myEmbed.set_author(name="Amek, Bluxe")
        await pesan.channel.send(embed=myEmbed)
    if pesan.content.startswith('hadist of the day'):
      quote = get_quote()
      perawi = get_perawi()
      await pesan.channel.send(perawi)
      await pesan.channel.send(random.choice(quote)["id"])
    if any(word in pesan.content for word in sara):
      await pesan.channel.send('dilarang sara bang!')
    
    
keep_alive()
client.run(os.getenv('token'))
