#imports

import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation
from .user import User

from pyrogram import Client, __version__

#import ENV

from FilterBot.config import API_ID, API_HASH, BOT_TOKEN, DB_URI, USER_SESSION


# Logging Thing

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "filterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
