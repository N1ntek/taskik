from uuid import UUID

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    active: bool


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserInDb(User):
    password: bytes
