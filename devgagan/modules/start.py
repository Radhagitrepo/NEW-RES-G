from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("✨ Join Channel ✨", url="https://t.me/tg_bots_radha")],
        [InlineKeyboardButton("💵 Buy Premium 💵", url="https://t.me/i_am_radha")]
        [InlineKeyboardButton("📕 Free Course 📕", url="https://t.me/Free_study_material_By_Radha")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://telegra.ph/file/ef9db8df89cbfa68d2d1d.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
