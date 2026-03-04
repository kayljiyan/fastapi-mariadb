import hashlib
import os
import binascii

from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status

from src.schemas.AuthSchema import User

from passlib.context import CryptContext


def hash_password(password: str) -> str:
    hashed = hashlib.sha256(password.encode())
    return hashed.hexdigest()


def verify_password(password: str, stored_hash: str) -> bool:
    input_hash = hash_password(password)
    return input_hash == stored_hash


class AuthService:
    @staticmethod
    async def login(
        db: Session,
        email: str,
        password: str,
    ) -> str:

        result = db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        return user.email

    @staticmethod
    async def seed(
        db: Session,
    ):
        ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
        ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

        # Check if admin already exists
        result = db.execute(select(User).where(User.email == ADMIN_EMAIL))
        existing_admin = result.scalar_one_or_none()

        if existing_admin:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Admin already exists",
            )

        # Create admin user
        admin_user = User(
            email=ADMIN_EMAIL,
            password_hash=hash_password(ADMIN_PASSWORD),
        )

        db.add(admin_user)
        db.commit()
