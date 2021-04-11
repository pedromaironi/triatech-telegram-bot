from config import *
from random import randint

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # print( str(datetime.now().time()) + "\n" + str(datetime.now()))
    if call.data == 'x':
        uid = call.from_user.id
        print(str(uid))
        isExist = customer_exist(str(212))
        if isExist != None:
            x = showInfoUser(uid)
            responses_me = showInfoUser(uid)
            bot.send_message(call.message.json['chat']['id'], "asd")
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['es'])
    if call.data == 'Country':
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['country'])

    if call.data == "1":
        print('1')
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
        response_products = name_product + "\n" + details_product + "\n" + "Precio: $" + price + '\n' + "Categoria: " + categoria + "\n" + "/category Para obtener todas las categorias que tenemos." + "\n/shop " + " " + name_product + " Para realizar la compra de este producto."
        bot.send_photo(chat_id=call.message.json['chat']['id'], photo=url, caption=response_products)


@bot.message_handler(commands=['products'])
def message_handler(message):
    markup = InlineKeyboardMarkup()
    x = count_products()
    # print(str(x))
    y = showInfoProducts()
    for k in y:
        markup.add(InlineKeyboardButton(k['name'], callback_data=k['id']))
    bot.send_message(message.chat.id, "Productos", reply_markup=markup)


@bot.message_handler(commands=['register'])
def message_handler(message):
    list = {"Email","Name", "Age", "Country", "Address 1", "Address 2", "State", "Zip code"}
    markup = InlineKeyboardMarkup()
    cont = 0
    for k in list:
        print(k)
        markup.add(InlineKeyboardButton(k, callback_data=k))
    bot.send_message(message.chat.id, "Registro de Cliente 🚨", reply_markup=markup)
