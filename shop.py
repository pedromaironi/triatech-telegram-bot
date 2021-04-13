# # -*- coding: utf-8 -*-
from config import *

list_prices = InlineKeyboardMarkup()
def list(price):
    list = price
    add_price(price, 1)
    return list_prices

def add_price(name, name_callback):
    markup.add(InlineKeyboardButton(name, callback_data=name_callback))

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'x':
        print('fggggggggggggggg')

@bot.message_handler(commands=['shop'])
def message_handler(message):
    print("asd")
    product = message.json['text']
    words = product
    name_of_product = words.replace('/shop ','')
    details = showDetailsProducts(name_of_product.strip())
    if details != None:
        print(name_of_product)
        print(details)
        details_product = details['detail']
        price = details['price']
        url = details['image']
        categoria = details['category']
        keyboard=json.dumps({ "inline_keyboard": [ [ {"text": 'DOP ' + details['price'], "callback_data": "x"} ] ] })
        # print(keyboard)
        markups = types.InlineKeyboardMarkup()
        markups.add(types.InlineKeyboardButton(text=details['name'] + ' ' + details['price'] + ' DOP ', callback_data='x'))
        response_products = name_of_product + "\n" + details_product + "\n" + "Precio: $" + price + '\n'
        bot.send_photo(message.chat.id, photo=url, caption=response_products, reply_markup=markups)

