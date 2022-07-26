from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class User(Document):
    name: str = Field(..., max_length=50)
    email: Indexed(EmailStr, unique=True)
    age: int = Field(ge=18)
    password: str = Field(...)
    
    @property
    def create(self) -> datetime:
        return self.id.generation_time

    class Collection:
        name = 'users'
