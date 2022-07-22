from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.api_v1.router import router
from app.core.config import settings

app = FastAPI(
    title="Comic's layaways",
)

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse('/docs')

@app.get('/health-check')
def health_check():
    return {"message": "it's working"}

app.include_router(router, prefix=settings.API_V1)