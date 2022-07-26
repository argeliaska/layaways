from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.exceptions import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.api.api_v1.router import router
from app.core.config import settings
from app.models.user_model import User
import logging

app = FastAPI(
    title="Comic's layaways",
    description="API Rest for techinal exam",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail':exc.errors()}),
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({'detail':exc}),
    )

@app.on_event("startup")
async def startup_db_client():
    try:
        db_client = AsyncIOMotorClient(settings.MONGO_URI, serverSelectionTimeoutMS=10).layaways

        await init_beanie(
                database=db_client,
                document_models=[
                    User,
                ]
            )
        
    except Exception as exc:
        logging.error(f'Unable to connect to database {settings.MONGO_URI}')
        
@app.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse('/docs')

@app.get('/health-check')
def health_check():
    return {"message": "it's working"}

app.include_router(router, prefix=settings.API_V1)