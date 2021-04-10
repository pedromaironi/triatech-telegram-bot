# -*- coding: utf-8 -*-
from config import *

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

@bot.message_handler(commands=['contact'])
def commanStart(message):
    bot.reply_to(message,"Contacto" + "\n" + str(responses['contact']['es']) + "\n", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: 'Category')
def callback_query_handler(call):
    print(call)
    if call.data == "101":
        showDetailsCategories(call, "101")
    elif call.data == "102":
        showDetailsCategories(call, "102")
    elif call.data == "103":
        showDetailsCategories(call, "103")


@bot.message_handler(commands=['category'])
def message_handler(message):
    # print(message)
    bot.send_chat_action(message.chat.id,'typing')
    bot.send_message(message.chat.id, "Categorias", reply_markup=markups())
    bot.send_message(message.chat.id, "")


def showDetailsCategories(calls, idCategory):
    data = {}
    name_category = ""
    if call.data == idCategory:
        for x in call.message.json['reply_markup']['inline_keyboard']:
            data = x
            print(data)
            for x in data:
                print(x)
                if x['callback_data'] == idCategory:
                    name_category = x['text']
        print(name_category)
        productos = searchProducts_category(name_category)
        name_products = productos['name']
        bot.send_message(call.message.json['chat']['id'], name_products)
