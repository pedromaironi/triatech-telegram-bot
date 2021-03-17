from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *
markup = InlineKeyboardMarkup()

def gen_markup():
    x = count_products()
    # print(str(x))
    y = showInfoProducts()
    for k in y:
        markup_add(k['name'], k['id'])
    return markup

def markup_add(name, name_callback):
    markup.add(InlineKeyboardButton(name, callback_data=name_callback))

@bot.callback_query_handler(func=lambda call: 'Products')
def callback_query(call):
    x = searchCategories()
    for y in x:
        print(y)
    if call.data == "1":
        showDetails(call, "1")
    elif call.data == "2":
        showDetails(call, "2")
    elif call.data == "3":
        showDetails(call, "3")
    elif call.data == "4":
        showDetails(call, "4")
    elif call.data == "5":
        showDetails(call, "5")

def showDetails(call, idProduct):
    data = {}
    name_product = ""
    if call.data == idProduct:
        for x in call.message.json['reply_markup']['inline_keyboard']:
            data = x
            # print(data)
            for x in data:
                # print(x)
                if x['callback_data'] == idProduct:
                    name_product = x['text']
        print(name_product)
        details = showDetailsProducts(name_product)
        details_product = details['detail']
        price = details['price']
        url = details['image']
        categoria = details['category']
        response_products = name_product + "\n" + details_product + "\n" + "Precio: $" + price + '\n' + "Categoria: " + categoria + "\n" + "/category Para obtener todas las categorias que tenemos."
        bot.send_photo(chat_id=call.message.json['chat']['id'], photo=url, caption=response_products)


@bot.message_handler(commands=['products'])
def message_handler(message):
    bot.send_message(message.chat.id, "Productos", reply_markup=gen_markup())


