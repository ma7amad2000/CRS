import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال يامطووري يبووك @bp_bp 🥺❤",


             "هذا مطوري @bp_bp🥺❤",
            

             "يببووكككككككك @bp_bp 🙂😒",
            
           
 
            
            

        ]


        


@app.on_message(command(["وسكي","الوسكي","ويسكي"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
