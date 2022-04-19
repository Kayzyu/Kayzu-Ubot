# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, KAY2, KAY3, KAY4, KAY5):
    user_ids = list(SUDO_USERS) or []
    kay_id = await bot.get_me()
    user_ids.append(kay_id.id)

    try:
        if KAY2 is not None:
            id2 = await KAY2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if KAY3 is not None:
            id3 = await KAY3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if KAY4 is not None:
            id4 = await KAY4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if KAY5 is not None:
            id5 = await KAY5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTkwNDc5MTMzOA==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        KAY_CLIENT = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        KYY_CLIENT = client.first_name
    kyy_rpk = f"[{KAY_CLIENT}](tg://user?id={OWNER_ID})"
    return OWNER_ID, KAY_CLIENT, kyy_rpk
