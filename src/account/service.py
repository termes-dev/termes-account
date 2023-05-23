import asyncio
import logging
import signal

import nats
from nats.aio.client import Client
from nats.aio.msg import Msg
from nats.aio.subscription import Subscription


class AccountService:
    def __init__(self, name: str):
        self.name: str = name
        self.nats_client: Client | None = None
        self.subscription: Subscription | None = None

    @staticmethod
    async def _message_handler(msg: Msg):  # For test only
        logging.info(f"Received msg from {msg.subject}: {msg.data.decode()}")
        await msg.respond(f"Hello from service! Echo: {msg.data.decode()}".encode())

    async def connect(self, servers: list[str]):
        logging.info("Connecting to NATS servers")
        self.nats_client = await nats.connect(servers)

    async def start(self):
        if self.nats_client is None or self.nats_client.is_closed:
            await self.connect(["nats://127.0.0.1:4222"])  # Temporary hardcoded nats address :)
        logging.info("Starting service")
        self.subscription = await self.nats_client.subscribe(f"{self.name}.*", cb=AccountService._message_handler)
        logging.info("Configuring signal handlers (SIGINT, SIGTERM)")

        async def signal_handler():
            await self.stop()
            asyncio.get_running_loop().stop()

        loop = asyncio.get_running_loop()
        loop.add_signal_handler(signal.SIGINT, lambda: asyncio.create_task(signal_handler()))
        loop.add_signal_handler(signal.SIGTERM, lambda: asyncio.create_task(signal_handler()))

    async def stop(self):
        logging.info("Initiating shutdown")
        if self.subscription is None:
            logging.warning("Service is not running!")
        else:
            await self.subscription.unsubscribe()
        await self.nats_client.drain()
        logging.info("Service exiting")
