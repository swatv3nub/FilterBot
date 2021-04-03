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

#main app

class app(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "filterbot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "FilterBot/plugins"
            },
            workers=4,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(markdown)
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
