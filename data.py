from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣️", url="https://t.me/flirting_chating"),
         InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://t.me/tiger_iz_here"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Mᴀᴅᴇ ᴡɪᴛʜ pyar😏 ʙʏ : [TIGER](https://t.me/tiger_iz_here) !
    """
