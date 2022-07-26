from fastapi import APIRouter
from app.api.api_v1.handlers import comics, user
from app.api.auth.jwt import auth_router

router = APIRouter()

router.include_router(comics.comics_router, prefix='/comics', tags=['comics'])
router.include_router(user.user_router, prefix='/users', tags=['users'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])

