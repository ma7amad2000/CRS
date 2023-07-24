import sys

from pyrogram import Client

import config

from ..logging import LOGGER

from pyrogram.enums import ChatMemberStatus

class AnonXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} تم تشغيل البوت على 𝐒𝐎𝐔𝐑𝐂𝐄•𝐂𝐑𝐘𝐒𝐓𝐀𝐋 بنجاح:**\n\n✨ ɪᴅ : `{self.id}`\n❄ الاسم : {self.name}\n💫 المعرف : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "فشل في استدعاء البوت تأكد من اضافته في المجموعه وترقيتع كمسؤول"
            )
            sys.exit()
