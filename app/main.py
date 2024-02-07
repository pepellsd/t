from fastapi import FastAPI

from app.services.redis.abc import AbstractRedisClient
from app.services.redis.client import redis_client_fabric
from app.routers import user


def application_factory():
    application = FastAPI(debug=True, docs_url='/docs')
    # в реальности все настройки будут браться из переменных среды(.env) или любых конфигурационных файлов
    # так же и для клиента редиса, где они типо беруться, но указаны дефолты
    # в докере можно использовать docker secrets или так же просто тянуть с .env
    application.dependency_overrides[AbstractRedisClient] = redis_client_fabric
    # опять же в реальности лучше стоило бы использовать пулл соеднинений, нежели отдельные

    application.include_router(user.router)

    return application


app = application_factory()
