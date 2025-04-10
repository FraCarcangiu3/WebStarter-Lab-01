from fastapi import FastAPI
from routers import books

app = FastAPI()
app.include_router(books.router, tags=["books"]) #includo il router per la gestione dei libri,
                                                 # tags è un modo per raggruppare le rotte in base alla loro funzionalità


if __name__ == "__main__": #è importante perchè esegue il codice che verrà dopo solo se eseguiamo questo file come script principale
    import uvicorn #uvicorn è un server ASGI per eseguire applicazioni web
    uvicorn.run(app, reload=True) #lanciamo l'applicazione FastAPI con il server uvicorn