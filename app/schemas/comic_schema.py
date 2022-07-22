from pydantic import BaseModel
from datetime import datetime

class ComicOut(BaseModel):
    id: int = 0 # identificador del cómic
    title: str = None # nombre del cómic
    image: str = None # imagen del cómic
    onSaleDate: datetime = None # fecha de lanzamiento