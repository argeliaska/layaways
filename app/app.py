from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Comic's layaways",
)

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse('/docs')

@app.get('/health-check')
def health_check():
    return {"message": "it's working"}