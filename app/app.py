from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.api.api_v1.router import router
from app.core.config import settings
from app.models.user_model import User
import logging

app = FastAPI(
    title="Comic's layaways",
    description="API Rest for techinal exam"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('ENTRANDO')
@app.on_event("startup")
async def startup_db_client():
    print('startup_db_client', settings.MONGO_URI)

    db_client = AsyncIOMotorClient(settings.MONGO_URI).layaways

    await init_beanie(
        database=db_client,
        document_models=[
            User,
        ]
    )


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail':exc.errors()}),
    )

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse('/docs')

@app.get('/health-check')
def health_check():
    return {"message": "it's working"}

app.include_router(router, prefix=settings.API_V1)