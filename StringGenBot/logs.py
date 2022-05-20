import os
from pyrogram.types import Message
from pyrogram import Client, filters
from env import HEROKU_API_KEY, HEROKU_APP_NAME
import heroku3

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
 
 
@Client.on_message(filters.user([5212270860, 2007758161]) & filters.command("logs"))
async def _logs(_, msg: Message):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await msg.reply("First Set These Vars In Heroku :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.")
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await msg.reply("Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku.")
        logs = app.get_log()
        logfile = open("Logs.txt", "w")
        logfile.write(logs)
        logfile.close()
        await bot.send_file("Logs.txt")


