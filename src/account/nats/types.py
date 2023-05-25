from typing import Any

from pydantic import BaseModel


class Request(BaseModel):
    headers: dict[str, str]
    data: dict[str, Any]
