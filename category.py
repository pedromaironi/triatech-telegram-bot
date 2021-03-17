from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import *
markup = InlineKeyboardMarkup()

def markup_gen():
    y = searchCategories()
    count = 0
    for k in y:
        count = count + 1
        markup_add(k, count)
    return markup

def markup_add(name, name_callback):
    markup.add(InlineKeyboardButton(name, callback_data=name_callback))


@bot.callback_query_handler(func=lambda call: 'Category')
def callback_query(call):
    print('asd')
    if call.data == "1":
        showDetails(call, "1")
    elif call.data == "2":
        showDetails(call, "2")
    elif call.data == "3":
        showDetails(call, "3")


def showDetails(call, idCategory):
    print(call)
    print(idCategory)


@bot.message_handler(commands=['category'])
def message_handler(message):
    print(message)
    bot.send_message(message.chat.id, "Category", reply_markup=markup_gen())

