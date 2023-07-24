from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off
from pyrogram.types import Message

async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "محادثه خاصه"
        logger_text = f"""
**{MUSIC_BOT_NAME} مسجل التشغيل**

**الدردشه:** {message.chat.title} [`{message.chat.id}`]
**المعرف:** @{message.from_user.username}
**الايدي:** `{message.from_user.id}`
**رابط الدردشه:** {chatusername}

**تم البحث بواسطة:** {message.text}

**نوع المشغل:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
