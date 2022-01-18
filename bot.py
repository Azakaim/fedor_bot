import random
import telebot
from environ import Env
from settings import *

env = Env()
env.load_env()


token = env('BOT_TOKEN')
bot = telebot.TeleBot(token)


def get_random_response(message):
    message_text_fix = message.text.title()
    response_phrases_friend = [" Ave — «здравствуй» на латыни.) ",
                               f"Да благословят вас боги {message.text.title()}! ", "DRUG.!. ",
                               "Рад видеть Его Величество в добром здравии! ",
                               f"Мир вашему {random.choice(phrases_chunk)}",
                               f"Давно не виделись! Как твои старые кости, друг {message.text.title()}?"]

    if message.text in name_friends:
        bot.send_message(message.chat.id, f"{random.choice(response_phrases_friend)} {message_text_fix} {emoji}")
    elif message.text in katya:
        bot.send_message(message.chat.id, f"{random.choice(response_phrases_katya)} {emoji}")
    else:
        bot.send_message(message.chat.id, f"Эй,{message.text} ,{random.choice(response_other)} {emoji}")


@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(message.from_user.id, bot_hallo)


@bot.message_handler(content_types=["text"])
def echo(message):
    get_random_response(message)


if __name__ == '__main__':
    print("Start bot...")
    bot.polling(none_stop=True)
