from pyrogram import Client, __version__

from .config import API_HASH, API_ID, LOGGER, USER_SESSION


class User(Client):
    def __init__(self):
        super().__init__(
            USER_SESSION,
            api_hash=API_HASH,
            api_id=API_ID,
            workers=4
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
