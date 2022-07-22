from fastapi import APIRouter
from app.api.api_v1.handlers import comics

router = APIRouter()

router.include_router(comics.comics_router, prefix='/comics', tags=['comics'])
