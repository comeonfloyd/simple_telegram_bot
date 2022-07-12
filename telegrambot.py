import telebot
import pandas as pd
import random

arr = ["Модель простая как три сапога",
       "Тут что-то не по-русском написано",
       "Три дня работаешь! Уже эксперт!",
       "А ты нам чо?",
       "Ты делаешь недостаточно!",
       "Кассовый разрыв!",
       "Док",
       "Зовите меня Мэрфи",
       "Фёдор Меркурьев и ВИА Королева",
       "Ща я ей устный ВПР покажу",
       ]

text_lines = pd.read_excel('Цитаты.xlsx').to_numpy()
df = text_lines.tolist()



bot = telebot.TeleBot('5570274268:AAFvaYDVMo2kEZ-5_g3FSHItu6rLm8wjF5k')

#raz = (f"Я на раз на раз-два, раз, два, три, четыре! Панама в эфире!")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Ты делаешь недостаточно, <b>{message.from_user.first_name}</b> !'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['nds'])
def calculate(message):
    bot.send_message("Какая сумма?")


@bot.message_handler()
def user_message(message):
    if message.text == "раз":
        bot.send_message(message.chat.id, f"Я на раз на раз-два, раз, два, три, четыре! Панама в эфире!", parse_mode='html')
    elif message.text == "1":
        bot.send_message(message.chat.id, f"Я на раз на раз-два, раз, два, три, четыре! Панама в эфире!", parse_mode='html')
    elif message.text == "Три!":
        bot.send_message(message.chat.id, f"Жопку подотри!", parse_mode='html')

    elif message.text == "Если вы понимаете о чем я":
        photo = open('you_know.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Ссылку!":
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
        bot.send_message(message.chat.id, url)
    elif message.text == "Падла":
        bot.send_message(message.chat.id, 'Сам падла! Учись кодить, долботрон!')
    elif message.text == "Цитату!":

        bot.send_message(message.chat.id, random.choice(df))

    elif message.text == "Кочеткова в студию!":
        arr_photo = ['Кочетков1.png',
                     'Кочетков2.png',
                     'Кочетков3.png']
        file_photo_text = random.choice(arr_photo)
        photo = open(file_photo_text, 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Музыки хочу!":
        voice = open('music.ogg', 'rb')
        bot.send_audio(message.chat.id, voice)
    elif message.text == 'mp3':
        music = open('RickRoll.mp3', 'rb')
        bot.send_audio(message.chat.id, music)
    elif message.text == "Тимур давай!":
        video = open("timur.mp4", 'rb')
        bot.send_video(message.chat.id, video, protect_content=True)

#@bot.message_handler()
#def command(message):
 #   line = random.choice(text_lines)
  #  bot.send_message(message.chat.id, str(text_lines.sample()))









bot.polling(none_stop=True)

