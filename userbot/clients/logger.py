# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import KAY2, KAY3, KAY4, KAY5, bot, branch, tgbot
from userbot.utils import kayscrt

MSG_ON = """
✨**ҡᴧʏ-υѕєявσт ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋғᴛɪғᴋᴀɴ**!!
━━━━━━━━━━━━━━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}ping` **untuk Mengecheck Bot**
━━━━━━━━━━━━━━━
➠ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :** @KayXChannel
"""


async def kay_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            KayUBOT = await tgbot.get_me()
            BOT_USERNAME = KayUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            KayUBOT = await tgbot.get_me()
            BOT_USERNAME = KayUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await kayscrt(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAY2:
            await kayscrt(KAY2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAY2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAY3:
            await kayscrt(KAY3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KYY3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAY4:
            await kayscrt(KAY4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAY4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAY5:
            await kayscrt(KAY5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAY5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
