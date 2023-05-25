import asyncio
import logging
import signal

from account.service.config import Config
from account.database.database import Database
from account.nats.nats import Nats
from account.service.handlers import authentication


class AccountService:
    def __init__(self, config: Config):
        self.config = config
        self.nats: Nats = Nats(
            host=config.nats.host,
            port=config.nats.port,
            base_subject=config.service.name
        )
        self.database: Database = Database(
            host=config.database.host,
            port=config.database.port,
            user=config.database.user,
            password=config.database.password,
            name=config.database.name
        )

    def _set_signal_handlers(self):
        async def signal_handler():
            await self.stop()

        loop = asyncio.get_running_loop()
        loop.add_signal_handler(signal.SIGINT, lambda: asyncio.create_task(signal_handler()))
        loop.add_signal_handler(signal.SIGTERM, lambda: asyncio.create_task(signal_handler()))

    def run(self):
        if self.config.service.logging:
            logging.basicConfig(level=logging.INFO)

        self.nats.dispatcher.include_router(authentication.router)

        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.start())
        try:
            loop.run_forever()
        finally:
            loop.close()

    async def start(self):
        logging.info("Starting service")
        self._set_signal_handlers()
        await self.nats.connect()

    async def stop(self):
        logging.info("Initiating shutdown")
        await self.nats.disconnect()
        logging.info("Service exiting")
        asyncio.get_running_loop().stop()
