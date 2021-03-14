# -*- coding: utf-8 -*-
from config import *
from start import *
def main():
    pass

while True:
	try:
		bot.polling()#none_stop=True
	except Exception as e:
		time.sleep(15)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()