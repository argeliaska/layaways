from fastapi import Body, Request
from fastapi.encoders import jsonable_encoder
from app.schemas.user_schema import UserIn, UserOut
from pydantic import EmailStr
from app.models.user_model import User
from app.core.security import hash_password

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
    async def find_by_email(email: EmailStr):
        user = await User.find_one(User.email == email)
        return user