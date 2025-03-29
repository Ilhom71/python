from tr import to_cyrillic as kril ,to_latin as lotin
import telebot
key="7639068180:AAHpvr2zL4dPXffcf4bbD1cyo3XbVBwd8cU"
bot = telebot.TeleBot(key,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "matn kirit men uni lotin  kiril qilaman :🎲 ")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    jav=message.text;
    if jav.isascii():
        jav=kril(jav)
    else:
        jav=lotin(jav)    
    bot.reply_to(message, jav)
     
bot.polling()

# soz="a"
# print(("men so'zlarni kril lotin yoki lotin kirilga aylantiaman \n"))
# while soz !="":
#     soz=str(input("soz yoz :"))
#     if soz.isascii():
#         print(kril(soz))
#     else :
#         print(lotin(soz))     