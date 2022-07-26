from fastapi import Body, Request
from fastapi.encoders import jsonable_encoder
from app.schemas.user_schema import UserIn, UserOut
from bson.objectid import ObjectId
from pydantic import EmailStr
from app.models.user_model import User
from app.core.security import verify_password, hash_password

class UserService:
    
    @staticmethod
    async def create_user(user: UserIn):
        new_user = User(
            name=user.name,
            password=hash_password(user.password), 
            email=user.email,
            age=user.age
        )  

        await new_user.save()
        return new_user

    @staticmethod
    async def authenticate(email: str, password: str):
        user = await UserService.find_by_email(email=email)

        if not user:
            return None

        if not verify_password(password=password, hashed_pass=user.password):
            return None

        return user

    @staticmethod
    async def find_by_email(email: EmailStr):
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def find_by_id(id: str):
        user = await User.find_one(User.id == ObjectId(id))
        return user