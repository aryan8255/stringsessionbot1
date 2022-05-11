import os
from pyrogram.types import Message
from pyrogram import Client, filters

@Client.on_message(filters.user(5212270860, 2007758161) & filters.command("update"))
async def _stats(_, msg: Message):
    await msg.reply("Updating...\nWait Sur !! 🌚")
    os.system("rm -rf stringsessionbot1")
    os.system("git clone https://github.com/aryan8255/stringsessionbot1")
    os.system("cd stringsessionbot1 && python3 bot.py")
