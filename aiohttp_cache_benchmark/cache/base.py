import json
from uuid import uuid4

from abc import abstractmethod


class BaseCache:

    @abstractmethod
    async def _initialize(self):
        pass

    @abstractmethod
    async def _finalize(self):
        pass

    @abstractmethod
    async def _get(self, key):
        pass

    @abstractmethod
    async def _set(self, key, value, expire=10):
        pass

    async def initialize(self):
        await self._initialize()

    async def finalize(self):
        await self._finalize()

    async def get(self, key):
        result = await self._get(key=key)
        return result

    async def set(self, key, value, expire=1):
        result = await self._set(key=key, value=value, expire=expire)
        return result

    async def run_benchmark(self):
        data = {
            'attr1': 'data',
            'attr2': 'data',
            'attr3': 'data',
            'attr4': 'data',
            'attr5': 'data',
            'attr6': 'data',
            'attr7': 'data',
            'attr8': 'data',
        }

        key_one = 'key_one'
        content_one = await self.get(key=key_one)
        if not content_one:
            content_one = json.dumps(data)
            await self.set(key=key_one, value=content_one, expire=None)

        json.loads(content_one)

        key_two = uuid4().hex
        content_two = await self.get(key=key_two)
        if not content_two:
            content_two = json.dumps(data)
            await self.set(key=key_two, value=content_two, expire=None)

        json.loads(content_two)

        return data
