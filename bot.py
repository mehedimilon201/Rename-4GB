from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyrogram.utils

pyrogram.utils.MIN_CHAT_ID = -4837590077
pyrogram.utils.MIN_CHANNEL_ID = -1002682807987



bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))




if STRING_SESSION:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()




# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
