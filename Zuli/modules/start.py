from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Zuli import Zuli
from config import BOT_USERNAME

start_txt = """**
ɪ ᴀᴍ ɴᴏᴛᴛʏʏ

ɪ ᴀᴍ ʙᴜɪʟᴛ ʙʏ ᴄᴏᴍʙɪɴɪɴɢ ᴠᴀʀɪᴏᴜꜱ ᴀɪ ᴄᴀᴘᴀʙɪʟɪᴛɪᴇꜱ. ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀɴꜱᴡᴇʀꜱ ᴛᴏ ᴀʟʟ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴꜱ, ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴀꜱᴋ ᴍᴇ ᴀɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ ʏᴏᴜ ʜᴀᴠᴇ. ᴀᴅᴅɪᴛɪᴏɴᴀʟʟʏ, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ɪᴍᴀɢᴇꜱ ᴀɴᴅ ᴇᴠᴇɴ ᴇᴅɪᴛ ᴄᴏɴᴛᴇɴᴛ. ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀᴛ ᴍʏ ᴅɪꜱᴘᴏꜱᴀʟ
**"""




@Zuli.on_message(filters.command("on"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝐒ᴜᴍᴍᴏɴ 𝐌ᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs", url="https://t.me/AloneXBots"),
          InlineKeyboardButton("𝐃ᴇᴠ", url="https://t.me/ALONE_WAS_BOT"),
        ],
        [
          InlineKeyboardButton("𝐂ᴏᴍᴍᴀɴᴅs", callback_data="help_")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/233a6f44e3f009c1e6724.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )





