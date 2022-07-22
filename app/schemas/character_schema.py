from pydantic import BaseModel

class CharacterOut(BaseModel):
    id: int = 0 # identificador del personaje
    name: str = None # nombre del personaje
    image: str = None # url de la imagen del personaje
    appearances: int = 0 # número de apariciones en comics
