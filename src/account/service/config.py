from pydantic import BaseModel


class ServiceConfig(BaseModel):
    name: str
    logging: bool


class NatsConfig(BaseModel):
    host: str
    port: int


class DatabaseConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    name: str


class Config(BaseModel):
    service: ServiceConfig
    nats: NatsConfig
    database: DatabaseConfig
