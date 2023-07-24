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

            f"؏ـيوٍڼ {MUSIC_BOT_NAME}😻🫶",


             "ﻧ؏ـ۾ 🥺❤",
            

            "هہذآ آڛـﻤــي 🫶😻",
            
            
            f"ضـوꪆ {MUSIC_BOT_NAME}،💗🧸!َ''))",
            
            
            "نعٓم يـﺣـبـعـﻣـري،🥺🧡🌸!َ''))",
            
            
             "ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]
txt1 = [

            f"**؏ـيوٍڼ {MUSIC_BOT_NAME}😻🫶 يا مطوريي**",


             f"**ﻧ؏ـم يامطوريي**",
            

            f"**امرني يا مطوري الحبيب**",
            
            
           
            
            
 
            
            

        ]



        


@app.on_message(command([MUSIC_BOT_NAME]))


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
       
     
        
