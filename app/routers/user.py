from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


router = APIRouter(tags=["user"])


@router.get("/me")
def check_data(request: Request):
    print("_____________________________________________________________________________________________")
    print(request.__dict__)
    print("_____________________________________________________________________________________________")
    print(request.headers)
    print("_____________________________________________________________________________________________")
    return JSONResponse(content={"message":"logined"})


@router.get("/admin")
async def fffupdate_data(request: Request):
    print("_____________________________________________________________________________________________")
    print(request.__dict__)
    print("_____________________________________________________________________________________________")
    print(request.headers)
    print("_____________________________________________________________________________________________")
    print(await request.body())
    print("_____________________________________________________________________________________________")
    return JSONResponse(content={"message":"salam"})
