import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "2019249814:AAGvigNYy6CihdihRdhzcQpYiGOLVU6cPdY")

API_ID = int(os.environ.get("API_ID", "6764849"))

API_HASH = os.environ.get("API_HASH", "682f2b9a44e0aab50c6e559963e19ff0")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
