from fastapi import FastAPI

# import controllers here
from src.controllers.AuthController import router as auth_router

#


def register_routes(app: FastAPI):
    # register controllers here
    app.include_router(prefix="/api/v1", tags=["auth"], router=auth_router)
