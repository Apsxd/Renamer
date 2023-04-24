import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5817904504:AAHfBRRANKN-8tpMG74SGbwvE9N25RR6_zI")

API_ID = int(os.environ.get("API_ID", "22331950"))

API_HASH = os.environ.get("API_HASH", "112e87ded984e6d03d3197decac00f4e")

STRING = os.environ.get("STRING", "BACxmMXVr67xSe2t0E900BwnJDP4PJ1XSsNSRVkG5ZRQSDspNBntw2DZ1J-Wo9ElFc9eJ51s-ewvSR_fPZazickEljrnx1eCrMOmWnibTHbdFovBxCQRCwFZ5_Sf6GUMQA-jyOxJDC-5r04z-ZGqvaJGkr3dPFp4QpCipiwxDgLDfubWTMdC09vq48tmTd1-S_oqbk-nMWLL7iM9n3YaRbr9HeM02A1s3jxt_LXj-ejZWWbFDBm4NRFk6rGr28_GwPIWqoP-ZqOQn5zBZYTv6q9ziyV63fudQbWQSSblcaPcRuqaVcZ-8Slk2JFTjzdpAM5ttPud80VzwqWtzGp_SNtlAAAAAWBtLzUA")



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
