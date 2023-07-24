# from pyrogram import Client, filters
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
# from config import * 
# from strings.filters import command
# from AnonX import app, Telegram

# @app.on_message(filters.command(["start"]))
# def start(client:Client, message:Message):
#     SUPPORT_CHANNEL = "{SUPPORT_CHANNEL}"

#     bot_button = InlineKeyboardMarkup(
#         [[
#             InlineKeyboardButton("زيارة القناة", url=f"{SUPPORT_CHANNEL}"),
#             InlineKeyboardButton("تحقق من الاشتراك", callback_data="check_subscription")
#         ]]
#     )

#     message.reply_text("مرحبًا بك! اضغط على أحد الأزرار بالأسفل للاشتراك.", reply_markup=bot_button)

# @app.on_callback_query()
# def callback_handler(client:Client, callback):
#     if callback.data == "check_subscription":
#         channel_id = CHANNEL_ID 

#         if client.get_chat_member(chat_id= channel_id, user_id= callback.from_user.id).status == "member":
#             callback.answer("تم التحقق من الاشتراك! مستخدم صالح.", show_alert=True)
