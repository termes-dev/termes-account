import logging
from typing import Callable, Awaitable

import msgpack
from msgpack import OutOfData
from nats.aio.msg import Msg
from pydantic import BaseModel

from account.nats.errors import InvalidDataError
from account.nats.router import Router
from account.nats.types import Request


class Dispatcher(Router):
    def __init__(self, base_subject: str):
        super().__init__()
        self.base_subject: str = base_subject

    async def handle(self, msg: Msg):
        handler = self.handlers.get(msg.subject)
        if handler is None:
            logging.info(f"Message from '{msg.subject}' not handled")
            return

        try:
            data = msgpack.unpackb(msg.data)
        except ValueError:
            raise InvalidDataError("Invalid request data (must be a valid dictionary object)", msg.data)

        if not isinstance(data, dict):
            raise InvalidDataError("Request data object is not a dictionary object", msg.data)

        request = Request(
            headers=msg.headers,
            data=data
        )

        response = await handler(request)

        if isinstance(response, BaseModel):
            response = response.dict()
        elif not isinstance(response, dict):
            raise InvalidDataError("Response data object is not a dictionary object", response)

        try:
            response_data = msgpack.packb(response)
        except (ValueError, OutOfData):
            raise InvalidDataError("Invalid response data", response)

        await msg.respond(response_data)

        logging.info(f"Message from {msg.subject} handled")

    @property
    def subscription_callback(self) -> Callable[[Msg], Awaitable[None]]:
        async def handler(msg: Msg):
            await self.handle(msg)

        return handler
