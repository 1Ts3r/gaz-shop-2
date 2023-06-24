import random
import telebot
import webbrowser
import os
from telebot import types
from flask import Flask, request

# Считываю свой токен из файла mytoken.txt, в твоем случае это будет не нужно
# Удали 6 и 7 строчки и вместо переменной mytoken в 10 строчке напиши свой токен
# Пример: bot = telebot.TeleBot('62732:RyJidSDIdi...')
# Передаем сюда токен, который получили от FatherBot
TOKEN = '5814137876:AAFakytbuSZ0NU8XBxgcrRublNqEJDbH2JI'
bot = telebot.TeleBot(TOKEN)
# Варианты ответов пользователю, если тот ввел непонятное боту сообщение
answers = ['Я не розумію вас', 'Напишіть щось інше']

# Обработка команды /start
app = Flask(__name__)
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200
@bot.message_handler(commands=['start'])
def welcome(message):
    # Добавляем кнопки, которые будут появляться после ввода команды /start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button2 = types.KeyboardButton('📄 Справка')
    # Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок
    markup.row(button1)
    markup.row(button2)

    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Доброго дня {message.from_user.first_name}!\nУ мене Ви зможете купити одяг!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекину тебе в меню!', reply_markup=markup)


# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == 'Товари':
        goodsChapter(message)
    elif message.text == 'Інформація':
        infoChapter(message)
    elif message.text == '🔹 Товар #1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Інфа', reply_markup=markup)
    elif message.text == '🔹 Товар #2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Інфа', reply_markup=markup)
    elif message.text == '🔹 Товар #3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Інфа', reply_markup=markup)
    elif message.text == '🔹 Товар #4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Купити', reply_markup=markup)
    elif message.text == '💳 Купити':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    # Если пользователь написал свое сообщение, то бот рандомно генерирует один из возможных вариантов ответа
    # Добавлять и редактировать варианты ответов можно в списке answers
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

# Функция, отвечающая за раздел товаров
def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Товар #1')
    button2 = types.KeyboardButton('🔹 Товар #2')
    button3 = types.KeyboardButton('🔹 Товар #3')
    button4 = types.KeyboardButton('🔹 Товар #4')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Ось ці всі товари є в продажі:', reply_markup=markup)

# Функция, отвечающая за раздел помощи
def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1)
    bot.send_message(message.chat.id, 'Обирай одну із кнопок та дивись чи підходить тобі цей товар', reply_markup=markup)

# Строчка, чтобы программа не останавливалась
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))