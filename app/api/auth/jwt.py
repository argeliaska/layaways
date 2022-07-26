from fastapi import APIRouter, Depends, Body
from fastapi import HTTPException, status
from fastapi.exceptions import ValidationError
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token, create_refresh_token
from app.services.user_service import UserService
from app.models.user_model import User
from app.schemas.auth_schema import TokenSchema, TokenPayload, RefreshTokenSchema
from app.core.config import settings
from datetime import datetime
from jose import jwt

auth_router = APIRouter()

@auth_router.post('/login',
                  summary='Creates tokens for the user',
                  response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.authenticate(email=form_data.username, 
                                          password=form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Incorrect email or password")

    return {
        "access_token": create_access_token(user.id), 
        "refresh_token": create_refresh_token(user.id), 
    }

@auth_router.post('/refresh', 
                    summary="Renews the tokens by the refresh token",
                    response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
             raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate":"Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials",
            headers={"WWW-Authenticate":"Bearer"},
        )
    
    user = await UserService.find_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find the user"
        )

    return {
        'access_token': create_access_token(user.id),
        'refresh_token': create_refresh_token(user.id)
    }