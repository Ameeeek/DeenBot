import discord
import time
import random
from discord.ext import commands
from discord.ext.commands.core import has_permissions
client = discord.Client()
import json
import requests
import os
from keep_alive import keep_alive

def get_quote():
  response = requests.get("https://api.hadith.sutanlab.id/books/ibnu-majah?range=2600-2900")
  json_data = json.loads(response.text)
  quote = json_data["data"]["hadiths"]
  return(quote)
def get_perawi():
  response = requests.get("https://api.hadith.sutanlab.id/books/ibnu-majah?range=2600-2900")
  json_data = json.loads(response.text)
  perawi = json_data["data"]["name"] 
  return(perawi)

#wordlist
sara = ["Yshoes", "awloch", "tuhan kok digantung", "sapi kok disembah","icelamp", "kris10", "byksw", "krislam", "boedha", "jasjus kristoes", "jasjus", "hambaque", "twohand", "toehan"]
sedih = [".sedih", ".stress", ".depresi", ".pusing",".sad"]
janganSedih = ["Janganlah kamu bersedih, sesungguhnya Allah bersama kita.— At-Taubah: 40",
    "Ingatlah, hanya dengan mengingat Allah-lah hati menjadi tenteram.– QS Ar Ra’d: 28", 
    "Ya Allah, aku memohon perlindungan denganMu daripada keluh kesah dan kesedihan, rasa lemah dan kemalasan Aku memohon perlindungan denganMu daripada sifat penakut dan kebakhilam dan aku mohon perlindungan denganMu dari bebanan hutang dan dikuasai seseorang (Hadith riwayat Abu Daud)", "sesungguhnya allah lebih mengetahui yang terbaik untuk mu bisa maka bersabarlah", " Bukankah Kami telah melapangkan untukmu dadamu? dan Kami telah menghilangkan daripadamu bebanmu, yang memberatkan punggungmu? Dan Kami tinggikan bagimu sebutan (nama)mu, Karena sesungguhnya sesudah kesulitan itu ada kemudahan..” (QS. Al Insyirah: 1-5 )",  "Dan sungguh akan Kami berikan cobaan kepadamu, dengan sedikit ketakutan, kelaparan, kekurangan harta, jiwa dan buah-buahan. Dan berikanlah berita gembira kepada orang-orang yang sabar, (QS. Al Baqarah:155)", 
    "\"Saad bin Abi Waqqash berkata, \"Aku bertanya kepada Rasulullah saw., 'Ya Rasulullah, siapakah orang yang paling berat ujian dan cobaannya?' Nabi saw. menjawab, 'Para nabi, kemudian yang menyerupai mereka, dan yang menyerupai mereka. Seseorang diuji menurut kadar agamanya. Kalau agamanya tipis (lemah), dia diuji sesuai dengan itu (ringan); dan bila imannya kokoh, dia diuji sesuai itu (keras). Seorang diuji terus-menerus sehingga dia berjalan di muka bumi bersih dari dosa-dosa'.\" (HR. Bukhari)",]
senang = [".senang", ".bahagia", ".bersyukur"]
Bersyukur = ["Karena itu, ingatlah kamu kepada-Ku niscaya Aku ingat (pula) kepadamu, dan bersyukurlah kepada-Ku, dan janganlah kamu mengingkari (nikmat)-Ku.-QS Al baqarah: 152", "Tanah yang baik, tanaman-tanamannya tumbuh subur atas izin Allah. Dan tanah yang tidak subur, tanaman-tanamannya hanya tumbuh merana. Demikianlah Kami mengulangi tanda-tanda kebesaran (Kami) bagi orang-orang yang bersyukur. – (Q.S Al-A’raf: 58)", "Dan ingatlah ketika Tuhanmu memaklumkan, “Sesungguhnya jika kamu bersyukur, pasti Aku akan menambahkan nikmat-Ku kepadamu, dan jika kamu mengingkari (nikmat-Ku), maka sesungguhnya azab-Ku sangatlah pedih”. – (Q.S Ibrahim: 7)", "Dan Dialah, Allah yang menundukkan lautan, supaya kamu dapat memakan daging yang segar (ikan) dari hasil laut itu, dan dari lautan itu kamu mengeluarkan perhiasan yang kamu pakai. Dan kamu melihat bahtera berlayar padanya, dan supaya kamu mencari (keuntungan) dari karunia-Nya, dan supaya kamu bersyukur. – (Q.S An-Nahl: 14)", "Dan Allah mengeluarkan kamu dari perut ibumu dalam kondisi tidak mengetahui sesuatupun, dan Dia memberi kamu pendengaran, penglihatan dan hati, agar kamu bersyukur. – (Q.S An-Nahl: 78)", "Maka makanlah yang halal lagi baik dari rezeki yang telah Allah berikan kepadamu, dan bersyukurlah kamu atas nikmat Allah, jika memang hanya kepada-Nya kamu menyembah. – (Q.S An-Nahl: 114)", "Dan Dia (Allah) yang menjadikan malam dan siang silih berganti bagi orang yang ingin mengambil pelajaran atau orang yang ingin bersyukur. – (Q.S Al-Furqan: 62)", "“Allah berfirman dalam hadits qudsi-Nya: “wahai anak Adam, bahwa selama engkau mengingat Aku, berarti engkau mensyukuri Aku, dan apabila engkau melupakan Aku, berarti engkau telah mendurhakai Aku!”. [H.R Thabrani]", ""]
semangat = [".semangat",".Semangat!"]
penyemangat = ["Janganlah kamu bersikap lemah, dan janganlah (pula) kamu bersedih hati, padahal kamulah orang-orang yang paling tinggi (derajatnya), jika kamu orang-orang yang beriman.",
"“Hai orang-orang yang beriman bersabarlah kamu dan kuatkanlah kesabaranmu dan tetaplah bersiap siaga (diperbatasan negerimu) dan bertawakalah kepada Allah supaya kamu beruntung.” (QS Al Imran 200)",
"“Wahai mereka yang beriman, mintalah pertolongan kepada Allah dengan sabar dan solat. Sesungguhnya Allah bersama-sama dengan orang yang sabar.” (Al-Baqarah: 153)",
"“Dan apabila hamba-hamba-Ku bertanya kepadamu tentang Aku, maka (jawablah), bahwasannya Aku adalah dekat. Aku mengabulkan permohonan orang yang berdo’a apabila ia memohon kepada-Ku, maka hendaklah mereka itu memenuhi (segala perintah)Ku dan hendaklah mereka beriman kepada-Ku, agar mereka selalu berada dalam kebenaran”. (QS. Al Baqarah: 186)"
]
cape = [".cape"]
JanganCape = ["Janganlah kamu bersikap lemah dan janganlah pula kamu bersedih hati, padahal kamulah orang-orang yang paling tinggi derajatnya jika kamu orang-orang yang beriman. QS. Ali-Imran [3: 139]", "Apakah manusia itu mengira bahwa mereka dibiarkan (saja) mengatakan: \"Kami telah beriman\", sedang mereka tidak diuji lagi? Dan sesungguhnya kami telah menguji orang-orang yang sebelum mereka, maka sesungguhnya Allah mengetahui orang-orang yang benar dan sesungguhnya Dia mengetahui orang-orang yang dusta. QS. Al Ankabut [29: 2-3]"]
cewe = [".cewe", ".wanita", ".perempuan"]
HargaiCewe = ["Dunia adalah perhiasan dan sebaik-baik perhiasan adalah wanita sholihah. (HR. Muslim).", "Hai orang-orang yang beriman, tidak halal bagi kamu mempusakai wanita dengan jalan paksa dan janganlah kamu menyusahkan mereka karena hendak mengambil kembali sebagian dari apa yang telah kamu berikan kepadanya, terkecuali bila mereka melakukan pekerjaan keji yang nyata. Dan bergaullah dengan mereka secara patut. Kemudian bila kamu tidak menyukai mereka, (maka bersabarlah) karena mungkin kamu tidak menyukai sesuatu, padahal Allah menjadikan padanya kebaikan yang banyak. (QS. An Nisa [4]: 19)", "Sesungguhnya orang-orang yang menuduh wanita yang baik-baik, yang lengah (tidak terbersit di benaknya berbuat zina) lagi beriman, mereka dilaknat di dunia dan akhirat, dan bagi mereka azab yang besar. [QS. An-Nuur: 23].", "Sesungguhnya wanita diciptakan dari tulang rusuk. Dan sungguh bagian yang paling bengkok dari tulang rusuk adalah yang paling atasnya. Bila engkau ingin meluruskannya, engkau akan mematahkannya. Dan jika engkau ingin bersenang-senang dengannya, engkau bisa bersenang-senang namun padanya ada kebengkokan. [HR. Al-Bukhari no. 3331 dan Muslim no. 3632]."]
insecure = [".insecure", ".Insecure"]
janganInsecure = ["\"Allah tidak melihat bentuk rupa dan harta benda kalian, tapi Dia melihat hati dan amal kalian.\" - Nabi Muhammad SAW", "\"Ketahuilah bahwa kemenangan bersama kesabaran, kelapangan bersama kesempitan, dan kesulitan bersama kemudahan\". (HR Tirmidzi)"]












#kick 
class Moderation(commands.Cog, description="commands for moderation use $ as prefix"):
    #kick
    @commands.has_permissions(kick_members=True)
    @commands.command(name='kick', help='kicks a member from the server')
    async def kick(self, ctx, user: discord.Member, *, reason='No reason provided'):
        kick_dm  = discord.Embed(
        title='You have Been kicked! :door:',
        description = f"You were kicked from {ctx.message.guild.name}!!**\n \n Reason:{reason}**\n "
        )


        kick_msg = discord.Embed(
            title = f"kicked {user}",
            description = f"reason {reason}\nBy: {ctx.author.mention}"
        )

        await user.send(embed=kick_dm)
        await user.kick(reason=reason)
        await ctx.channel.send(embed=kick_msg)

    @commands.has_permissions(ban_members=True)
    @commands.command(name='ban', help='kicks a member from the server')
    async def ban(self, ctx, user: discord.Member, *, reason='No reason provided'):
        ban_msg = discord.Embed(
            title = f"terban {user}",
            description = f"reason {reason}\nBy: {ctx.author.mention}"
        )

        await user.send(embed=ban_msg)
        await user.ban(reason=reason)
        await ctx.channel.send(embed=ban_msg)

bot = commands.Bot(command_prefix = "$")
@bot.event 
async def on_ready():
    activity=discord.Activity(type=discord.ActivityType.watching, name='Allah is watching')
    await bot.change_presence(activity=activity)
    print("bot ready!")
@bot.event 
async def on_message(message):
    print(f'{message.author}: {message.content}')
    await bot.process_commands(message)
    if any(word in message.content for word in senang):
        await message.channel.send(random.choice(Bersyukur))
    if message.content.startswith('.hadist of the day'):
        quote = get_quote()
        perawi = get_perawi()
        await message.channel.send(perawi)
        await message.channel.send(random.choice(quote)["id"])
    if any(word in message.content for word in sara):
        await message.channel.send(f' jangan sara bang\nDan janganlah kamu memaki sembahan-sembahan yang mereka sembah selain Allah, karena mereka nanti akan memaki Allah dengan melampaui batas tanpa pengetahuan. Demikianlah Kami jadikan setiap umat menganggap baik pekerjaan mereka. Kemudian kepada Tuhan merekalah kembali mereka, lalu Dia memberitakan kepada mereka apa yang dahulu mereka kerjakan. (QS Al An\'am 108)')
    if any(word in message.content for word in cewe):
        await message.channel.send(random.choice(HargaiCewe))
    if any(word in message.content for word in cape):
        await message.channel.send(random.choice(JanganCape))
    if any(word in message.content for word in sedih):
        await message.channel.send(random.choice(janganSedih))
    if any(word in message.content for word in semangat):
        await message.channel.send(random.choice(penyemangat))
    if message.content.startswith('ingfokan sirkel'):
        await message.channel.send('Bertakwalah kepada Allah di mana pun kamu berada, dan ikutilah perbuatan buruk dengan perbuatan baik niscaya itu menghapusnya, dan bergaullah dengan manusia dengan akhlak yang luhur. (HR. Tirmidzi)')
    if message.content.startswith('.puasa'):
        await message.channel.send('"Sesungguhnya puasa itu tidak lain adalah perisai. Apabila salah seorang di antara kamu sedang berpuasa maka janganlah berkata kotor dan jangan pula bertindak bodoh. Dan jika ada seorang yang menyerangnya atau mencacinya maka hendaklah dia mengatakan "Sesungguhnya aku berpuasa, sesungguhnya aku berpuasa." (HR. Bukhari dan Muslim)')
    if any(word in message.content for word in insecure):
        await message.channel.send(random.choice(janganInsecure))
    if message.content.startswith('.version'):
        myEmbed = discord.Embed(title="DeenBot", description="Version 1", color=0x00ff00)
        myEmbed.add_field(name="date released", value="26/7/2021", inline="false")
        myEmbed.set_footer(text="dunia is temporary, deen is forever")
        myEmbed.set_author(name="Amek, Bluxe")
        await message.channel.send(embed=myEmbed)
    if message.content.startswith('.darkjoke'):
      await message.channel.send('"Dan jika kamu tanyakan kepada mereka (tentang apa yang mereka lakukan itu), tentulah mereka akan menjawab, ‘Sesungguhnya kami hanyalah bersenda gurau dan bermain-main saja’. Katakanlah, ‘Apakah dengan Allah, ayat-ayat-Nya, dan Rasul -Nya kamu selalu berolok-olok?" (QS at-Taubah [9]: 65).')
      await message.channel.send('"Tidak usah kamu minta maaf, karena kamu kafir sesudah beriman. Jika Kami memaafkan segolongan kamu (lantaran mereka taubat), niscaya Kami akan mengazab golongan (yang lain) disebabkan mereka adalah orang-orang yang selalu berbuat dosa." (QS at-Taubah [9]:66)')
    if message.content.startswith('.DarkJoke'):
      await message.channel.send('Dan tinggalkanlah orang-orang yang menjadikan agama mereka sebagai main-main dan senda gurau, dan mereka telah ditipu oleh kehidupan dunia. Peringatkanlah (mereka) dengan al-Quran itu agar masing-masing diri tidak dijerumuskan (ke dalam neraka), karena perbuatannya sendiri. Tidak akan ada baginya pelindung selain Allâh dan tidak pula pemberi syafaat. Meskipun dia menebus dengan segala macam tebusan pun, niscaya tidak akan diterima itu darinya. Mereka itulah orang-orang yang dijerumuskan (ke dalam neraka) karena apa-apa yang telah mereka lakukan. Bagi mereka (disediakan) minuman dari air yang sedang mendidih dan adzab yang pedih disebabkan kekafiran mereka dahulu. [Al-An’am/6:70]')
 
bot.add_cog(Moderation())
keep_alive()
bot.run(os.getenv('token'))
