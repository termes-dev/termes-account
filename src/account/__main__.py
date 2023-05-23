import asyncio
import logging
import os

from account.service import AccountService


async def main():
    logging.basicConfig(level=logging.INFO)

    nats_servers = os.getenv("NATS_SERVERS").split(",")
    if nats_servers is None or len(nats_servers) == 0:
        raise RuntimeError("NATS_SERVERS is not defined")

    service = AccountService(nats_servers)
    await service.start()


if __name__ == "__main__":
    asyncio.run(main())
