# -*- coding: utf-8 -*-

from config import *

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# markup.add(types.KeyboardButton('register'))

@bot.message_handler(commands=['start'])
def commanStart(message):
    uname = message.from_user.first_name
    cid = message.chat.id
    uid = message.from_user.id
    print('chat id:' + str(cid))
    print('user id:' + str(uid))
    data = {"id": message.from_user.id,"name":message.from_user.first_name,"lastname":message.from_user.last_name,"username":message.from_user.username,"language_code":message.from_user.language_code}
    with open('extra_data/user.json', 'w') as f:
        json.dump(data, f)
    if(confirm_user(uid) == 0):
        create_user()
        bot.reply_to(message, "Hola " + uname + "\n" + responses['start_2']['es'] + "\n\n" + "Escribe /me para ver tu informacion", reply_markup=markup)
    elif(confirm_user(uid) > 0):
        bot.reply_to(message, "Hola " + uname + "\n" + responses['start_already_user']['es'] + "\n\n" + "Escribe /me para ver tu informacion", reply_markup=markup)

@bot.message_handler(commands=['me'])
def commandMe(message):
    uid = message.from_user.id
    responses_me = showInfoUser(uid)
    print(responses_me['language_code'])
    if(responses_me['language_code'] == 'None'):
        txt = "Debes seleccionar un lenguaje en la configuracion de tu cuenta."
    else:
        txt = str(responses_me['language_code'])
    bot.reply_to(message,"Nombre de usuario: @" + str(responses_me['username']) + "\n" + "Nombre: " + str(responses_me['name']) + "\n" + "Apellido: " + str(responses_me['lastname']) + "\n" + "Lenguaje: " + txt, reply_markup=markup)
    # print(responses_me['name'])

# @bot.message_handler(commands=['register'])
# def commanRegister(message):
#     # data
#     bot.reply_to(message,"/register para registrarte en la tienda para tu compra", reply_markup=markup)
