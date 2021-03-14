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
import socket
from collections import OrderedDict
import pymongo
from pymongo import MongoClient
import requests
from random import choice
from bson.objectid import ObjectId

MONGO_HOST = ''
MONGO_PORT = ''
MONGO_TIME = 0
MONGO_BASE_DATA = ''
MONGO_COLLECTION = 'productos'


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

# Instanciate the bot and the mongo
try:
    bot = telebot.TeleBot(extra['token'])
    MONGO_URI = 'mongodb://' + MONGO_HOST+':'+MONGO_PORT+'/'
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME)
    db = client.bot
except pymongo.errors.ServerSelectionTimeoutError as errorTime:
    print('Time lose: ' + errorTime)
except pymongo.errors.ConnectionFailure as errorConnection:
    print('Connection: ' + errorConnection)

# get responses from json
with open('extra_data/responses.json', encoding='utf-8') as f:
    responses = json.load(f, object_pairs_hook=OrderedDict)
    #print(responses)

def is_recent(m):
    return (time.time() - m.date) < 60

def get_user():
    return db.usuarios.find_one()

print(get_user())