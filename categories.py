from config import *
from products import *

# @bot.callback_query_handler(func=lambda calls: 'Category')
# def callback_query_category(calls):
#     print(calls.data)
#     if calls.data == "101":
#         print('1')
#         showDetailsCategories(calls, "101")
#     elif calls.data == "102":
#         print('2')
#         showDetailsCategories(calls, "102")
#     elif calls.data == "103":
#         print('3')
#         showDetailsCategories(calls, "103")


# def showDetailsCategories(calls, idCategory):
#     data = {}
#     name_category = ""
#     if call.data == idCategory:
#         for x in call.message.json['reply_markup']['inline_keyboard']:
#             data = x
#             print(data)
#             for x in data:
#                 print(x)
#                 if x['callback_data'] == idCategory:
#                     name_category = x['text']
#         print(name_category)
#         productos = searchProducts_category(name_category)
#         name_products = productos['name']
#         bot.send_message(call.message.json['chat']['id'], name_products)

# @bot.message_handler(commands=['category'])
# def message_handler_category(message):
#     # print(message)
#     bot.send_message(message.chat.id, "Categorias", reply_markup=markup_gen())
