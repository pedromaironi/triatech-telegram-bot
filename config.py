#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################
#                   BOT TOKEN #
#################################################

import os
import telebot
from telebot import types
from colorclass import Color
import json
import time
import six
import sys
import traceback
import re
from collections import OrderedDict
import pymongo
from pymongo import MongoClient
import requests
import random
from random import choice
from bson.objectid import ObjectId
from pprint import pprint
MONGO_HOST = ''
MONGO_PORT = ''
MONGO_TIME = 0
MONGO_BASE_DATA = ''
MONGO_COLLECTION = ''


#################################################
#          CONFIG AND METHODS                   #
#################################################
# Get token from Data
with open('extra_data/data.json', 'r') as file:
   extra = json.load(file)
   #print(extra)

# Get MongoConfig
with open('extra_data/mongo.json', 'r') as file:
   mongo = json.load(file)
   MONGO_HOST = mongo['MONGO_HOST']
   MONGO_PORT = mongo['MONGO_PORT']
   MONGO_TIME = mongo['MONGO_TIME']
   MONGO_BASE_DATA = mongo['MONGO_BASE_DATA']

# get responses from json
with open('extra_data/responses.json', encoding='utf-8') as f:
    responses = json.load(f)#, object_pairs_hook=OrderedDict
    # print(responses)

# Instanciate the bot and the mongo
try:
    bot = telebot.TeleBot(extra['token'])
    MONGO_URI = 'mongodb://' + MONGO_HOST+':'+MONGO_PORT+'/'
    client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME)
    db = client.bot
    print('Connection successful')
except pymongo.errors.ServerSelectionTimeoutError as errorTime:
    print('Time lose: ' + errorTime)
except pymongo.errors.ConnectionFailure as errorConnection:
    print('Connection: ' + errorConnection)



def create_user():#id, first_name,last_name,username,language_code
    MONGO_COLLECTION = 'usuarios'
    base_data = client[MONGO_BASE_DATA]
    collection = base_data[MONGO_COLLECTION]
    with open('extra_data/user.json') as f:
        data = json.load(f)
    collection.insert_one(data)

def is_user(cid):
    return db.usuarios.find_one(str(cid)) is not None and db.usuarios.find_one(str(cid))['active'] == True

def showInfoUser(uid):
    MONGO_COLLECTION = 'usuarios'
    base_data = client[MONGO_BASE_DATA]
    collection = base_data[MONGO_COLLECTION]
    # print(uid)
    find = {"id":uid}
    return collection.find_one(find)

def confirm_user(uid):
    MONGO_COLLECTION = 'usuarios'
    base_data = client[MONGO_BASE_DATA]
    collection = base_data[MONGO_COLLECTION]
    # print(uid)
    find = {"id":uid}
    return collection.find(find).count()

def count_products():
    MONGO_COLLECTION = 'productos'
    base_data = client[MONGO_BASE_DATA]
    collection = base_data[MONGO_COLLECTION]
    return collection.find().count()

def showInfoProducts():
    MONGO_COLLECTION = 'productos'
    base_data = client[MONGO_BASE_DATA]
    collection = base_data[MONGO_COLLECTION]
    return collection.find()

def showDetailsProducts(name):
    MONGO_COLLECTION = 'productos'
    base_data = client[MONGO_BASE_DATA]
    collection = base_data[MONGO_COLLECTION]
    # print(uid)
    find = {"name":name}
    return collection.find_one(find)









def send_exception(exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = traceback.extract_tb(exc_tb, 4)
    message = '\n`' + str(exc_type) + '`'
    message += '\n\n`' + str(exc_obj) + '`'
    for row in tb:
        message += line()
        for val in row:
            message += '`' + str(val) + '`\n'
    return message

def to_json(m):
    d = {}
    for x, y in six.iteritems(m.__dict__):
        if hasattr(y, '__dict__'):
            d[x] = to_json(y)
        else:
            d[x] = y
    return d