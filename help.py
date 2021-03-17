# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  inline_help.py importado.{/cyan}'))


@bot.message_handler(commands=['help'])
def query_help(message):
    txt = str(responses['help_1']['es']) + "\n" + str(responses['help_2']['es']['notify']) + "\n" + str(responses['help_2']['es']['products']) + "\n" + str(responses['help_2']['es']['credits']) + "\n" + str(responses['help_2']['es']['me']) + "\n" + str(responses['help_2']['es']['contact']) + "\n" + str(responses['help_2']['es']['cancel']) + "\n" + str(responses['help_2']['es']['info']) + "\n" + str(responses['help_2']['es']['help']) + "\n"
    bot.reply_to(message, txt)
    print(txt)

# @bot.message_handler(commands=['contact'])
# def query_contact(message):
#     txt = str(responses['help_1']['es']) + "\n" + str(responses['help_2']['es']['notify']) + "\n" + str(responses['help_2']['es']['products']) + "\n" + str(responses['help_2']['es']['credits']) + "\n" + str(responses['help_2']['es']['me']) + "\n" + str(responses['help_2']['es']['contact']) + "\n" + str(responses['help_2']['es']['cancel']) + "\n" + str(responses['help_2']['es']['info']) + "\n" + str(responses['help_2']['es']['help']) + "\n"
#     bot.reply_to(message, txt)
#     print(txt)
