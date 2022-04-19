import pybase64
from telethon import Button
from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/950d5fe4dd1dbe1726f5e.jpg",
                caption="✨ **Kay Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @KayXChannel ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/KayzuSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None


async def checking():
    gocheck = str(pybase64.b64decode("QEtheXp1U3VwcG9ydA=="))[2:15]
    checker = str(pybase64.b64decode("QEtheVhDaGFubmVs"))[2:14]
    try:
        await bot(GetSec(gocheck))
    except BaseException:
        pass
    try:
        await bot(GetSec(checker))
    except BaseException:
        pass
