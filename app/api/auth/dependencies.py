from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from starlette import status

from app.api.users.crud import get_user_by_id
from app.api.users.schemas import User

from app.core.database import SessionDep
from app.core.security import decode_jwt

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_token_payload(token: TokenDep) -> dict:
    try:
        payload = decode_jwt(token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}",
        )
    return payload


TokenPayloadDep = Annotated[dict, Depends(get_token_payload)]


async def get_current_user(
    session: SessionDep,
    payload: TokenPayloadDep,
) -> User:
    user_id: str | None = payload.get("sub")
    user = await get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalid",
        )
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
