from abc import ABC
from typing import Any, Union

from .client import RedisConfig


class AbstractRedisClient(ABC):
    def __init__(self):
        self.config: RedisConfig

    async def set_value(self, name: str, value: str) -> Union[None, bool]:
        ...

    async def update_value(self, name: str, value: str) -> Union[None, bool]:
        ...

    async def get_value(self, search_name: str) -> Any:
        ...
