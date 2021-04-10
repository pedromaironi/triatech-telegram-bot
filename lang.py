# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  lang.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(
    types.KeyboardButton('ESPAÑOL'),
    types.KeyboardButton('ENGsLISH')
    )


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'IDIOMA',
        'LANGUAGE'])

@bot.message_handler(commands=['lang'])
def command_lang(m):
    cid = m.chat.id
    uid = m.from_user.id
    # try:
    #     pass
    # except Exception as e:
    #     bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    # if not is_recent(m):
    #     return None
    # if is_user(cid):
    #     bot.send_chat_action(cid, 'typing')
    #     bot.send_message(
    #         cid, responses['lang_1'][
    #             lang(cid)], reply_markup=markup)
    #     userStep[cid] = 'lang'
    # else:
    #     bot.send_chat_action(cid, 'typing')
    #     bot.send_message(cid, responses['not_user'])
