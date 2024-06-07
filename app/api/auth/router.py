from uuid import UUID

from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from app.api.users.schemas import UserInDb
from app.core.security import hash_password, encode_jwt, decode_jwt, validate_password, TokenInfo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

john = UserInDb(
    id=UUID("ec963063-9d53-41f7-bcdc-c86e6c82bcbd"),
    username="john",
    email="test@email.com",
    password=hash_password("qwerty"),
    active=True,
)

users_db: dict[str, UserInDb] = {
    john.username: john,
}

router = APIRouter(prefix="/auth", tags=["auth"])


def validate_auth_user(
        username: str = Form(),
        password: str = Form(),
):
    unauth_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
    )



    if not (user := users_db.get(username)):
        raise unauth_exc

    if validate_password(
        password=password,
        hashed_password=user.password,
    ):
        return user

    raise unauth_exc


@router.post('/login', response_model=TokenInfo)
async def login(user: UserInDb = Depends(validate_auth_user)):
    payload = {"sub": user.id, "username": user.username, "email": user.email}
    token = encode_jwt(payload)
    return TokenInfo(access_token=token, token_type="Bearer")


def get_token_payload(token:  str = Depends(oauth2_scheme)) -> UserInDb:
    try:
        payload = decode_jwt(token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error {e}",
        )
    print(payload)
    return payload


def get_current_user(
        payload: dict = Depends(get_token_payload),
) -> UserInDb:
    username: str | None = payload.get("username")
    if not (user := users_db.get(username)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token invalid",
        )
    return user


@router.get('/users/me/')
async def auth_user_check_self_info(
        user: UserInDb = Depends(get_current_user),
):
    return {
        "username": user.username,
        "email": user.email,
    }
