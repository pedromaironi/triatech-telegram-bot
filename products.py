from config import *
from random import randint

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # print(call.message.json['reply_markup']['inline_keyboard'])
    # print( str(datetime.now().time()) + "\n" + str(datetime.now()))
    uid = call.from_user.id
    # print(str(uid))
    responses_me = showInfoCustomer(uid)
    isExist = customer_exist(uid)
    info_null = False
    data_incomplete = []
    band_action = False
    save = ''
    action = ''
    index = 0
    if call.data == 'x':
        if isExist != None:
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
            bot.send_message(call.message.json['chat']['id'], info_for_user + "\nUtilice el comando /register para confirmar sus datos")

        # print(data_incomplete);
            # bot.send_message(call.message.json['chat']['id'], "asd")
    if call.data == 'save_country':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['country'], reply_markup=sendto)

    if call.data == 'save_state':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['state'], reply_markup=sendto)

    if call.data == 'save_email':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['email'], reply_markup=sendto)

    if call.data == 'save_age':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['age'], reply_markup=sendto)

    if call.data == 'save_zip_code':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['zip'], reply_markup=sendto)

    if call.data == 'save_address_1':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['address1'], reply_markup=sendto)

    if call.data == 'save_address_2':
        sendto = types.ForceReply(selective=True)
        bot.send_message(call.message.json['chat']['id'], responses['register_customer']['address2'], reply_markup=sendto)

    if call.data == 'Country':
        if responses_me['country'] == "null":
            band_action = True
            save = 'save_'+'country'
            action = "Ciudad/Región\nClick en Guardar\nInserta el campo. Example: Santiago de los caballeros"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['country'] + responses_me['country'])
    if call.data == 'Age':
        if responses_me['age'] == "null":
            band_action = True
            save = 'save_'+'age'
            action = "Edad\nClick en Guardar\nInserta el campo. Example: 21"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['age'] + responses_me['age'])
    if call.data == 'Name':
        if responses_me['name'] == "null":
            band_action = True
            save = 'save_'+'name'
            action = "Nombre y Apellido\nClick en Guardar\nInserta el campo. Example: Pedro"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['name'] + responses_me['name'])
    if call.data == 'Zip code':
        if responses_me['zip_code'] == "null":
            band_action = True
            save = 'save_'+'zip_code'
            action = "Zip code\nClick en Guardar\nInserta el campo. Example: 51000"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['zip'] + responses_me['zip_code'])
    if call.data == 'State':
        if responses_me['state'] == "null":
            band_action = True
            save = 'save_'+'state'
            action = "Estado \nClick en Guardar\nInserta el campo. Example: Cibao"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['state'] + responses_me['state'])
    if call.data == 'Address1':
        if responses_me['address_1'] == "null":
            band_action = True
            save = 'save_'+'address_1'
            action = "Primera Direccion\nClick en Guardar\nInserta el campo. Example: Mella 85"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['address1'] + responses_me['address_1'])
    if call.data == 'Address2':
        if responses_me['address_2'] == "null":
            band_action = True
            save = 'save_'+'address_2'
            action = "Segunda Direccion\nClick en Guardar\nInserta el campo. Example: Navarrete,villa bisono"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['address2'] + responses_me['address_2'])
    if call.data == 'Email':
        if responses_me['email'] == "null":
            band_action = True
            save = 'save_'+'email'
            action = "Email\nClick en Guardar\nInserta el campo. Example: correo@hotmail.com"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['email'] + responses_me['email'])
    
    if band_action == True:
        send_action_to_user(call, action,save)

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
    list = {"Email","Name", "Age", "Country", "Address1", "Address2", "State", "Zip code"}
    markup = InlineKeyboardMarkup()
    cont = 0
    for k in list:
        print(k + " " + k)
        markup.add(InlineKeyboardButton(k, callback_data=k))
    bot.send_message(message.chat.id, "Registro de Cliente 🚨", reply_markup=markup)

def send_action_to_user(call,type_action,save):
     # while True:
                # bot.send_message(call.message.json['chat']['id'], responses['register_customer']['country'])
    menu_register = types.InlineKeyboardMarkup()
    btn_save = types.InlineKeyboardButton('Guardar', callback_data=save)
    menu_register.row(btn_save)
    bot.send_chat_action(call.message.chat.id, 'typing')
    msg = bot.send_message(call.from_user.id, type_action,
    parse_mode='HTML', reply_markup=menu_register)