import asyncio
from datetime import datetime

from Panda import pandaub
from . import mention
from ..core.managers import edit_or_reply

plugin_category = "plugins"


@pandaub.ilhammansiz_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        pandaevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await pandaevent.edit("`🚶`")
        await asyncio.sleep(0.3)
        await pandaevent.edit("`🏃`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await pandaevent.edit(f"Ping\n`{ms} ms`")
    else:
        pandaevent = await edit_or_reply(event, "|")
        await pandaevent.edit("__T__")
        await pandaevent.edit("__Te__")
        await pandaevent.edit("__Tes__")
        await pandaevent.edit("__Test__")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await pandaevent.edit(
            f"╭《 **U S E R B O T** 》\n"
            f"┗☉ **Ping =** `{ms} ms`\n"
            f"┗☉ **Milik =*# {mention} "
        )
