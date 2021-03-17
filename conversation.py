# # -*- coding: utf-8 -*-
from config import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import difflib
markup = InlineKeyboardMarkup()

def gen_markup():
    x = count_products()
    # print(str(x))
    y = showInfoProducts()
    for k in y:
        # print(k['category'])
        # print(k['name'] + "\n" + "id" + k['id'])
        markup_add(k['name'], k['id'])
    return markup

def gen_markup_category():
    x = count_products()
    # print(str(x))
    y = showInfoProducts()
    for k in y:
        # print(k['name'] + "\n" + "id" + k['id'])
        markup_add(k['name'], k['id'])
    return markup



print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  conversation.py importado.{/cyan}'))

def markup_add(name, name_callback):
    markup.add(InlineKeyboardButton(name, callback_data=name_callback))

@bot.message_handler(func=lambda Message: True)
def handle_messages(Message):
    # Variables
    product_band = False
    category_band = False
    user_name = Message.json['from']['first_name']
    message_response = ''

    # word save the message from the user
    word = Message.json['text']

    # Sentence write for the user
    first_word = word

    # Read the json
    with open('extra_data/conv.json', 'r') as file:
        words = json.load(file)

    s = first_word.split(' ')

    # words from sentence of user message
    for words_from_user in s:
        # print('words_from_user: ' + words_from_user)
        if(words_from_user == 'productos'):
            product_band = True
            print('product_band: ' + str(product_band))
        elif(words_from_user == 'categorias' or words_from_user == 'categoria' or words_from_user == 'category'):
            category_band = True
            # print('category_band: ' + str(category_band))

    # words from sentence of conversation.json
    for words_from_conv in words:
        # print(words_from_conv)
        # This condition is for search similitude between first_word and words_from_conversation.json
        if(first_word.lower() == words_from_conv):
            # print(words[words_from_conv])
            if(product_band):
                bot.reply_to(Message, words[words_from_conv] , reply_markup=gen_markup())
            # elif(category_band):
                # categories = searchCategories()
                # for ye in categories
                #     print(str(ye))
            else:
                bot.reply_to(Message, words[words_from_conv])

#function to split text into word
# def printWords(s):
#     # split the string
#     s = s.split(' ')
#     # iterate in words of string
#     for word in s:
#     # if length is even
#         if len(word)%2==0:
#             print(word)

# @bot.callback_query_handler(func=lambda call: 'Tenemos los siguientes productos en existencia:')
# def callback_query(call):
#     pass
    # print(call.data)

# @bot.message_handler(commands=['category'])
# def message_handler(message):
#     bot.send_message(message.chat.id, "Categorias", reply_markup=gen_markup())

# def getNamesCategories():
#     y = showInfoProducts()
#     list_categories = []
#     category = []
#     for k in y:
#         category.append(k['category'])
#     for i in category:
#         if i not in list_categories:
#             list_categories.append(i)
#     return list_categories
