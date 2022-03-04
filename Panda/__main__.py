# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# PANDA USERBOT
# ILHAM MANSIEZ
# TENTANG AKU DAN DIA


import glob
import os
import sys
from pathlib import Path

from telethon import utils

import Panda
from .versions import __version__ as botvers
from .Config import Config
from .core.logger import logging
from .core.session import PandaBot
from .helpers.utils import install_pip
from .utils import load_module
from telethon.tl.functions.channels import JoinChannelRequest

LOGS = logging.getLogger("PandaUserbot")

print(Panda.__copyright__)
print("Licensed under the terms of the " + Panda.__license__)

cmdhr = Config.COMMAND_HAND_LER
pandaub = PandaBot

async def setup_bot():
    try:
        await PandaBot.start()
        await PandaBot.start(bot_token=Config.TG_BOT_USERNAME)
        PandaBot.me = await PandaBot.get_me()
        PandaBot.uid = PandaBot.tgbot.uid = utils.get_peer_id(PandaBot.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(PandaBot.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()

PandaBot.loop.run_until_complete(setup_bot())

path = "Panda/plugins/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(shortname.replace(".py", ""))
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break
            else:
                os.remove(Path(f"Panda/plugins/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/plugins/{shortname}.py"))
            LOGS.info(f"Gagal membuka file {shortname} karena terjadi kesalahan {e}")



path = "Panda/plugins/VCPlugins/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(
                            shortname.replace(".py", ""),
                            plugin_path="Panda/plugins/VCPlugins",
                        )
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break

            else:
                os.remove(Path(f"Panda/plugins/VCPlugins/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/plugins/VCPlugins/{shortname}.py"))
            LOGS.info(f"gagal membuka file {shortname} karena terjadi kesalahan {e}")
            LOGS.info(f"{e.args}")



#AsistenBot

path = "Panda/plugins/AsistenBot/*.py"
files = glob.glob(path)
files.sort()
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(
                            shortname.replace(".py", ""),
                            plugin_path="Panda/plugins/AsistenBot",
                        )
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break

            else:
                os.remove(Path(f"Panda/plugins/AsistenBot/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"Panda/plugins/AsistenBot/{shortname}.py"))
            LOGS.info(f"gagal membuka file {shortname} karena terjadi kesalahan {e}")
            LOGS.info(f"{e.args}")

from importlib import import_module


from Panda.modules import ALL_MODULES


INVALID_PH = (
    "\nERROR: The Phone No. entered is INVALID"
    "\n Tip: Use Country Code along with number."
    "\n or check your phone number and try again !"
)


for module_name in ALL_MODULES:
    imported_module = import_module("Panda.modules." + module_name)

ON = f"""
✅ **Userbot Aktif**
•••••••••••
• **Version -** `{botvers}`
• **Ketik** `{cmdhr}alive` **untuk Mengecheck Bot apakah sudah aktif**
❗Sebaiknya Anda jangan keluar grup ini agar bot tidak mati
 ....Terimakasih....🇮🇩
❗You should not leave this group so that the bot does not die
 ....Thank You....🇺🇸
•••••••••••
"""

async def ongrup():
    try:
        if PandaBot:
            if Config.PRIVATE_GROUP_BOT_API_ID != 0:
                await PandaBot.send_message(
                    Config.PRIVATE_GROUP_BOT_API_ID,
                    ON,
                )
    except BaseException:
        pass

async def join():
    try:
        await PandaBot(JoinChannelRequest("@PandaUserbot"))
    except BaseException:
        pass

    
PandaBot.loop.run_until_complete(join())
PandaBot.loop.run_until_complete(ongrup())
print("🛠 Sedang memperoses.....")
print("Berhasil Diaktifkan!!!")
print(
    f"Mengaktifkan userbot {cmdhr}ping ⚙ BOT PANDA MENYALAH ⚙\
      \nIf you need assistance, head to https://t.me/TEAMSquadUserbotSupport"
)
print("Berhasil Mengaktifkan Userbot")

LOGS.info(f"Userbot \n⚙️ Version 2021 [ BERHASIL DIJALANKAN ]")

if len(sys.argv) not in (1, 3, 4):
    PandaBot.disconnect()
else:
    PandaBot.run_until_disconnected()
