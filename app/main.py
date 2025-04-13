from fastapi import FastAPI
from routers import books

<<<<<<< HEAD
<<<<<<< HEAD
# === IMPORTAZIONE LIBRERIE PER IL FRONTEND ===
# HTMLResponse: Classe che rappresenta una risposta HTTP in formato HTML
from fastapi.responses import HTMLResponse
# Jinja2Templates: Sistema di template per generare pagine HTML dinamiche
from fastapi.templating import Jinja2Templates
# Request: Classe che rappresenta una richiesta HTTP inviata dal client
from fastapi import Request
# StaticFiles: Per servire file statici come immagini, CSS e JavaScript
from fastapi.staticfiles import StaticFiles
=======
=======
>>>>>>> parent of 6c9e7c0 (update commit)
#IMPORTO LA LIBRERIA FASTAPI PER CREARE UN'APPLICAZIONE WEB - parte frontend
from fastapi.responses import HTMLResponse #HTMLResponse è una classe di FastAPI che rappresenta una risposta HTTP in formato HTML
from fastapi.templating import Jinja2Templates #Jinja2Templates è una classe di FastAPI che gestisce i template HTML
from fastapi import Request #Request è una classe di FastAPI che rappresenta una richiesta HTTP
###################################################
<<<<<<< HEAD
>>>>>>> parent of 6c9e7c0 (update commit)
=======
>>>>>>> parent of 6c9e7c0 (update commit)

#IMPORTO LA LIBRERIA FASTAPI PER CREARE UN'APPLICAZIONE WEB - parte backend
app = FastAPI()
app.include_router(books.router, tags=["books"]) #includo il router per la gestione dei libri,
                                                 # tags è un modo per raggruppare le rotte in base alla loro funzionalità
<<<<<<< HEAD

<<<<<<< HEAD
# Configurazione per servire i file statici
# Il primo parametro è il prefisso URL, il secondo è il percorso della cartella
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# === CONFIGURAZIONE FRONT-END ===
# Configurazione del sistema di template Jinja2, specificando la directory dove si trovano i file HTML
templates = Jinja2Templates(directory="app/templates")
=======
>>>>>>> parent of 6c9e7c0 (update commit)
=======

>>>>>>> parent of 6c9e7c0 (update commit)

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