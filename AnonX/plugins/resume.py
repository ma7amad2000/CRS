from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from config import BANNED_USERS
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import is_music_playing, music_on
from AnonX.utils.decorators import AdminRightsCheck
from AnonX.utils.inline.play import close_keyboard

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    command(RESUME_COMMAND)
  
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _):
    await message.reply_text(
        _["admin_4"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )
