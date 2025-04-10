from fastapi import FastAPI
from models.book import Book
from data.books import books

app = FastAPI()

@app.get("/books")
def get_all_books() -> list[Book]: #list[book] è il dato che
    """Restituisce la lista di tutti i libri disponibili"""
    return list(books.values()) #Mi restituisce i valori del dizionario books

if __name__ == "__main__": #è importante perchè esegue il codice che verrà dopo solo se eseguiamo questo file come script principale
    import uvicorn #uvicorn è un server ASGI per eseguire applicazioni web
    uvicorn.run(app, reload=True) #lanciamo l'applicazione FastAPI con il server uvicorn