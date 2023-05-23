import asyncio
import logging

from account.service import AccountService


async def main():
    logging.basicConfig(level=logging.INFO)

    service = AccountService("t.account")
    await service.start()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    try:
        loop.run_forever()
    finally:
        loop.close()
