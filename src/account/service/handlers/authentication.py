from account.nats.router import Router
from account.nats.types import Request

router = Router()


@router.message_handler("authentication")
async def authentication(request: Request):
    return request.data
