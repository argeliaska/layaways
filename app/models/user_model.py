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
    
    def __repr__(self) -> str:
        return f'<User {self.email}>'

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    class Collection:
        name = 'users'
