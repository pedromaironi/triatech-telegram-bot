from config import *
from random import randint

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print( str(datetime.now().time()) + "\n" + str(datetime.now()))
    if call.data == 'x':
        value = null
        for x in range(1):
            value = randint(1000, 9999)
        print(str(value))
        uid = call.from_user.id
        print(str(uid))
        x = showInfoUser(uid)
        responses_me = showInfoUser(uid)
        bot.send_message(call.message.json['chat']['id'], "asd")
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
from random import randint
# seed random number generator
seed(1)
# generate some integers
