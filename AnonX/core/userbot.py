import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            "cl1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            "cl2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            "cl3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            "cl4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            "cl5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Gettings Assistants Info...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("DevilsHeavenMF")
                await self.one.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Started as {self.one.name}"
            )
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} تم بدأ التشغيل :**\n\n✨ الايدي : `{self.one.id}`\n❄ الاسم : {self.one.name}\n💫 المعرف : @{self.one.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"فشل حساب المساعد 1 في الوصول إلى مجموعة السجل. تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيته كمسؤول ! "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("DevilsHeavenMF")
                await self.two.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} تم بدأ التشغيل :**\n\n✨ الايدي : `{self.two.id}`\n❄ الاسم : {self.two.name}\n💫 المعرف : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"فشل حساب المساعد 1 في الوصول إلى مجموعة السجل. تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيته كمسؤول ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Two Started as {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("DevilsHeavenMF")
                await self.three.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} تم بدأ التشغيل :**\n\n✨ الايدي : `{self.three.id}`\n❄ الاسم : {self.three.name}\n💫 المعرف : @{self.three.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"فشل حساب المساعد 1 في الوصول إلى مجموعة السجل. تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيته كمسؤول ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("DevilsHeavenMF")
                await self.four.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} تم بدأ التشغيل :**\n\n✨ الايدي : `{self.four.id}`\n❄ الاسم : {self.four.name}\n💫 المعرف : @{self.four.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"فشل حساب المساعد 1 في الوصول إلى مجموعة السجل. تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيته كمسؤول ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("DevilsHeavenMF")
                await self.five.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} تم بدأ التشغيل :**\n\n✨ الايدي : `{self.five.id}`\n❄ الاسم : {self.five.name}\n💫 المعرف : @{self.five.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"فشل حساب المساعد 1 في الوصول إلى مجموعة السجل. تأكد من إضافة مساعدك إلى مجموعة السجل الخاصة بك وترقيته كمسؤول ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.name}"
            )
