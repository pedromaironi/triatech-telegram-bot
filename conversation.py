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
        # print(k['name'] + "\n" + "id" + k['id'])
        markup_add(k['name'], k['id'])
    return markup


print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  name.py importado.{/cyan}'))

def markup_add(name, name_callback):
    markup.add(InlineKeyboardButton(name, callback_data=name_callback))

@bot.message_handler(func=lambda Message: True)
def handle_messages(Message):
    # Variables
    cont = 0
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
        if(words_from_user == 'productos'):
            print('\n El usuario dice productos \n')
        # print(word1)
        # if len(word1)%2==0:
        #     print(word1)
        #     pass
    # words from sentence of conversation.json
    for words_from_conv in words:
        print(words_)
        if(first_word.lower() == words_):
            pass
        # print(first_word + "1")
        # tokens ="The quick brown fox jumps over the lazy dog"
        # porter = PorterStemmer()
        # stems = []
        # for t in tokens:
        #     stems.append(porter.stem(t))
        # print(stems)
        # print(tokens)
        # printWords(words_)
        # print(words_ + "2")
        # callback_query(data)
        # print(Message)
        # bot.callback_query_handlers
        # bot.reply_to(Message, words[words_] , reply_markup=gen_markup() )
    # elif(first_word.lower() != words_):
    #     bot.reply_to(Message, 'No te entiendo muy bien, por favor se mas especifico ' + user_name)
    # # seq = difflib.SequenceMatcher(None,first_word,words_)
    # percent = seq.ratio()*100
    # if(percent == 100.0):
    #     print('asd' + words[words_])
    #     bot.reply_to(Message, words[words_] + " " + user_name.lower())
    # # elif(percent<=25.0):
    # #     bot.reply_to(Message, 'No puedo entenderte bien' + " " + user_name)
    # print(percent)

    # if(word == 'Hola'):
    #     message_response = 'Hola pedro'
    # print(message_response)
    # bot.reply_to(Message, message_response)


# user_name = Message.json['from']['first_name']
#     word = Message.json['text']
#     message_response = ''
#     first_word = word
#     with open('extra_data/conv.json', 'r') as file:
#         words = json.load(file)
#     for words_ in words:
#         print(words_)
#         seq = difflib.SequenceMatcher(None,first_word,words_)
#         percent = seq.ratio()*100
#         if(percent >= 75.0):
#             print('asd' + words[words_])
#             bot.reply_to(Message, words[words_] + " " + user_name)
#         # elif(percent<=25.0):
#         #     bot.reply_to(Message, 'No puedo entenderte bien' + " " + user_name)
#         print(percent)

#function to split text into word
def printWords(s):
    # split the string
    s = s.split(' ')
    # iterate in words of string
    for word in s:
    # if length is even
        if len(word)%2==0:
            print(word)

@bot.callback_query_handler(func=lambda call: 'Tenemos los siguientes productos en existencia:')
def callback_query(call):
    print(call.data)