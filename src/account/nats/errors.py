from typing import Any


class InvalidDataError(ValueError):
    def __init__(self, message: str, data: bytes | Any):
        super().__init__(message)
        self.data = data


class HandlerAlreadyRegisteredError(Exception):
    pass
