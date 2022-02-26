import time
from platform import python_version, uname

from telethon import version
import asyncio
from Panda import StartTime, pandaub, pandaversion

from ..Config import Config
from ..helpers.functions import get_readable_time
from ..sql_helper.globals import gvarstatus
from pytgcalls import __version__
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "Panda New Userbot"

from ..sql_helper.globals import gvarstatus
from ..core.data import _sudousers_list

# ================= CONSTANT =================
DEFAULTUSER = str(Config.ALIVE_NAME) if Config.ALIVE_NAME else uname().node
# ============================================
EMOJI = gvarstatus("EMOJI") or "🎨"
NAME = gvarstatus("NAME") or DEFAULTUSER

plugin_category = "plugins"

ilhammansizzz = "https://github.com/ilhammansiz/PandaX_Userbot"
support = "https://t.me/TEAMSquadUserbotSupport"
SUDO = gvarstatus("sudoenable")
SUDOuser = _sudousers_list()

LOGO = Config.ALIVE_PIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/37b52b38dffb858cccf49.jpg"



@pandaub.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def redis(alive):
    await PandaBot.get_me()
    await get_readable_time((time.time() - StartTime))
    await alive.edit("꧁༺ Panda Userbot ༻꧂")
    await alive.edit("꧁༺ Userbot ༻꧂")
    await asyncio.sleep(1)
    if LOGO:
        try:
            logo = LOGO
            await alive.delete()
            msg = await PandaBot.send_file(alive.chat_id, logo, caption=aliveess)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


aliveess = f"""
{CUSTOM_ALIVE_TEXT}

⦿ 👤 **Pemilik**: {NAME}

⦿ 🛰 **VERSION-BOT**: `𝚅{pandaversion}`

⦿ 👾 **Telethon**: `𝚅{version.__version__}`
⦿ 🎙 **Pythcalls**: `𝚅{__version__}`
⦿ 🐍 **Python**: `𝚅{python_version()}`
     
➖➖➖➖➖➖➖➖➖➖➖
╭─────────────────╮
                **Database**:

⦿ 🐘 **DB_Sql**: `{check_data_base_heal_th()}`
⦿ 🗺 **Mongo_DB**: `{Mongodb.ping()}`
⦿ 🚀 **Redis_DB**: `{redisalive()}`
⦿ 👥 **Sudo Info**: {SUDO}

╰─────────────────╯
➖➖➖➖➖➖➖➖➖➖➖
"""
