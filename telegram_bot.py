#!/usr/bin/python3

# Подключаем модуль случайных чисел
import random
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Подключаем модуль для Телеграма
import telebot
import datetime
import sys
import os

# Указываем токен
bot = telebot.TeleBot('******************')



# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "menu":

        # Пишем приветствие

        # bot.send_message(message.from_user.id, "")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_report = types.InlineKeyboardButton(text='report', callback_data='report')

        # И добавляем кнопку на экран

        keyboard.add(key_report)

        key_data = types.InlineKeyboardButton(text='date', callback_data='date')

        keyboard.add(key_data)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='-----MENU-----', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "report":
        # Формуємо звіт
        # print(file.read()
        file = open("log.txt", "r")

        msg = file.read()
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "date":
        msg = str(datetime.datetime.today())
        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)
