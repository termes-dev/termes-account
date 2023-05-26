from renats.dispatcher import Router

from account.service.handlers import authentication

router = Router()
router.include_router(authentication.router)
