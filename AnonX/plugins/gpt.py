import requests
import json
from AnonX import app
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from strings.filters import command

url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

def gpt(text) -> str:
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message':text,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except:
        return None

def reply_gpt(client, message:Message):
    text = message.text.split("سؤال ")[1]
    reply_text = gpt(text)
    chat_id = message.chat.id
    if message.reply_to_message is not None:
        message_id = message.reply_to_message.id
    else:
        message_id = None
    client.send_message(chat_id=chat_id, text=reply_text + "\n\n\n تم استخدام أحدث إصدار من الذكاء الاصطناعي 3.5 مطور من قبل @N_1_F", reply_to_message_id=message_id)

@app.on_message(command("سؤال"))
def reply(client, message:Message):
    message.reply_text(f"**مرحبا بـك يا {message.from_user.mention}\n\n اكتب سؤالك بالكامل وسوف يتم الرد عليك فورا**")
    reply_gpt(client, message)
