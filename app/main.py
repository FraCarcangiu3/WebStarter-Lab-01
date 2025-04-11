from fastapi import FastAPI
from routers import books

#IMPORTO LA LIBRERIA FASTAPI PER CREARE UN'APPLICAZIONE WEB - parte frontend
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request #Request è una classe di FastAPI che rappresenta una richiesta HTTP

app = FastAPI()
app.include_router(books.router, tags=["books"]) #includo il router per la gestione dei libri,
                                                 # tags è un modo per raggruppare le rotte in base alla loro funzionalità


#####PARTE FRONT END###################################################################################################

templates = Jinja2Templates(directory="app/templates") #creo un oggetto Jinja2Templates per gestire i template HTML
@app.get("/", response_class=HTMLResponse) #sto dicendo che codifico questa classe in HTML
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )





if __name__ == "__main__": #è importante perchè esegue il codice che verrà dopo solo se eseguiamo questo file come script principale
    import uvicorn #uvicorn è un server ASGI per eseguire applicazioni web
    uvicorn.run(app, reload=True) #lanciamo l'applicazione FastAPI con il server uvicorn