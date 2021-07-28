import discord
from discord import message
import requests
import json
import random
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from keep_alive import keep_alive
import os

#main
client = discord.Client()
#api SutanLab
def get_quote():
  response = requests.get("https://api.hadith.sutanlab.id/books/ibnu-majah?range=1500-1700")
  json_data = json.loads(response.text)
  quote = json_data["data"]["hadiths"]
  return(quote)
def get_perawi():
  response = requests.get("https://api.hadith.sutanlab.id/books/ibnu-majah?range=1-300")
  json_data = json.loads(response.text)
  perawi = json_data["data"]["name"] 
  return(perawi)

#word list
sara = ["Yshoes", "awloch", "tuhan kok digantung", "sapi kok disembah"]
sedih = ["sedih", "stress", "depresi", "pusing", "ga tau harus gimana", "Ga tau harus gimana", "banyak masalah"]
janganSedih = ["Janganlah kamu bersedih, sesungguhnya Allah bersama kita.— At-Taubah: 40",
    "Ingatlah, hanya dengan mengingat Allah-lah hati menjadi tenteram.– QS Ar Ra’d: 28", 
    "Ya Allah, aku memohon perlindungan denganMu daripada keluh kesah dan kesedihan, rasa lemah dan kemalasan Aku memohon perlindungan denganMu daripada sifat penakut dan kebakhilam dan aku mohon perlindungan denganMu dari bebanan hutang dan dikuasai seseorang (Hadith riwayat Abu Daud)", "sesungguhnya allah mengetahui yang terbaik untuk mu jadi", " Bukankah Kami telah melapangkan untukmu dadamu? dan Kami telah menghilangkan daripadamu bebanmu, yang memberatkan punggungmu? Dan Kami tinggikan bagimu sebutan (nama)mu, Karena sesungguhnya sesudah kesulitan itu ada kemudahan..” (QS. Al Insyirah: 1-5 )",  "Dan sungguh akan Kami berikan cobaan kepadamu, dengan sedikit ketakutan, kelaparan, kekurangan harta, jiwa dan buah-buahan. Dan berikanlah berita gembira kepada orang-orang yang sabar, (QS. Al Baqarah:155)", ""
        ]
senang = ["senang", "seneng", "bahagia"]
Bersyukur = ["Karena itu, ingatlah kamu kepada-Ku niscaya Aku ingat (pula) kepadamu, dan bersyukurlah kepada-Ku, dan janganlah kamu mengingkari (nikmat)-Ku.-QS Al baqarah: 152", "Tanah yang baik, tanaman-tanamannya tumbuh subur atas izin Allah. Dan tanah yang tidak subur, tanaman-tanamannya hanya tumbuh merana. Demikianlah Kami mengulangi tanda-tanda kebesaran (Kami) bagi orang-orang yang bersyukur. – (Q.S Al-A’raf: 58)", "Dan ingatlah ketika Tuhanmu memaklumkan, “Sesungguhnya jika kamu bersyukur, pasti Aku akan menambahkan nikmat-Ku kepadamu, dan jika kamu mengingkari (nikmat-Ku), maka sesungguhnya azab-Ku sangatlah pedih”. – (Q.S Ibrahim: 7)", "Dan Dialah, Allah yang menundukkan lautan, supaya kamu dapat memakan daging yang segar (ikan) dari hasil laut itu, dan dari lautan itu kamu mengeluarkan perhiasan yang kamu pakai. Dan kamu melihat bahtera berlayar padanya, dan supaya kamu mencari (keuntungan) dari karunia-Nya, dan supaya kamu bersyukur. – (Q.S An-Nahl: 14)", "Dan Allah mengeluarkan kamu dari perut ibumu dalam kondisi tidak mengetahui sesuatupun, dan Dia memberi kamu pendengaran, penglihatan dan hati, agar kamu bersyukur. – (Q.S An-Nahl: 78)", "Maka makanlah yang halal lagi baik dari rezeki yang telah Allah berikan kepadamu, dan bersyukurlah kamu atas nikmat Allah, jika memang hanya kepada-Nya kamu menyembah. – (Q.S An-Nahl: 114)", "Dan Dia (Allah) yang menjadikan malam dan siang silih berganti bagi orang yang ingin mengambil pelajaran atau orang yang ingin bersyukur. – (Q.S Al-Furqan: 62)", "“Allah berfirman dalam hadits qudsi-Nya: “wahai anak Adam, bahwa selama engkau mengingat Aku, berarti engkau mensyukuri Aku, dan apabila engkau melupakan Aku, berarti engkau telah mendurhakai Aku!”. [H.R Thabrani]", ""]
semangat = ["jangan nyerah ya", "semangat terus"]
penyemangat = ["Janganlah kamu bersikap lemah, dan janganlah (pula) kamu bersedih hati, padahal kamulah orang-orang yang paling tinggi (derajatnya), jika kamu orang-orang yang beriman.",
"“Hai orang-orang yang beriman bersabarlah kamu dan kuatkanlah kesabaranmu dan tetaplah bersiap siaga (diperbatasan negerimu) dan bertawakalah kepada Allah supaya kamu beruntung.” (QS Al Imran 200)",
"“Wahai mereka yang beriman, mintalah pertolongan kepada Allah dengan sabar dan solat. Sesungguhnya Allah bersama-sama dengan orang yang sabar.” (Al-Baqarah: 153)",
"“Dan apabila hamba-hamba-Ku bertanya kepadamu tentang Aku, maka (jawablah), bahwasannya Aku adalah dekat. Aku mengabulkan permohonan orang yang berdo’a apabila ia memohon kepada-Ku, maka hendaklah mereka itu memenuhi (segala perintah)Ku dan hendaklah mereka beriman kepada-Ku, agar mereka selalu berada dalam kebenaran”. (QS. Al Baqarah: 186)"
]
#main loop
@client.event
async def on_ready():
    print('{0.user} is now on'.format(client))


# features
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
        myEmbed = discord.Embed(title="DeenBot", description="Version 0.1.7", color=0x00ff00)
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
      await pesan.channel.send('dilarang sara bang!\nDan janganlah kamu memaki sembahan-sembahan yang mereka sembah selain Allah, karena mereka nanti akan memaki Allah dengan melampaui batas tanpa pengetahuan. Demikianlah Kami jadikan setiap umat menganggap baik pekerjaan mereka. Kemudian kepada Tuhan merekalah kembali mereka, lalu Dia memberitakan kepada mereka apa yang dahulu mereka kerjakan [QS: Al-An\'am 108]')
    if any(word in pesan.content for word in semangat):
        await pesan.channel.send(random.choice(penyemangat))
    
keep_alive()
client.run(os.getenv('token'))
