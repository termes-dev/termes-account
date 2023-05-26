from typing import Any

from renats.dispatcher import Router

from account.database.database import Database

router = Router()


@router.callback("authentication")
async def authentication(headers: dict[str, str], data: dict[str, Any], database: Database):
    return {
        "status": 403,
        "error": {
            "detail": "Access denied"
        }
    }
