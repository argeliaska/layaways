from passlib.context import CryptContext
from jose import jwt
from datetime import datetime
from datetime import timedelta
from app.core.config import settings
from typing import Union, Any

password_context = CryptContext(schemes=['bcrypt'])

def create_access_token(subject: Union[str, Any], expires: int = None) -> str:
    if expires is not None:
        expires = datetime.utcnow() + expires
    else:
        # first access
        expires = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    token_data = {'exp': expires, 'sub': str(subject)}
    encoded_jwt = jwt.encode(token_data, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt 

def create_refresh_token(subject: Union[str, Any], expires: int = None) -> str:
    if expires is not None:
        expires = datetime.utcnow() + expires
    else:
        # first access token created
        expires = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    token_data = {'exp': expires, 'sub': str(subject)}
    encoded_jwt = jwt.encode(token_data, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt 

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)