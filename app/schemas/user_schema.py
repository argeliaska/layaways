from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime
from app.models.user_model import User

def user_out(user: User) -> dict:
    return {
        'id': str(user.id),
        'name': user.name,
        'email': user.email,
        'age': user.age
    }

def user_me_out(user: User, access_token: str) -> dict:
    return {
        'id': str(user.id),
        'name': user.name,
        'email': user.email,
        'age': user.age,
        'token': access_token
    }

class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int

class UserMeOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    token: str

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int