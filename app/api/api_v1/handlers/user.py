from fastapi import APIRouter, Body, Request, Depends, Header
from fastapi import status, HTTPException
from app.schemas.user_schema import UserIn, UserOut, UserMeOut, user_out, user_me_out
from app.services.user_service import UserService
from app.api.api_v1.deps import get_current_user
from app.models.user_model import User
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

@user_router.get('/me', summary="Get the current user", response_model=UserMeOut)
async def me(req: Request, current_user: User = Depends(get_current_user)):
    token = req.headers["Authorization"]
    token_str = token[len('Bearer '):]
    return user_me_out(current_user, token_str)

@user_router.get('/{email}', summary="Get the user by email", response_model=UserOut)
async def get(email: EmailStr):
    user = await UserService.find_by_email(email)
    if user:
        return user_out(user)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with email {email} doesn\'t exists',
        headers={"WWW-Authenticate":"Bearer"},
    )