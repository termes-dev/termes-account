import nats
from nats.aio.client import Client


class AccountService:
    def __init__(self, servers: list[str]):
        self.servers: list[str] = servers
        self.handlers: list[MessageListener]
        self.nats_client: Client | None = None

    async def connect(self):
        self.nats_client = await nats.connect(self.servers)

    async def start(self):
        pass  # TODO: start service

    async def stop(self):
        pass  # TODO: stop service
