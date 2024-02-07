from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.services.redis.abc import AbstractRedisClient


router = APIRouter(tags=["user"])


class Data(BaseModel):
    phone: str
    address: str

# можно сделать куда лучше, используя встроенные валидаторы в пидантик, свои типы
# скорее всего в реальности, это будет value object, со своей логикой
# и модели пидантака будут использоваться только для сереализации\десериализации и будут мапяться


@router.get("/check_data")
async def check_data(
        phone: str = Query(),
        redis_client: AbstractRedisClient = Depends()
):
    address = await redis_client.get_value(phone)
    if address is None:
        return JSONResponse(content={"message": "телефон не был найден"}, status_code=404)
    return JSONResponse(content={"address": address}, status_code=200)


@router.put("/write_data")
async def update_data(
        data: Data,
        redis_client: AbstractRedisClient = Depends()
):
    status = await redis_client.update_value(data.phone, data.address)
    if status is None:
        return JSONResponse(content={"message": "изменения не приняты, телефона с таким номером нет"}, status_code=400)
    return JSONResponse(content={"message": "успешно изменено"}, status_code=202)


@router.post("/write_data")
async def create_data(
        data: Data,
        redis_client: AbstractRedisClient = Depends()
):
    status = await redis_client.set_value(data.phone, data.address)
    if status is None:
        return JSONResponse(content={"message": "телефон с таким номером уже существует"}, status_code=400)
    return JSONResponse(content={"message": "успешно создано"}, status_code=201)

