from pydantic import BaseModel


class ServiceConfig(BaseModel):
    name: str
    logging: bool


class NatsConfig(BaseModel):
    host: str
    port: int

    @property
    def url(self):
        return f"nats://{self.host}:{self.port}"


class DatabaseConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    name: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Config(BaseModel):
    service: ServiceConfig
    nats: NatsConfig
    database: DatabaseConfig
