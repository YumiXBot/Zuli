from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Zuli import Poki



start_txt = """**
ʜᴇʏ, ɪ ᴀᴍ ᴛʜᴇ ɴᴏᴛᴛʏʏ ʙᴏᴛ. ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ɢᴀᴍᴇꜱ ꜰᴏʀ ʏᴏᴜ ᴛᴏ ᴇɴᴊᴏʏ, ᴀɴᴅ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴄʀᴇᴀᴛᴇᴅ ᴘᴜʀᴇʟʏ ꜰᴏʀ ᴇɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ. ᴊᴜꜱᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ɢᴀᴍᴇꜱ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʜᴀᴠᴇ ꜰᴜɴ ᴘʟᴀʏɪɴɢ.
**"""




@Poki.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝐆ᴀᴍᴇꜱ", url="https://poki.com")
        ],
        [
          InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs", url="https://t.me/AloneXBots"),
          InlineKeyboardButton("𝐃ᴇᴠ", url="https://t.me/ALONE_WAS_BOT"),
      
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/c94e27226d97b06bab820.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


