from fastapi import APIRouter
from starlette import status

from app.api.users import crud
from app.api.users.schemas import User, UserCreate
from app.core.database import SessionDep

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: SessionDep):
    return await crud.create_user(session, user)
