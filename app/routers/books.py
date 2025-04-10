# Sto creando un file per gli endpoint delle API per la gestione dei libri che partona da /books

from fastapi import APIRouter
from models.book import Book
from data.books import books


#questo è il router per la gestione delle rotte relative ai libri ovvero mi permette di definire le rotte
router = APIRouter(prefix="/books") #questo routers lavora sotto il prefisso /books


@router.get("/")
def get_all_books() -> list[Book]: #list[book] è il dato che
    """Restituisce la lista di tutti i libri disponibili"""
    return list(books.values()) #Mi restituisce i valori del dizionario books