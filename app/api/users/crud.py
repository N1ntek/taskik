from pydantic import EmailStr
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.users.schemas import UserCreate
from app.core.models import User
from app.core.security import hash_password


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    if await session.scalar(select(User).where(User.email == user_in.email)):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user with this email already exists"
        )
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hash_password(user_in.password),
    )
    session.add(user)
    await session.commit()
    return user


async def get_user_by_email(session: AsyncSession, user_email: EmailStr) -> User:
    stmt = select(User).where(User.email == user_email)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()