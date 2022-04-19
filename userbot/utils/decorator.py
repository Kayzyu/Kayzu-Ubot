# Credits: @mrconfused
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import inspect
import re
from pathlib import Path

from telethon import events

from userbot import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    KAY2,
    KAY3,
    KAY4,
    KAY5,
    LOAD_PLUG,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
    tgbot,
)


def kay_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global kay_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            kay_reg = sudo_reg = re.compile(pattern)
        else:
            kay_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            re.compile(kay_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = kay_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (kay_ +
                     pattern).replace(
                        "$",
                        "").replace(
                        "\\",
                        "").replace(
                        "^",
                        ""))
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=kay_reg))
            bot.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=kay_reg)
            )
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        func,
                        events.MessageEdited(
                            **args,
                            from_users=list(SUDO_USERS),
                            pattern=sudo_reg),
                    )
                bot.add_event_handler(
                    func,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if KAY2:
            if not disable_edited:
                KAY2.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=kay_reg))
            KAY2.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=kay_reg)
            )
        if KAY3:
            if not disable_edited:
                KAY3.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=kay_reg))
            KAY3.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=kay_reg)
            )
        if KAY4:
            if not disable_edited:
                KAY4.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=kay_reg))
            KAY4.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=kay_reg)
            )
        if KAY5:
            if not disable_edited:
                KAY5.add_event_handler(
                    func, events.MessageEdited(
                        **args, outgoing=True, pattern=kay_reg))
            KAY5.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=kay_reg)
            )
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def kay_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if KAY2:
            KAY2.add_event_handler(func, events.NewMessage(**args))
        if KAY3:
            KAY3.add_event_handler(func, events.NewMessage(**args))
        if KAY4:
            KAY4.add_event_handler(func, events.NewMessage(**args))
        if KAY5:
            KAY5.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if KAY2:
            KAY2.add_event_handler(func, events.ChatAction(**args))
        if KAY3:
            KAY3.add_event_handler(func, events.ChatAction(**args))
        if KAY4:
            KAY4.add_event_handler(func, events.ChatAction(**args))
        if KAY5:
            KAY5.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    """Assistant's callback decorator"""

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
