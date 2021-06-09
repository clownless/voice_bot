import telebot
from random import randint, choice
import time

username = []
reason = []
when = []

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['voice'])
def send_voice(message):
    if message.voice:
        if message.chat.type == 'private':
            time.sleep(1)
            bot.send_message(message.from_user.id, 'войсоблядь')
        elif message.chat.type == "supergroup":
            time.sleep(1)
            bot.reply_to(message, "войcоблядь")


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == "supergroup":
        if message.text.lower() == 'похуй':
            bot.reply_to(message, 'иди нахуй, быдлан ебаный блять')
            bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time() + 43200)
        if message.text.lower() == 'ссылки':
            time.sleep(1)
            bot.reply_to(message, '@dannie_SahaGlens')
        if message.text.lower() == 'ж':
            j_1 = ['ж', 'опа']
            time.sleep(1)
            bot.reply_to(message, choice(j_1))
        if message.text.lower() == 'рандом':            
            time.sleep(1)
            bot.reply_to(message, f'рандомное число: ' + str(randint(0, 99999999)))
        if message.text.lower() == 'хелп':
            time.sleep(1)
            bot.reply_to(message, 'https://telegra.ph/Pravila-06-05-9')
        if message.text.lower() == 'иди нахуй':
            time.sleep(1)
            bot.reply_to(message, 'сам иди')
        if message.text.lower() == 'слыш' or message.text.lower() == 'слышь':
            time.sleep(1)
            bot.reply_to(message, 'за углом поссыш')
        if message.text.lower() == 'ты гей':
            j_1 = ['нахуй иди', 'сам']
            time.sleep(1)
            bot.reply_to(message, choice(j_1))
        if message.text.lower() == 'бот лох':
            time.sleep(1)
            bot.reply_to(message, 'иди нахуй')
        if message.text.lower() == 'айди':
            bot.reply_to(message, message.chat.id)

@bot.message_handler(content_types=['new_chat_members'])
def new_mem(message):
    bot.reply_to(message, 'выебать')


@bot.message_handler(content_types=['new_chat_title'])
def new_tittle(message):
    bot.reply_to(message, 'заебали')


bot.polling(none_stop=True, interval=0)
