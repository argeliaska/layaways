from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    MARVEL_PUBLIC_KEY: str = config('MARVEL_PUBLIC_KEY')
    MARVEL_HASH_CODE: str = config('MARVEL_HASH_CODE')
    MARVEL_URL: str = config('MARVEL_URL')
    MONGO_URI: str = config("MONGO_URI", cast=str)
    MONGO_DB_NAME: str = config('MONGO_DB_NAME')
    MARVEL_SECURITY_PARAMS: dict = {}
    MARVEL_CHARACTERS_ENDPOINT: str = config('MARVEL_CHARACTERS_ENDPOINT')
    MARVEL_COMICS_ENDPOINT: str = config('MARVEL_COMICS_ENDPOINT')
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []    

settings = Settings()
settings.MARVEL_SECURITY_PARAMS = {'ts': 1, 
                                   'apikey': settings.MARVEL_PUBLIC_KEY,
                                   'hash': settings.MARVEL_HASH_CODE}
