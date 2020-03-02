'''
LorxTeam Bot Base
Created By: Ent33r
Date: Feb 20 2020
'''
'''
Info about plugin:
Saying "Hello" to all messages
'''


#The main part of imports(From telegram.ext or telegram)
from telegram.ext import Updater #Blank #<= This import required
from telegram.ext.dispatcher import run_async
#Import all you need from telegram following "Updater"

#Importing modules from base that you need in your plugin
from base import up #<= This import required

#Importing details
import requests




#Start of your methods plugin
@run_ansyc
def Hello(update, context):
    update.message.reply_text('Hello')

#Adding method as a hendler
up.dispatcher.add_handler(Hello)
