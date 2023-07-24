import asyncio
import time
import json
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from pyrogram.enums import ChatType, ParseMode
import config
import requests
import redis, re
from pyrogram import *
from config import (OWNER_ID ,
		     USER_OWNER,
	         MUSIC_BOT_NAME,
	         SUPPORT_CHANNEL,
	         BOT_TOKEN,
	         BANNED_USERS)
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.formatters import get_readable_time
from AnonX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)
loop = asyncio.get_running_loop()
token = (BOT_TOKEN)
bot_id = app.bot_token.split(":")[0]
r = redis.from_url('redis://')
owner = (OWNER_ID)
dev_owner = int(5676384368)
@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            dev = (OWNER_ID, 6275847466,5676384368)
          
		
            keyboard = help_pannel(_)
            user = message.from_user.id
            if int(user) == dev_owner:
                await message.reply(f"**𖢿 | : مرحبا حبيبي كرستال مطور السورس{message.from_user.mention}\n𖢿 | : كل اقسام التحكم بالبوتات\n𖢿 | : تستطيع التحكم بكل البوتات عن طريق هذه الازرار**",reply_markup=OwnerM)
					
            elif message.from_user.id in owner:
		           
                   await message.reply(f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",reply_markup=main_dev_key)
                        
 
            else:  
                   await message.reply_text(f"**اهلا عزيزي {message.from_user.mention}\n\n في بوت الميوزك {MUSIC_BOT_NAME} الخاص بي @{USER_OWNER} \n\n هذا بوت تشغيل اغاني وبه الكثير من المميزات الجميله \n\n ارفع البوت مشرف وهايرفعك مالك ويرفع المشرفين تلقائي**",reply_markup=Owneruser)
                   return await message.reply_photo(
                       photo=config.START_IMG_URL,
                       caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )

            

        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 يتم جلب الاحصائيات الخاصه لـ {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[قناة السورس](https://t.me/VVHH9) ** ᴩʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ضغط ستارت على البوت <code>دخل على قائمة المطورين</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(f"ʜᴇʏ {message.from_user.first_name},\nشكرا لوثوقك في انا  {config.MUSIC_BOT_NAME}, تم تخزين بياناتك اللازمه يمكنك التشغيل الان")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention}ضغط ستارت على البوت <code>تحقق من نفسه</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("دقيقه يقلبي وحانجيب البيانات")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
😲**جلب المعلومات**😲
📌 **العنوان:** {title}

⏳ **المده:** {duration} دقيقه
👀 **المشاهدات:** `{views}`
⏰ **نشرت في:** {published}
🎥 **القناه:** {channel}
📎 **رابط القناه:** [عرض القناه]({channellink})
🔗 **الرابط:** [مشاهده في اليوتيوب]({link})
💖 بحث بواسطة {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• ʏᴏᴜᴛᴜʙᴇ •", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="• قناة السورس •", url="https://t.me/VVHH9"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention}ضغط ستارت على البوت<code>جلب المعلومات</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                owner = (OWNER_ID) 
                user = message.from_user.id
                if int(user) == dev_owner: 
                   return await message.reply(f"**𖢿 | : مرحبا حبيبي كرستال مطور السورس{message.from_user.mention}\n𖢿 | : كل اقسام التحكم بالبوتات\n𖢿 | : تستطيع التحكم بكل البوتات عن طريق هذه الازرار**",reply_markup=OwnerM)
                if message.from_user.id in owner: 
                   return await message.reply_text(f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",reply_markup=main_dev_key)
                else:  
                   await message.reply_text(f"**اهلا عزيزي {message.from_user.mention}\n\n في بوت الميوزك {MUSIC_BOT_NAME} الخاص بي @{USER_OWNER} \n\n هذا بوت تشغيل اغاني وبه الكثير من المميزات الجميله \n\n ارفع البوت مشرف وهايرفعك مالك ويرفع المشرفين تلقائي**",reply_markup=Owneruser)
                   return await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
    
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ضغط ستارت في البوت.\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
            )
        

@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**بوت ميوزك خاص**\n\فقط الدردشات المصرح بها بواسطة المطور."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return


OwnerM = ReplyKeyboardMarkup([
[("رفع مالك"),("تنزيل مالك"),("المالكين"),("حذف المالكين")],
[("الغاء")], 
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه الكل")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("روابط المجموعات")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍ قسم معرف المطور ◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("عرض معرف المطور"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("اضافه معرف المطور"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("حذف معرف المطور"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)
main_dev_key = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("الغاء")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 
[("◍ قسم الاشتراك ◍")],
[("عرض قناة الاشتراك")],
[("اضف قناة اشتراك اجباري")],
[("حذف قناه الاشتراك")],
[("الغاء")],
[("◍ قسم المطور ◍")],
[("عرض قناة المطور")],
[("اضافه قناه المطور")],
[("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)

Owneruser = ReplyKeyboardMarkup([
[("الاوامر"),("السورس")],[("المطور"),("مبرمج السورس"),("/مساعده")],
[("غنيلي"),("كت"),("صور")],
[("اذكار"),("مميزات"),("ذكاء اصتناعي")],
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)
