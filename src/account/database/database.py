from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession


class Database:
    def __init__(self, host: str, port: int, user: str, password: str, name: str):
        self._engine: AsyncEngine = create_async_engine(
            f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"
        )
        self._sessionmaker: async_sessionmaker[AsyncSession] = async_sessionmaker(self._engine, expire_on_commit=False)

    @property
    def session(self):
        return self._sessionmaker
