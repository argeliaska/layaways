from pydantic import BaseSettings
from dotenv import load_dotenv
from os import getenv

class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    MARVEL_PUBLIC_KEY: str = getenv('MARVEL_PUBLIC_KEY')
    MARVEL_HASH_CODE: str = getenv('MARVEL_HASH_CODE')
    MARVEL_URL: str = getenv('MARVEL_URL')
    MARVEL_CHARACTERS_ENDPOINT: str = getenv('MARVEL_CHARACTERS_ENDPOINT')
    MARVEL_COMICS_ENDPOINT: str = getenv('MARVEL_COMICS_ENDPOINT')
    MARVEL_SECURITY_PARAMS: dict = {}

load_dotenv()
settings = Settings()
settings.MARVEL_SECURITY_PARAMS = {'ts': 1, 
                                   'apikey': settings.MARVEL_PUBLIC_KEY,
                                   'hash': settings.MARVEL_HASH_CODE}
