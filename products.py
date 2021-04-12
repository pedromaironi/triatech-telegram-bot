from config import *
from random import randint

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # print( str(datetime.now().time()) + "\n" + str(datetime.now()))
    if call.data == 'x':
        uid = call.from_user.id
        # print(str(uid))
        isExist = customer_exist(uid)
        info_null = False
        data_incomplete = []
        index = 0
        if isExist != None:
            responses_me = showInfoCustomer(uid)
            # with open('extra_data/conditions.json','w') as file:
            #     json.dump(responses_me, file, ident=4)

            for items in responses_me:
                index = index + 1
                x = items
                if responses_me[x] == "null":
                    info_null = True
                    print(info_null)
                    data_incomplete.insert(index,x)
                    # print(responses_me[x] + "errir")
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['es'])

        print(info_null)
        if info_null == True:
            print("asd")
            info_for_user = "Necesitamos tener todos sus datos para enviar el producto.\n" + "Los siguientes campos debe completarlos correctamente:"
            print(info_for_user)
            for item in data_incomplete:
                print(item)
                info_for_user = info_for_user + " " + item + ","
            print(info_for_user)
            bot.send_message(call.message.json['chat']['id'], info_for_user)

        # print(data_incomplete);
            # bot.send_message(call.message.json['chat']['id'], "asd")

    if call.data == 'Country':
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['country'])
    if call.data == 'Age':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['age'])
    if call.data == 'Name':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['name'])
    if call.data == 'Zip code':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['zip'])
    if call.data == 'State':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['state'])
    if call.data == 'Address 1':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['address1'])
    if call.data == 'Address 2':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['address2'])
    if call.data == 'Email':
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['email'])

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
