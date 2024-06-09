from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.users.crud import get_user_by_email
from app.api.users.schemas import User

from app.core.database import db
from app.core.security import decode_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_token_payload(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = decode_jwt(token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}",
        )
    return payload


async def get_current_user(
        session: AsyncSession = Depends(db.session_dependency),
        payload: dict = Depends(get_token_payload),
) -> User:
    user_id: str | None = payload.get("id")
    user = await get_user_by_email(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalid",
        )
    return user
