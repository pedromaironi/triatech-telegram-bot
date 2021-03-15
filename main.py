# -*- coding: utf-8 -*-
from config import *
from start import *

def main():
    pass

bot.polling()#none_stop=True

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()