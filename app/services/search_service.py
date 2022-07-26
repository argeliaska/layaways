from app.utils import get_response
from app.core.config import settings
from .character_service import CharacterService
from .comic_service import ComicService

class SearchService():
    @staticmethod
    def get(q:str=None, character:str=None, comic:str=None):
        results = []
        
        if q:
            characters_results = CharacterService.search(q)
            comics_results = ComicService.search(q)

            results.extend(characters_results)
            results.extend(comics_results)
        elif character:
            results = CharacterService.find_by_name(character)
        elif comic:
            results = ComicService.find_by_title(comic)
        else:
            results = CharacterService.list()

        return results
        
