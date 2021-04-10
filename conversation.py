# # -*- coding: utf-8 -*-
from config import *
import difflib

# def markup_add(name, name_callback):
#     markup.add(InlineKeyboardButton(name, callback_data=name_callback))

# def markup_add_category(name, name_callback):
#     print("name: " + str(name) + "namec: " + str(name_callback))
#     markup_category.add(InlineKeyboardButton(name, callback_data=name_callback))

# @bot.message_handler(func=lambda Message: True)
# def handle_messages(Message):
#     # Variables
#     product_band = False
#     category_band = False
#     pc_band = False
#     user_name = Message.json['from']['first_name']
#     message_response = ''

#     # word save the message from the user
#     word = Message.json['text']

#     # Sentence write for the user
#     first_word = word

#     # Read the json
#     with open('extra_data/conv.json', 'r') as file:
#         words = json.load(file)

#     s = first_word.split(' ')

#     # words from sentence of user message
#     for words_from_user in s:
#         # print('words_from_user: ' + words_from_user)
#         if(words_from_user.lower() == 'productos' or words_from_user.lower() == 'producto' or words_from_user.lower() == 'products' or words_from_user.lower()== 'productos' ):
#             product_band = True
#             print('product_band: ' + str(product_band))
#         elif(words_from_user.lower() == 'categorias' or words_from_user.lower() == 'categoria' or words_from_user.lower() == 'category' or words_from_user.lower()=='categories' ):
#             category_band = True
#             print('category_band: ' + str(category_band))
#         elif(words_from_user.lower() == 'computadora' or words_from_user.lower() == 'computadoras' or words_from_user.lower() == 'pc' or words_from_user.lower() == 'pc gamer'):
#             pc_band = True
#             print('pc_band: ' + str(pc_band))
#     # words from sentence of conversation.json

#     for words_from_conv in words:
#         # print("words_from_conv" + words_from_conv)
#         # This condition is for search similitude between first_word and words_from_conversation.json
#         if(first_word.lower() == words_from_conv):
#             # print("words[words_from_conv]: " + words[words_from_conv])
#             if(product_band):
#                 bot.reply_to(Message, words[words_from_conv] , reply_markup=gen_markup())
#             if(category_band):
#                 bot.reply_to(Message, words[words_from_conv] , reply_markup=markup_gen())
#             if(pc_band):
#                 bot.reply_to(Message, words[words_from_conv] , reply_markup=markup_gen())

# @bot.callback_query_handler(func=lambda call: 'Tenemos la siguiente lista de categorias:')
# def callback_query_categories(call):
#     pass
# #     # print("call: " + call)
# # # @bot.message_handler(commands=['category'])
# # # def message_handler(message):
# # #     bot.send_message(message.chat.id, "Categorias", reply_markup=gen_markup())
