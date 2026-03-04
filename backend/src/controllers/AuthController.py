from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.models.AuthModel import LoginRequest, LoginResponse
from src.services.AuthService import AuthService
from src.database.core import get_db
from src.rate_limiting import limiter

router = APIRouter(prefix="/auth")


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=LoginResponse,
)
@limiter.limit("5/minute")
async def login_api(
    request: Request,
    payload: LoginRequest,
    db: Session = Depends(get_db),
):
    user = await AuthService.login(
        db=db,
        email=payload.email,
        password=payload.password,
    )

    return LoginResponse(access_token=user)


@router.post(
    "/seed",
    status_code=status.HTTP_200_OK,
)
@limiter.limit("5/minute")
async def seed_db(
    request: Request,
    db: Session = Depends(get_db),
):
    result = await AuthService.seed(
        db=db,
    )

    return {"message": "Seeded successfully"}
