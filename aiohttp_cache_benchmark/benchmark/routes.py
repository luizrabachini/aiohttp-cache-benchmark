from .views import AioRedisCacheBenchmarkView


def register_routes(app):
    app.router.add_route(
        '*',
        '/benchmark/aioredis/',
        AioRedisCacheBenchmarkView
    )
