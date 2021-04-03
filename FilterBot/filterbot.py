from pyrogram import Client, __version__

from .config import API_HASH, API_ID, BOT_TOKEN 
from . import LOGGER

from .user import User

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
        self.LOGGER(__name__).info("FilterBot stopped. Bye.")
