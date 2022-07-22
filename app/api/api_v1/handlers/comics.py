from fastapi import APIRouter
from fastapi import Query
from typing import Union
from app.services.search_service import SearchService

comics_router = APIRouter()

@comics_router.get('/searchComics')
def search_comics(q: Union[str, None] = Query(default=None), 
                  character: str=None,
                  comic: str=None):
    return SearchService.get(q, character, comic)
