from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.auth.dependencies import CurrentUser, TokenPayloadDep
from app.api.auth.utils import validate_user
from app.core.database import SessionDep
from app.core.security import encode_jwt, TokenInfo

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenInfo)
async def login(
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = await validate_user(
        session=session, email=form_data.username, password=form_data.password
    )
    payload = {"sub": str(user.id), "username": user.username, "email": user.email}
    token = encode_jwt(payload)
    return TokenInfo(access_token=token, token_type="Bearer")


@router.get("/users/me/")
async def auth_user_check_self_info(
    current_user: CurrentUser, token_payload: TokenPayloadDep
) -> dict:
    return {
        "username": current_user.username,
        "email": current_user.email,
        "login_at": token_payload.get("iat"),
    }
