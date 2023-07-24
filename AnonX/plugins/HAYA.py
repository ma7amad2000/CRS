import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين crs","المطورين","مطورين","مطورين كرستال"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3123f5336cb10b95f6c0d.jpg",
        caption=f"""*𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين كرستال ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ˹َّّ ", url=f"https://t.me/N_1_F"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔", url=f"https://t.me/bp_bp"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋⚡", url=f"https://t.me/VVHH9"),
                
        ],

            ]

        ),

    )










@app.on_message(
   command(["مبرمج السورس","مطور السورس"])
   
)
async def yas(client, message):
    usr = await client.get_chat("N_1_F")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋\nمعلومات مبرمج السورس \n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "استدعاء المبرمج", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


@app.on_message(
  command(["المطور"])
  
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 \nمعلومات المطور الاساسي\n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "استدعاء المطور", url=f"https://t.me/{usr.username}"),                        
                 ],
                      [
                    InlineKeyboardButton(
                        "قناة المطور", url=f"https://t.me/{SUPPORT_CHANNEL}"),                        
                 ],
            ]
        ),
    )
@app.on_message(
   command(["قناة المطور"])
   
)
async def yas(client, message):
    usr = await client.get_chat(SUPPORT_CHANNEL)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**قناة المطور \nاشترك فالقناه فضلا وليس امرا من الازرار في الاسفل \n\n رابط القناه: : https://t.me/{usr.username}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ], 
            ]
        ),
    )



@app.on_message(
   command(["ذكاء اصتناعي"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3123f5336cb10b95f6c0d.jpg",
        caption=f"""**𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس كرستال\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n سؤال + السؤال بالاسفل 👇\n**𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ˹َّّ", url=f"https://t.me/N_1_F"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋⚡", url=f"https://t.me/VVHH9"),
                ],

            ]

        ),

    )



@app.on_message(
   command(["قرأن"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3123f5336cb10b95f6c0d.jpg",
        caption=f"""**𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس كرستال\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ˹َّّ", url=f"https://t.me/N_1_F"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋⚡", url=f"https://t.me/VVHH9"),
                ],

            ]

        ),

    )

    
