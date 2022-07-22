from app.utils import get_response
from app.core.config import settings
from app.schemas.character_schema import CharacterOut
from pydantic import HttpUrl

class CharacterService():
    @staticmethod
    def search(q:str=None):
        results = []
        
        url = f'{settings.MARVEL_URL}{settings.MARVEL_CHARACTERS_ENDPOINT}'
        params = dict.copy(settings.MARVEL_SECURITY_PARAMS)
        params.update({'nameStartsWith': q})
        
        resp = get_response(url, params)

        if resp:
            resp_results = resp['data']['results']

            for character_resp in resp_results:
                character = CharacterOut()
                character.id = character_resp.get('id')
                character.name = character_resp.get('name')
                image = character_resp.get('thumbnail').get('path')
                image += '.' + character_resp.get('thumbnail').get('extension')
                character.image = image
                character.appearances = character_resp.get('comics').get('available')
                results.append(character)

        return results

    @staticmethod
    def list():
        results = []
        
        url = f'{settings.MARVEL_URL}{settings.MARVEL_CHARACTERS_ENDPOINT}'
        params = dict.copy(settings.MARVEL_SECURITY_PARAMS)
        
        resp = get_response(url, params)

        if resp:
            resp_results = resp['data']['results']
            
            characters_names = []
            characters = []

            for character_resp in resp_results:
                character = CharacterOut()
                character.id = character_resp.get('id')
                character.name = character_resp.get('name')
                characters_names.append(character.name)
                image = character_resp.get('thumbnail').get('path')
                image += '.' + character_resp.get('thumbnail').get('extension')
                character.image = image
                character.appearances = character_resp.get('comics').get('available')
                characters.append(character)
        
            characters_names = sorted(characters_names)

            for item in characters:
                for name in characters_names:
                    if item.name == name:
                        results.append(item)
                        characters_names.remove(name)

        return results

    @staticmethod
    def find_by_name(name:str=None):
        results = []
        
        url = f'{settings.MARVEL_URL}{settings.MARVEL_CHARACTERS_ENDPOINT}'
        params = dict.copy(settings.MARVEL_SECURITY_PARAMS)
        params.update({'name': name})
        
        resp = get_response(url, params)

        if resp:
            resp_results = resp['data']['results']

            for character_resp in resp_results:
                character = CharacterOut()
                character.id = character_resp.get('id')
                character.name = character_resp.get('name')
                image = character_resp.get('thumbnail').get('path')
                image += '.' + character_resp.get('thumbnail').get('extension')
                character.image = image
                character.appearances = character_resp.get('comics').get('available')
                results.append(character)

        return results

    