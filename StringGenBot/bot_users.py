from pyrogram.types import Message
from pyrogram import Client, filters
from StringGenBot.db import SESSION
from StringGenBot.db.users_sql import Users, num_users
import asyncio

@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user([5212270860, 2007758161]) & filters.command("users"))
async def _stats(_, msg: Message):
    users = await num_users()
    count = await msg.reply("__Counting... Wait Sur !! 🌚__")
    await asyncio.sleep(1.5)
    if users < 100:
        await count.edit(f"#sᴇᴅ\n\nᴏɴʟʏ `{users}` ᴘᴇᴏᴘʟᴇs ᴀʀᴇ ᴜsɪɴɢ ᴍᴇ.")
    else:
        await count.edit(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs : {users} ")
