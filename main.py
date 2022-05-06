# kril lotin bot kutubxonalari
from transliterate import to_cyrillic,to_latin
import telebot
# Kursni aniqlovchi kutubxonalarni chaqirish
import math
import requests
from pprint import pprint as print
# Sana vaqtni aniqlash uchun kutubxonalar
import datetime as dt

# SANA VA VAQT
hozir=dt.datetime.now()
sana=hozir.date()




# KURSNI ANIQLASH UCHUN KOD
kod =  'bfb4ae90a65e63cc7a717986'  #API dan olgan kodim ExchangeRate-API
davlat='USD' #AQSH USD, ROSIYA RUB, UZB UZS,
#url ga murojat qilib Kursni aniqlash.
url=f"https://v6.exchangerate-api.com/v6/{kod}/pair/{davlat}/UZS"
javob = requests.get(url) # Saytdan qaytgan javob <requests> taminlayapmiz
taxlangan = javob.json()
kurs =taxlangan['conversion_rate']
# print(f"Bugungi kurs: 1-{davlat} = {math.ceil(kurs)} so'm")



# TELEGRAMGA BOG'LANISH
TOKEN='5246150731:AAE1tcZmXTCPgq-MRZ0oaJJ9swjhFxE9hIo'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start',"help"])
def send_welcome(message):
    javob="Assalomu Alaykum, Xush kelibsiz! \nKril-Lotin  "
    javob+="Lotin-Kril botman😎😎. \nMatn kiriting:  ⌛️⏳  "
    javob+=f"\n\nBugungi kurs: 1$-AQSH  = {math.ceil(kurs)} so'm"
    javob+=f"\n{sana}"
    bot.reply_to(message,javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    xabar=message.text
    if xabar.isascii():
        javob=to_cyrillic(xabar)
        javob+=f"\n\nBugungi kurs: 1$-AQSH  = {math.ceil(kurs)} so'm"
        javob+=f"\n{sana} "

    else:
        javob=to_latin(xabar)
        javob+=f"\n\nBugungi kurs: 1$-AQSH  = {math.ceil(kurs)} so'm"
        javob+=f"\n{sana} "

    bot.reply_to(message,javob)

bot.polling()
