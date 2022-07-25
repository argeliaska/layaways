from fastapi import APIRouter, Body, Request
from fastapi import status, HTTPException
from app.schemas.user_schema import UserIn, UserOut, user_out
from app.services.user_service import UserService
from pydantic import EmailStr
import pymongo

user_router = APIRouter()

@user_router.post("/create", summary="Creates a new user", response_model=UserOut)
async def create_user(data: UserIn):
    try:
        user_created = await UserService.create_user(data)
        return user_out(user_created)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this email already exists'
        )

@user_router.get('/{email}', summary="Get the user by email", response_model=UserOut)
async def get(email: EmailStr):
    user = await UserService.find_by_email(email)
    return user_out(user)