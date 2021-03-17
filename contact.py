# -*- coding: utf-8 -*-
from config import *

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

@bot.message_handler(commands=['contact'])
def commanStart(message):
    bot.reply_to(message,"Contacto" + "\n" + str(responses['contact']['es']) + "\n", reply_markup=markup)