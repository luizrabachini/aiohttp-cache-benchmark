import logging

from aiocache import caches
from aiohttp import web
from simple_settings import settings

from aiohttp_cache_benchmark.cache import AioRedisCache

logger = logging.getLogger(__name__)


class AioRedisCacheBenchmarkView(web.View):

    async def get(self):
        cache = AioRedisCache.create()
        result = await cache.run_benchmark()
        return web.json_response(data=result)
