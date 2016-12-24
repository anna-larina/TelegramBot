# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot=telebot.TeleBot("250979097:AAFa9NL46DRjgqgZz4XCkHObnDhqLaack3Q")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup=telebot.types.ReplyKeyboardMarkup(True, False)
    itembtn1 = types.KeyboardButton('/news')
    itembtn2 = types.KeyboardButton('/расписание')
    itembtn3 = types.KeyboardButton('/cats')
    itembtn4 = types.KeyboardButton(u'/зачет')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3, itembtn4)
    bot.reply_to(message, u'Здаров, неудачник, как сессия?э',reply_markup=markup)

@bot.message_handler(commands=['news'])
def news(message):
    bot.reply_to(message, 'https://news.yandex.ru/')

@bot.message_handler(commands=['расписание'])
def a(message):
    markup=telebot.types.ReplyKeyboardMarkup(True, False)
    bot.reply_to(message, u'Просто учи билеты. Сессия близко. Держи расписание http://ruz.spbstu.ru/faculty/98/groups/21307',reply_markup=markup)

@bot.message_handler(commands=['cats'])
def b(message):
    markup=telebot.types.ReplyKeyboardMarkup(True, False)
    bot.reply_to(message, 'Котики тебя любят! http://nakolenke.club/uploads/posts/2016-09/1473248821_kotiki04.jpg',reply_markup=markup)

@bot.message_handler(commands=[u'зачет'])
def c(message):
    markup=telebot.types.ReplyKeyboardMarkup(True, False)
    bot.reply_to(message, u'Пффффф, наивный! Его нужно еще заслужить!(с)Одинцов',reply_markup=markup)


bot.polling()
