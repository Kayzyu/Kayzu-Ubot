from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.sc$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("ππΌππΌπππππππππ ππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππππππ₯Ίπ₯Ίπ₯Ί")
        sleep(1)
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππΌππΌπππππππ₯Ίπ₯Ί")
        sleep(1)
        await e.edit("πΌππ ππΌπππππππ ππ")
        sleep(1)
        await e.edit("πΌππππ πππππππππ ππ ππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππΌππΌπΌπππππ ππ")
        sleep(1)
        await e.edit("πππππππ πππππ₯Ίπ₯Ίπ₯Ί")
        sleep(1)
        await e.edit("πππππππππππ₯Ίπ₯Ί")
        sleep(1)
        await e.edit("πΌπππ ππΌππππππ ππ")
        sleep(1)
        await e.edit("π ππππ πππππππ")
        sleep(1)
        await e.edit("ππππππΌπΌπΎπΎπππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("πΌππ ππΌππΌππ ππΌπππ")
        sleep(1)
        await e.edit("ππππππΌπΌπΌπΎπΎπΎπππππππ")


CMD_HELP.update({
    "sleepcall":
    "πΎπ€π’π’ππ£π: `.sc`"
    "\nUsage: Cobain Sendiri"
})
