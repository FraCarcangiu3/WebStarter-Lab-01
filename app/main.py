from fastapi import FastAPI
from models.book import Book
from data.books import books

app = FastAPI()

@app.get("/books")
def get_all_books() -> list[Book]: #list[book] è il dato che
    """Restituisce la lista di tutti i libri disponibili"""
    return list(books.values()) #Mi restituisce i valori del dizionario books
