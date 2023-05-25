import logging
from typing import Callable, Any, Awaitable

from pydantic import BaseModel

from account.nats.errors import HandlerAlreadyRegisteredError
from account.nats.types import Request

HandlerType = Callable[[Request], Awaitable[BaseModel | dict[str, Any]]]


class Router:
    def __init__(self):
        self.handlers: dict[str, HandlerType] = {}

    def include_router(self, router: "Router"):
        self.handlers.update(router.handlers)

    def message_handler(self, subject: str):
        def wrapper(handler: HandlerType):
            self.register_message_handler(subject, handler)
            return handler
        return wrapper

    def register_message_handler(self, subject: str, handler: HandlerType):
        if subject in self.handlers:
            raise HandlerAlreadyRegisteredError(f"Message handler for {subject} is already registered")
        self.handlers[subject] = handler
        logging.info(f"Registered message handler for {subject}")