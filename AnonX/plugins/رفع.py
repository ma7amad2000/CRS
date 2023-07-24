import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus 

lokrf = []

@app.on_message(
     command(["قفل الرفع","تعطيل الرفع"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــــن"
    else:   
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
     
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in lokrf:
            return await message.reply_text(f"**يا {message.from_user.mention}\n الالعاب مقفله من قبل**")
        lokrf.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الالعاب بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")

@app.on_message(
    command(["فتح الرفع","تفعيل الرفع"])
    & filters.group
)
async def idljjopen(client:Client, message:Message):
    dev = (OWNER_ID)
  
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطـور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")       
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in lokrf:
        return await message.reply_text(f"**يا {message.from_user.mention}\الالعاب معفل من قبل**")
      lokrf.remove(message.chat.id)
      return await message.reply_text(f"**تم فتح الالعاب بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 
   


klb = []

@app.on_message(command("رفع كلب"))
async def rf3nmla(client:Client, message:Message):
  
  if message.reply_to_message.from_user.mention in klb:
    klb.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n كلب من قبل {message.from_user.mention}😂♥️**")


@app.on_message(command("ت كلب"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in klb:
    klb.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة الكلاب 😂♥️ \n\n لعرض القائمه اكتب قائمة الكلاب**")


@app.on_message(command("قائمة كلاب"))
async def nml(client:Client, message:Message):
  kq = ""
  for n in klb:
      kq += n + "\n"
  await message.reply_text(f"**قائمة الكلاب لي تنبح 😂😂 \n\n{kq}**")

zoj = []


@app.on_message(command("رفع زوجي"))
async def rf3nmla(client, message:Message):
  if message.reply_to_message.from_user.mention in zoj:
    zoj.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  زوج لـ {message.from_user.mention}😂♥️ \n\n لعرض القائمه اكتب قائمة المتزوجين**")


@app.on_message(command("ت زوجي"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in zoj:
    zoj.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة المتزوجين رد عزابي 😂♥️**")


@app.on_message(command("قائمة المتزوجين"))
async def nml(client, message):
  zq = ""
  for n in zoj:
      zq += n + "\n"
  await message.reply_text(f"**قائمة العرسان 😂😂 \n {zq}**")

hth =[]


@app.on_message(command("رفع حثاله"))
async def rf3nmla(client, message:Message):
  
  if message.reply_to_message.from_user.mention in hth:
    hth.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  حثاله من قبل {message.from_user.mention}😂♥️\n\n لعرض القائمه اكتب قائمة حثاله**")


@app.on_message(command("ت حثاله"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in hth:
    hth.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة الحثاله 😂♥️**")


@app.on_message(command("قائمة حثاله"))
async def nml(client, message):
  hq = ""
  for n in hth:
      hq += n + "\n"
  await message.reply_text(f"**حثالة المجتمع 😂😂 : \n {hq}**")


zog =[]


@app.on_message(command("رفع زوجتي"))
async def rf3nmla(client, message:Message):
  if message.reply_to_message.from_user.mention in zog:
    zog.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  قعدت مرات هذا خلفو دنقات {message.from_user.mention}😂♥️ \n\n لعرض القائمه اكتب قائمة المتزوجات**")


@app.on_message(command("ت زوجتي"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in zog:
    zog.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  وصارت مطلقه جاده للزواج 😂♥️**")


@app.on_message(command("قائمة المتزوجات"))
async def nml(client:Client, message:Message):
  zzq = ""
  for n in zog:
      zzq += n + "\n"
  await message.reply_text(f"**قائمة العرسان 😂😂 \n {zzq}**")
