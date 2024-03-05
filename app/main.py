from fastapi import FastAPI

from app.routers import user


def application_factory():
    application = FastAPI(debug=True, docs_url='/docs')
    application.include_router(user.router)
    return application


app = application_factory()
