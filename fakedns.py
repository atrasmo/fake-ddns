#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import telepot
from requests import get

##This is the TOKEN for bot 
TOKEN = '372667382:AAEyXVmZBgakjpsajdiik90hvJQZSYYJ'
##This is the channel name
chat_id ='@<channel-name>'

bot = telepot.Bot(TOKEN)

ip = get('https://api.ipify.org').text
bot.sendMessage(chat_id, "L'indirizzo IP ora è: {}".format(ip))
