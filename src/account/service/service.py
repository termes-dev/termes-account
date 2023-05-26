import logging

from renats.client import ReNats
from renats.dispatcher import Dispatcher

from account.database.database import Database
from account.service import handlers
from account.service.config import Config


class AccountService:
    def __init__(self, config: Config):
        self.config = config
        self.database: Database = Database(config.database.url)
        self.nats = ReNats([config.nats.url])
        self.dispatcher = Dispatcher(config.service.name, config=config, database=self.database)
        self.dispatcher.include_router(handlers.router)

    async def run(self):
        if self.config.service.logging:
            logging.basicConfig(level=logging.INFO)

        await self.nats.polling(self.dispatcher)
