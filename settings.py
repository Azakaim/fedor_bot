import random

katya = ["Катя", "Катюша", "Любимая", "Екатерина"]
phrases_chunk = ["шалашу", "дому", "селу", "городу", "аулу", "племени"]
response_other = random.choice(
    ["Вы,кто такие???Я вас не звал!",
     "Ко мне попрошу на Вы!",
     "Не думал что на *уй сходить столько желающих!",
     "Буду разговаривать только с главным!"
     ])
response_phrases_katya = ["Привет,любимая,Катюшенька!",
                          "Привет,жопик!)",
                          "Привет,котенок))", "Лучеглазик *)",
                          "Не устала от комплементов,принцесса?)",
                          "Рад видеть Её Величество в добром здравии!"]
bot_hallo = "Бот-приветствия, принимает на вход имя с заглавной буквы!"

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
