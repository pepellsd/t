import os

from functools import lru_cache
from aioredis import StrictRedis
from typing import Any, Union
from dataclasses import dataclass


@dataclass
class RedisConfig:
    host: str = os.environ.get("REDIS_HOST", default="redis")
    port: int = os.environ.get("REDIS_PORT", default="6379")
    password: str = os.environ.get("REDIS_PASSWORD", default="123")


@lru_cache
def read_redis_config():
    return RedisConfig()


class RedisClient:
    def __init__(self, config: RedisConfig):
        self.redis = StrictRedis(
            host=config.host,
            port=config.port,
            password=config.password,
            decode_responses=True,
        )

    async def set_value(self, name: str, value: str) -> Union[None, bool]:
        async with self.redis.client() as conn:
            status = await conn.set(name, value, nx=True)
        return status

    async def update_value(self, name: str, value: str) -> Union[None, bool]:
        async with self.redis.client() as conn:
            status = await conn.set(name, value, xx=True)
        return status

    async def get_value(self, search_name: str) -> Any:
        async with self.redis.client() as conn:
            val = await conn.get(search_name)
        return val


def redis_client_fabric():
    config = read_redis_config()
    return RedisClient(config=config)
