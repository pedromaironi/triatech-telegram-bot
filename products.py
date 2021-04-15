from config import *


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    # Quantity of products with names
    list_callbacks_sales = []
    all_names_products = showInfoProducts()
    query_quantity_products = cantProducts()
    for x in range(query_quantity_products):
        products_names_query = all_names_products.next()
        for items in products_names_query:
            # print(items)
            if items == 'name':
                list_callbacks_sales.append(products_names_query[items])


    # Variables
    sales_buttons = InlineKeyboardMarkup()
    uid = call.from_user.id
    # print(str(uid))
    infoCustomer = showInfoCustomer(uid)
    isExist = customer_exist(uid)
    info_null = False
    data_incomplete = []
    band_action = False
    save = ''
    action = ''
    index = 0
    for items in list_callbacks_sales:
        # print(items)
        if call.data == items:
            print(call.data)
            name_product_sale = ''
            details_sales = {}
            details_sales = QueryInfoShoppingProduct(items)
            product_n = details_sales['name_product']
            details_of_product_query = showDetailsProducts(product_n)
            message = responses['shop']['info_shop']['info'] + "\n" + responses['shop']['info_shop']['name_customer'] + details_sales['name_customer'] + "\n" + responses['shop']['info_shop']['ship'] + details_sales['shipment_no'] + "\n" +responses['shop']['info_shop']['name_product'] + details_sales['name_product'] + "\n" +responses['shop']['info_shop']['Fecha_compra'] + details_sales['date_sale'] + "\n" +responses['shop']['info_shop']['date_delivered'] + details_sales['date_delivered'] + "\n" +responses['shop']['info_shop']['track_code'] + details_sales['track_code'] + "\n" +responses['shop']['info_shop']['total_paid'] + details_sales['total_paid']
            bot.send_photo(chat_id=call.message.json['chat']['id'], photo=details_of_product_query['image'], caption=message)

    # Sales info
    if call.data == 'my_sales':
        quantity = QueryInfoShoppingCount(uid)
        print(quantity)
        sales_information = QueryInfoShopping(uid)
        for amount in range(quantity):
            sales = sales_information.next()
            for items_ in sales:
                if items_ == 'name_product':
                    # print(sales[items_])
                    name_product_query = sales[items_]
                    sales_buttons.add(InlineKeyboardButton(name_product_query, callback_data=name_product_query))
        bot.send_chat_action(call.message.json['chat']['id'], 'typing')
        bot.send_message(call.message.json['chat']['id'], "Sales🚨", reply_markup=sales_buttons)
    if call.data == 'x':
        jsonProduct = call.message.json['caption']
        if isExist != None:
            for items in infoCustomer:
                index = index + 1
                x = items
                if infoCustomer[x] == "null":
                    info_null = True
                    print(info_null)
                    data_incomplete.insert(index,x)
                    print(infoCustomer[x] + "errir")
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_customer']['es'])

        # print(info_null)
        if info_null == True:
            print("asd")
            info_for_user = "Necesitamos tener todos sus datos para enviar el producto.\n" + "Los siguientes campos debe completarlos correctamente:"
            print(info_for_user)
            for item in data_incomplete:
                print(item)
                info_for_user = info_for_user + " " + item + ","
            print(info_for_user)
            bot.send_message(call.message.json['chat']['id'], info_for_user + "\nUtilice el comando /register para confirmar sus datos")
        else:
            cont = 0
            total_paid = ''
            for line in jsonProduct.splitlines():
                cont = cont + 1
                # print(cont)
                # print(line)
                if cont == 1:
                    jsonProduct = line
                elif cont == 3:
                    total_paid = line
                elif cont == 4:
                    break
            buttons = InlineKeyboardMarkup()
            list = {"Si", "No"}
            buttons.add(InlineKeyboardButton("Si", callback_data="Si_comprar"),
            InlineKeyboardButton("No", callback_data="No_comprar") )
            bot.send_message(call.message.json['chat']['id'],jsonProduct + "\n" + total_paid + "\n" + responses['shop']['line1'], reply_markup=buttons)
    if call.data == 'Si_comprar':
        cont = 0
        jsonProduct = call.message.json['text']
        total_paid = ''
        for line in jsonProduct.splitlines():
            cont = cont + 1
            if cont == 1:
                jsonProduct = line
            if cont == 2:
                total_paid = line.replace("Precio: ", "")
        print(jsonProduct)
        # details_product = showInfoProducts(jsonProduct)
        print(total_paid)
        infoCustomer = showInfoCustomer(uid)
        # print(infoCustomer)
        details = showDetailsProducts(jsonProduct)
        description_product = details['detail']
        category_product = details['category']
        no_shipment = random.randint(100000000,200000000)
        date_sale = str(datetime.now().date())
        date_delivered = str(datetime.now().date() + timedelta(days=15))
        track_code = generate_track_code()
        information_sale = {
        "idCustomer": infoCustomer['id'],
        'name_customer':infoCustomer['name'],
        'shipment_no':str(no_shipment),
        'name_product':jsonProduct,
        'description':description_product,
        'category_product': category_product,
        'date_sale':date_sale,
        'date_delivered': date_delivered,
        'track_code':track_code,
        'total_paid':total_paid
        }

        with open('extra_data/information_sale.json', 'w') as f:
            json.dump(information_sale, f)
        print(information_sale)

        # Create sale
        create_sale()
        bot.send_message(call.message.json['chat']['id'],
        responses['shop']['info_shop']['info'] + "\n" +
        responses['shop']['info_shop']['name_customer'] + infoCustomer['name'] + "\n" +
        responses['shop']['info_shop']['ship'] + str(no_shipment) + "\n" +
        responses['shop']['info_shop']['name_product'] + jsonProduct + "\n" +
        responses['shop']['info_shop']['Fecha_compra'] + date_sale + "\n" +
        responses['shop']['info_shop']['date_delivered'] + date_delivered + "\n" +
        responses['shop']['info_shop']['track_code'] + track_code + "\n" +
        responses['shop']['info_shop']['total_paid'] + total_paid + "\n" +
        responses['shop']['line2'] + "\n" +
        responses['information_myself']['state'] + infoCustomer['state'] + "\n" +
        responses['information_myself']['country'] + infoCustomer['country'] + "\n" +
        responses['information_myself']['address1'] + infoCustomer['address_1'] + "\n" +
        responses['information_myself']['address2'] + infoCustomer['address_2'] + "\n" +
        responses['information_myself']['email'] + infoCustomer['email'] + "\n" +
        responses['information_myself']['zip'] + infoCustomer['zip_code']
        )

    if call.data == 'Mi informacion':
        infoCustomer = showInfoCustomer(uid)
        bot.send_message(call.message.json['chat']['id'],
        responses['information_myself']['name'] + infoCustomer['name'] + "\n" +
        responses['information_myself']['age'] + infoCustomer['age'] + "\n" +
        responses['information_myself']['state'] + infoCustomer['state'] + "\n" +
        responses['information_myself']['country'] + infoCustomer['country'] + "\n" +
        responses['information_myself']['address1'] + infoCustomer['address_1'] + "\n" +
        responses['information_myself']['address2'] + infoCustomer['address_2'] + "\n" +
        responses['information_myself']['email'] + infoCustomer['email'] + "\n" +
        responses['information_myself']['zip'] + infoCustomer['zip_code']
        )
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
        if infoCustomer['country'] == "null":
            band_action = True
            save = 'save_'+'country'
            action = "Ciudad/Región\nClick en Guardar\nInserta el campo. Example: Santiago de los caballeros"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['country'] + infoCustomer['country'])
    if call.data == 'Age':
        if infoCustomer['age'] == "null":
            band_action = True
            save = 'save_'+'age'
            action = "Edad\nClick en Guardar\nInserta el campo. Example: 21"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['age'] + infoCustomer['age'])
    if call.data == 'Name':
        if infoCustomer['name'] == "null":
            band_action = True
            save = 'save_'+'name'
            action = "Nombre y Apellido\nClick en Guardar\nInserta el campo. Example: Pedro"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['name'] + infoCustomer['name'])
    if call.data == 'Zip code':
        if infoCustomer['zip_code'] == "null":
            band_action = True
            save = 'save_'+'zip_code'
            action = "Zip code\nClick en Guardar\nInserta el campo. Example: 51000"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['zip'] + infoCustomer['zip_code'])
    if call.data == 'State':
        if infoCustomer['state'] == "null":
            band_action = True
            save = 'save_'+'state'
            action = "Estado \nClick en Guardar\nInserta el campo. Example: Cibao"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['state'] + infoCustomer['state'])
    if call.data == 'Address1':
        if infoCustomer['address_1'] == "null":
            band_action = True
            save = 'save_'+'address_1'
            action = "Primera Direccion\nClick en Guardar\nInserta el campo. Example: Mella 85"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['address1'] + infoCustomer['address_1'])
    if call.data == 'Address2':
        if infoCustomer['address_2'] == "null":
            band_action = True
            save = 'save_'+'address_2'
            action = "Segunda Direccion\nClick en Guardar\nInserta el campo. Example: Navarrete,villa bisono"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['address2'] + infoCustomer['address_2'])
    if call.data == 'Email':
        if infoCustomer['email'] == "null":
            band_action = True
            save = 'save_'+'email'
            action = "Email\nClick en Guardar\nInserta el campo. Example: correo@hotmail.com"
        else:
            bot.send_message(call.message.json['chat']['id'], responses['register_complete']['email'] + infoCustomer['email'])

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
    list = {"Email","Name", "Age", "Country", "Address1", "Address2", "State", "Zip code", 'Mi informacion'}
    markup = InlineKeyboardMarkup()
    cont = 0
    for k in list:
        print(k + " " + k)
        markup.add(InlineKeyboardButton(k, callback_data=k))
    bot.send_message(message.chat.id, "Registro de Cliente 🚨", reply_markup=markup)

@bot.message_handler(commands=['shopping'])
def message_handler(message):
    options = InlineKeyboardMarkup()
    options.add(InlineKeyboardButton("Mi informacion", callback_data='Mi informacion'), InlineKeyboardButton("Mis compras", callback_data='my_sales'))
    bot.send_message(message.chat.id, "Shopping🚨", reply_markup=options)

def send_action_to_customer(call,type_action,save):
     # while True:
                # bot.send_message(call.message.json['chat']['id'], responses['register_customer']['country'])
    menu_register = types.InlineKeyboardMarkup()
    btn_save = types.InlineKeyboardButton('Guardar', callback_data=save)
    menu_register.row(btn_save)
    bot.send_chat_action(call.message.chat.id, 'typing')
    msg = bot.send_message(call.from_user.id, type_action,
    parse_mode='HTML', reply_markup=menu_register)

def send_action_to_user(call,type_action,save):
     # while True:
                # bot.send_message(call.message.json['chat']['id'], responses['register_customer']['country'])
    menu_register = types.InlineKeyboardMarkup()
    btn_save = types.InlineKeyboardButton('Guardar', callback_data=save)
    menu_register.row(btn_save)
    bot.send_chat_action(call.message.chat.id, 'typing')
    msg = bot.send_message(call.from_user.id, type_action,
    parse_mode='HTML', reply_markup=menu_register)