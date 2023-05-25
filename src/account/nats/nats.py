import nats
from nats.aio.client import Client

from account.nats.dispatcher import Dispatcher


class Nats:
    def __init__(self, host: str, port: int, base_subject: str):
        self._host: str = host
        self._port: int = port
        self.dispatcher: Dispatcher = Dispatcher(base_subject)
        self.client: Client | None = None

    async def connect(self):
        self.client = await nats.connect([f"nats://{self._host}:{self._port}"])

    async def disconnect(self):
        await self.client.drain()
