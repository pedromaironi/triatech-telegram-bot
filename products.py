from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *
markup = InlineKeyboardMarkup()

def gen_markup():
    x = count_products()
    print(str(x))
    y = showInfoProducts()
    markup.row_width = 1
    markup.row_height = 2
    for k in y:
        print(k['name'] + "\n" + "id" + k['id'])
        markup_add(k['name'], k['id'])
    return markup

def markup_add(name, name_callback):
    markup.add(InlineKeyboardButton(name, callback_data=name_callback))

@bot.callback_query_handler(func=lambda call: 'Products')
def callback_query(call):
    # print(call.message.json['reply_markup']['inline_keyboard'][1]['text'])
    print(call)
    data = {}
    name_product = ""
    if call.data == "1":
        for x in call.message.json['reply_markup']['inline_keyboard']:
            data = x
            # print(data)
            for x in data:
                # print(x)
                if x['callback_data'] == "1":
                    name_product = x['text']
        # print(name_product)
        # bot.answer_callback_query(call.id, name_product)
        # print(name_product)
        details = showDetailsProducts(name_product)
        details_product = details['detail']
        url = details['image']
        # print(url)
        # bot.answer_callback_query(call.id, name_product)
        bot.send_photo(chat_id=call.message.json['chat']['id'], photo=url, caption=details_product)
    elif call.data == "2":
        data = {}
        name_product = ""
        if call.data == "2":
            for x in call.message.json['reply_markup']['inline_keyboard']:
                data = x
                print(call)
                print(data)
                for x in data:
                    # print(x)
                    if x['callback_data'] == "2":
                        name_product = x['text']
            # print(name_product)
            # bot.answer_callback_query(call.id, name_product)
             # print(name_product)
            details = showDetailsProducts(name_product)
            details_product = details['detail']
            url = details['image']
            # print(url)
            # bot.answer_callback_query(call.id, name_product)
        bot.send_photo(chat_id=call.message.json['chat']['id'], photo=url, caption=details_product)
    elif call.data == "3":
        data = {}
        name_product = ""
        if call.data == "3":
            for x in call.message.json['reply_markup']['inline_keyboard']:
                data = x
                print(data)
                for x in data:
                    # print(x)
                    if x['callback_data'] == "3":
                        name_product = x['text']
            # print(name_product)
            details = showDetailsProducts(name_product)
            details_product = details['detail']
            price = details['price']
            url = details['image']
            categoria = details['category']
            # print(details)
            # bot.answer_callback_query(call.id, name_product)
            response_products = name_product + "\n" + details_product + "\n" + "Precio: $" + price + "Categoria: " + categoria + "\n" + "/category Para obtener todos los productos pertenecientes a esta categoria"
        bot.send_photo(chat_id=call.message.json['chat']['id'], photo=url, caption=response_products)


@bot.message_handler(commands=['products'])
def message_handler(message):
    bot.send_message(message.chat.id, "Productos", reply_markup=gen_markup())