import aioredis
import logging
from simple_settings import settings

from .base import BaseCache
from .mixins import SingletonCreateMixin

logger = logging.getLogger(__name__)


class AioRedisCache(BaseCache, SingletonCreateMixin):

    _redis = None

    async def _initialize(self):
        if self._redis is None:
            self._redis = await aioredis.create_redis_pool(
                f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}',
                minsize=settings.REDIS_MIN_POOL_SIZE,
                maxsize=settings.REDIS_MAX_POOL_SIZE
            )
            logger.info('AioRedisCache connection initialized')

    async def _finalize(self):
        if self._redis is None:
            logger.info('Cache not initialize to finalize')
            return

        self._redis.close()
        await self._redis.wait_closed()

    async def _get_redis(self):
        if self._redis is None:
            await self.initialize()
        return self._redis

    async def _get(self, key):
        redis = await self._get_redis()
        result = await redis.get(key=key)
        return result

    async def _set(self, key, value, expire=10):
        redis = await self._get_redis()
        result = await redis.set(key=key, value=value, expire=expire)
        return result
