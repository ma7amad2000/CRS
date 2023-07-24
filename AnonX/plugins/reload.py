import asyncio

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message
from strings.filters import command
from config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from strings import get_command
from AnonX import app
from pyrogram import enums
from AnonX.core.call import Anon
from AnonX.misc import db
from AnonX.utils.database import get_authuser_names, get_cmode
from AnonX.utils.decorators import (ActualAdminCB, AdminActual,
                                         language)
from AnonX.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@app.on_message(
    command(RELOAD_COMMAND)
   
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
        chat_id = message.chat.id
        adminlist[chat_id] = []
        async for user in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if user.privileges.can_manage_video_chats == True:
                adminlist[chat_id].append(user.user.id)
        await message.reply_text(_["admin_20"])


@app.on_message(
    command(RESTART_COMMAND)
 
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"يرجى الانتظار الاعادة التشغيل {MUSIC_BOT_NAME} في الدردشه الخاصه بك."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Anon.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Anon.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        f"تم اعادة التشغيل بنجاح {MUSIC_BOT_NAME}في دردشتك يمكنك بدء التشغيل..."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.message_id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "تم التحميل مسبقا.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "تم التحميل مسبقا.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "تم الغاء التحميل", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"تم الغاء التحميل بواسطة : {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "فشل التحميل...", show_alert=True
            )
    await CallbackQuery.answer(
        "فشل في التعرف على.", show_alert=True
    )
