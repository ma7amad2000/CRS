import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID, MUSIC_BOT_NAME
from pyrogram import filters

txt = [

            f"انت البوت يلي راسك مربعع اسمي {MUSIC_BOT_NAME}",


             f"اسمي {MUSIC_BOT_NAME} مكتوب الخط العريضض",
            

            f"معش تعيطط بوت بوت اسمميي {MUSIC_BOT_NAME}",
            
            
           f"لنا الله",
            
            
            f"حسبي الله فيك اسمي {MUSIC_BOT_NAME} 🙂",
            
            
            f"ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]
txt1 = [

            "**؏ـيوٍڼ 😻🫶 البوت يا مطوريي**",


             "**ااحسنن مطوور فالدنياا كلههاا**",
            

            "**اطلق من يصيحح بووت**",
            
            
           
            
            
 
            
            

        ]



        


@app.on_message(command(["بوت"]))


async def cutt(client: Client, message: Message):
     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(


         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       
     
        
