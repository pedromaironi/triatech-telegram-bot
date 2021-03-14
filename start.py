# -*- coding: utf-8 -*-

from config import *
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(types.KeyboardButton('register'))

@bot.message_handler(commands=['start'])
def commanStart(message):
    uname = message.from_user.first_name
    cid = message.chat.id
    uid = message.from_user.id
    date = message.date
    bot.reply_to(message, "Hola " + uname + "\n" + responses['start_2']['es'] + "\n" + "/register para registrarte en la tienda para tu compra", reply_markup=markup)
    data = {"id:": m.from_user.id,"name":m.from_user.first_name,"lastname":m.from_user.last_name,"username":m.from_user.username,"language_code":m.from_user.language_code}
    with open('extra_data/user.json', 'w') as f:
        json.dump(data, f)

    # create_user(uid, m.from_user.first_name, m.from_user.last_name, m.from_user.username, m.from_user.language_code)
    # print("id:" + uid + " name:" + m.from_user.first_name + " lastname: " + m.from_user.last_name + " username: " + m.from_user.username + " language code:" + m.from_user.language_code)

# def find_at(msg):
#     for text in msg:
#         if '@' in text:
#             return text

# @bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# def at_answer(message):
#     texts = message.text.split()
#     find_at(texts)
#     bot.reply_to(message,texts)


@bot.message_handler(commands=['register'])
def commanRegister(message):
    # data
    data = {"id:": m.from_user.id,"name":m.from_user.first_name,"lastname":m.from_user.last_name,"username":m.from_user.username,"language_code":m.from_user.language_code}
    with open('extra_data/user.json', 'w') as f:
        json.dump(data, f)
    bot.reply_to(message,"/register para registrarte en la tienda para tu compra", reply_markup=markup)
