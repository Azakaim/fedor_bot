import random
import telebot
from environ import Env
from settings import *

env = Env()
env.load_env()


token = env('BOT_TOKEN')
bot = telebot.TeleBot(token)

# ===SMILES===
thunderstorm = u'\U0001F612'  # zloy
drizzle = u'\U0001F602'  # smeh
rain = u'\U0001F621'  # grust
snowflake = u'\U0001F620'  # zloy
snowman = u'\U0001F632'  # rev
atmosphere = u'\U0001F637'  # maska
clearSky = u'\U0001F648'  # obez
fewClouds = u'\U0001F44F'  # ovacii
clouds = u'\U0001F44D'  # Code: 802-803-804 clouds general
hot = u'\U0001F525'  # Code: 904
defaultEmoji = u'\U0001F634'  # default emojis
love = u'\U0001F493'  # love
# =============


emoji = random.choice([thunderstorm, drizzle, rain,
     snowflake, snowman, atmosphere,
     clearSky, fewClouds, clouds,
     hot, defaultEmoji
     ])
name_friends = [
    "Jhon", "Алексей", "Лёха", "Лёша", "Леха", "Леша", "Иван", "Ваня"
]



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
