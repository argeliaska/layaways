from app.utils import get_response
from app.core.config import settings
from app.schemas.comic_schema import ComicOut

class ComicService():
    @staticmethod
    def search(q:str=None):
        results = []
        
        url = f'{settings.MARVEL_URL}{settings.MARVEL_COMICS_ENDPOINT}'
        params = dict.copy(settings.MARVEL_SECURITY_PARAMS)
        params.update({'titleStartsWith': q})
        
        resp = get_response(url, params)

        if resp:
            resp_results = resp['data']['results']

            for comic_resp in resp_results:
                comic = ComicOut()
                comic.id = comic_resp.get('id')
                comic.title = comic_resp.get('title')
                image = comic_resp.get('thumbnail').get('path')
                image += '.' + comic_resp.get('thumbnail').get('extension')
                comic.image = image

                dates = comic_resp.get('dates')
                for dte in dates:
                    print(dte['type'])
                    if dte['type'] == 'onsaleDate':
                        comic.onSaleDate = dte['date']
                
                results.append(comic)
        return results

    @staticmethod
    def find_by_title(title:str=None):
        results = []
        
        url = f'{settings.MARVEL_URL}{settings.MARVEL_COMICS_ENDPOINT}'
        params = dict.copy(settings.MARVEL_SECURITY_PARAMS)
        params.update({'title': title})
        
        resp = get_response(url, params)

        if resp:
            resp_results = resp['data']['results']

            for comic_resp in resp_results:
                comic = ComicOut()
                comic.id = comic_resp.get('id')
                comic.title = comic_resp.get('title')
                image = comic_resp.get('thumbnail').get('path')
                image += '.' + comic_resp.get('thumbnail').get('extension')
                comic.image = image

                dates = comic_resp.get('dates')
                for dte in dates:
                    if dte['type'] == 'onsaleDate':
                        comic.onSaleDate = dte['date']
                
                results.append(comic)
        return results