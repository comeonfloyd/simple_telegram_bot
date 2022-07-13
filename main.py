#Дисклаймер - Бот создавался просто чтобы научится создавать ботов в телеграмме. Всё содержимое исключительно развлекательная история.


import telebot
import pandas as pd
import random

text_lines = pd.read_excel('Цитаты.xlsx').to_numpy() # Загружаем эксельку с цитатами и её загняем в лист
df = text_lines.tolist()

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Ты делаешь недостаточно, <b>{message.from_user.first_name}</b> !'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['nds']) # Команда для расчёта НДС, изучал как бот обрабатывает инпут и что с ним дальше можно сделать
def calculate2(pm):
    sent_msg2 = bot.send_message(pm.chat.id, "Какая сумма? Введите в формате с точкой")
    bot.register_next_step_handler(sent_msg2, numbers_nds2)

def numbers_nds2(pm):
    number2 = pm.text
    sent_msg2 = bot.send_message(pm.chat.id, f"Какой размер НДС?")
    bot.register_next_step_handler(sent_msg2, calculation2, number2)

def calculation2(pm, number2):
    nds_number2 = pm.text
    data_text2 = ("Сумма с НДС: " + str((float(number2) * float(nds_number2)) + float(number2)))
    bot.send_message(pm.chat.id, data_text2)


@bot.message_handler(commands=['nds_reg']) # Команда для расчёта обратного НДС, изучал как бот обрабатывает инпут и что с ним дальше можно сделать
def calculate(pm):
    sent_msg = bot.send_message(pm.chat.id, "Какая сумма? Введите в формате с точкой")
    bot.register_next_step_handler(sent_msg, numbers_nds)

def numbers_nds(pm):
    number = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"Какой размер НДС?")
    bot.register_next_step_handler(sent_msg, calculation, number)

def calculation(pm, number):
    nds_number = pm.text
    data_text = ("Ваш выделенный НДС: " + str((((float(number) / (1 + float(nds_number))) - float(number)) * -1)))
    bot.send_message(pm.chat.id, data_text)



@bot.message_handler(commands=['weather']) # Продолжаем изучать команды

def weather(message):
    url = 'https://yandex.ru/pogoda/'
    bot.send_message(message.chat.id, url)


@bot.message_handler() # Большая страшная штука для реакции на сообщения
def user_message(message):
    if message.text == "раз":
        bot.send_message(message.chat.id, f"Я на раз на раз-два, раз, два, три, четыре! Панама в эфире!", parse_mode='html')
    elif message.text == "1":
        bot.send_message(message.chat.id, f"Я на раз на раз-два, раз, два, три, четыре! Панама в эфире!", parse_mode='html')
    elif message.text in ("Три!", "три", "Три", "три!):
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

bot.polling(none_stop=True)
