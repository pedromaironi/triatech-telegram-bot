# -*- coding: utf-8 -*-
from config import *
from start import *
from products import *
from shop import *
from help import *
from contact import *
from conversation import *
from categories import *
import emails

def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)