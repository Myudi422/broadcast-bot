#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("1920905087:AAGvlh_lBs44Z_s9l7IzNyxtlo040oVKNFY", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("7120601", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("aebd45c2c14b36c2c91dec3cf5e8ee9a", "")

    # Database URI
    DB_URI = os.environ.get("mongodb+srv://akuiiki:aaaaaaac@cluster0.5oiq7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", "")

    # Group / channel username of the support chat
    SUPPORT_CHAT = os.environ.get("@otakuindonew", "")

    # List of admin user ids for special functions(Storing as an array)
    AUTH_USERS = set(int(x) for x in os.environ.get("784985038", "").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
