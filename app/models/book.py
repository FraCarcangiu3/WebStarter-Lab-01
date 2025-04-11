from pydantic import BaseModel, Field # BaseModel serve per creare modelli di dati
from typing import Annotated # Annotated serve per aggiungere annotazioni ai tipi di dati

class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Annotated[int|None, Field(ge=1, le=5)] = None




