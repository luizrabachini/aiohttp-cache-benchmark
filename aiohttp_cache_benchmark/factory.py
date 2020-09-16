from aiohttp import web
from aiohttp_swagger import setup_swagger
from simple_settings import settings

from .cache import AioRedisCache
from .benchmark.routes import register_routes as register_benchmark_routes
from .healthcheck.routes import register_routes as register_heathcheck_routes
from .contrib.middlewares import (
    exception_handler_middleware,
    version_middleware
)

CACHES = {
    'AioRedisCache': AioRedisCache
}


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())

    app.on_startup.append(start_plugins)
    app.on_cleanup.append(stop_plugins)

    setup_swagger(
        app,
        swagger_url='/docs',
        swagger_from_file="docs/swagger.yaml"
    )

    register_routes(app)

    return app


def register_routes(app):
    register_heathcheck_routes(app)
    register_benchmark_routes(app)


def get_middlewares():
    return [
        version_middleware,
        exception_handler_middleware
    ]

async def start_plugins(app):
    if settings.PRELOAD_CACHE in CACHES:
        cache_class = CACHES[settings.PRELOAD_CACHE]
        cache = cache_class.create()
        await cache.initialize()

async def stop_plugins(app):
    for cache_class in CACHES:
        cache = cache_class.create()
        await cache.finalize()
