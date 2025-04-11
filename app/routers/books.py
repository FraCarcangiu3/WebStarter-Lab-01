# Sto creando un file per gli endpoint delle API per la gestione dei libri che partona da /books
from fastapi.exceptions import RequestValidationError
from requests import RequestException

#importo le librerie necessarie per la creazione dell'APIk = books[id]
from models.book import Book
from models.review import Review
from data.books import books

#importo le librerie necessarie per la creazione dell'API
from fastapi import APIRouter, HTTPException, Path
from pydantic import ValidationError # ValidationError serve per gestire gli errori di validazione dei dati
from typing import Annotated # Annotated serve per aggiungere annotazioni ai tipi di dati

from models.review import Review

#questo è il router per la gestione delle rotte relative ai libri ovvero mi permette di definire le rotte
router = APIRouter(prefix="/books") #questo routers lavora sotto il prefisso /books


@router.get("/")
def get_all_books() -> list[Book]: #list[book] è il dato che FastAPI converte in JSON
    """Restituisce la lista di tutti i libri disponibili"""
    return list(books.values()) #Mi restituisce i valori del dizionario books

@router.get("/{id}") # tra parentesi graffe fa una ricerca parametrica
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book")])-> Book:
    """
    Retrunr the book with the given ID
    """
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found" )
    # in caso venga inserito un id non disponibile in data/books.py
    # restituisce un errrore


@router.post("/{id}/review")
def add_review(
    id: Annotated[int, Path(description="The ID of the book")],
    review: Review #FastAPI converte automaticamente il corpo della richiesta in un oggetto Review
):
    """
    Add a review to the book with the given ID
    """
    try:
        books[id].review = review.review
        #stiamo sovrascrivendo il valore della review della classe Book con il valore review della classe Review
        return "Review added successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Libro non trovato")
    # in caso venga inserito un id non disponibile in data/books.py


@router.post("/")
def add_book(book: Book): #book è un istanza della classe Book
    """
    Add a new book to the list
    """
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book ID already exists")
    books[book.id] = book
    return "Book added successfully"

@router.put("/{id}")
def update_book(
    id: Annotated[int, Path(description="The ID of the book")],
    book: Book #FastAPI converte automaticamente il corpo della richiesta in un oggetto Book
):
    """
    Update the book with the given ID
    """
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[id] = book
    return "Book updated successfully"

@router.delete("/")
def delete_all_book():
    """
    Delete all books from the list
    """
    books.clear()
    return "All books deleted successfully"

@router.delete("/{id}")
def delete_book(
    id: Annotated[int, Path(description="The ID of the book")]
):
    """
    Delete the book with the given ID
    """
    try:
        del books[id]
        return "Book deleted successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")