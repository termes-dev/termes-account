from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession


class Database:
    def __init__(self, url: str):
        self._engine: AsyncEngine = create_async_engine(url)
        self._sessionmaker: async_sessionmaker[AsyncSession] = async_sessionmaker(self._engine, expire_on_commit=False)

    @property
    def session(self):
        return self._sessionmaker
