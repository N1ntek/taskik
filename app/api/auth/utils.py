from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.users.crud import get_user_by_email
from app.api.users.schemas import User
from app.core.security import validate_password


async def validate_user(session: AsyncSession, email: EmailStr, password: str) -> User:
    unauth_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
    )

    user = await get_user_by_email(session, email)
    if not user:
        raise unauth_exc

    if validate_password(
        password=password,
        hashed_password=user.hashed_password,
    ):
        return user

    raise unauth_exc
