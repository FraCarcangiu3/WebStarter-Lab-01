# Laboratorio di Programmazione Web - Libreria Online

Benvenuto al corso introduttivo di Programmazione Web! Questo progetto è una semplice applicazione per gestire una libreria online, che ti permetterà di imparare i concetti fondamentali dello sviluppo web.

## Indice dei contenuti

1. [Introduzione](#introduzione)
2. [Tecnologie utilizzate](#tecnologie-utilizzate)
3. [Struttura del progetto](#struttura-del-progetto)
4. [Back-end con FastAPI](#back-end-con-fastapi)
5. [Front-end con HTML, CSS e JavaScript](#front-end-con-html-css-e-javascript)
6. [API e comunicazione client-server](#api-e-comunicazione-client-server)
7. [Come eseguire l'applicazione](#come-eseguire-lapplicazione)
8. [Esercizi proposti](#esercizi-proposti)

## Introduzione

Questa applicazione è un esempio pratico di un'applicazione web full-stack che implementa le operazioni CRUD (Create, Read, Update, Delete) su una collezione di libri. L'applicazione permette di:
- Visualizzare l'elenco dei libri
- Aggiungere nuovi libri
- Modificare libri esistenti
- Eliminare libri
- Aggiungere recensioni ai libri

Il progetto è strutturato seguendo le migliori pratiche di sviluppo web moderno, con una chiara separazione tra back-end (server) e front-end (client).

## Tecnologie utilizzate

### Back-end
- **Python**: linguaggio di programmazione versatile e facile da imparare
- **FastAPI**: framework moderno per creare API web con Python
- **Pydantic**: per la validazione dei dati e definizione dei modelli
- **Uvicorn**: server ASGI per eseguire l'applicazione FastAPI

### Front-end
- **HTML5**: per la struttura della pagina web
- **CSS3**: per lo stile e il layout
- **JavaScript**: per la logica dell'interfaccia e le chiamate API

## Struttura del progetto

```
lab2025/
├── app/
│   ├── data/
│   │   └── books.py         # "Database" di esempio con i libri
│   │   └── reviews.py       # Modello per le recensioni
│   │   └── books.py         # Definizione delle API
│   ├── models/
│   │   ├── book.py          # Modello per i libri
│   │   └── review.py        # Modello per le recensioni
│   ├── routers/
│   │   └── books.py         # Definizione delle API
│   ├── templates/
│   │   └── home.html        # Interfaccia utente
│   ├── __init__.py
│   └── main.py              # Punto di ingresso dell'applicazione
└── README.md                # Questa guida
```

## Back-end con FastAPI

### Modelli dati (app/models/)

I modelli dati definiscono la struttura dei nostri oggetti e garantiscono che i dati siano validi.

#### Modello Book (app/models/book.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Annotated[int|None, Field(ge=1, le=5)] = None
```

Questo modello rappresenta un libro con:
- `id`: identificatore numerico univoco
- `title`: titolo del libro
- `author`: autore del libro
- `review`: recensione opzionale (da 1 a 5)

#### Modello Review (app/models/review.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Review(BaseModel):
    review: Annotated[int | None, Field(ge=1, le=5)] = None
```

Questo modello rappresenta una recensione con un valore da 1 a 5.

### Dati di esempio (app/data/books.py)

Per semplicità, usiamo un dizionario Python come "database" invece di un database reale:

```python
from models.book import Book

books = {
    0: Book(id=0, title="libro zero", author="autore zero", review=1),
    1: Book(id=1, title="libro uno", author="autore uno", review=2),
    2: Book(id=2, title="libro due", author="autore due", review=5),
}
```

### API (app/routers/books.py)

Le API definiscono le operazioni che possiamo eseguire sui nostri dati:

- **GET /books**: ottiene tutti i libri (con ordinamento opzionale per valutazione)
- **GET /books/{id}**: ottiene un libro specifico per ID
- **POST /books**: aggiunge un nuovo libro
- **PUT /books/{id}**: aggiorna un libro esistente
- **DELETE /books**: elimina tutti i libri
- **DELETE /books/{id}**: elimina un libro specifico
- **POST /books/{id}/review**: aggiunge una recensione a un libro

### Punto di ingresso (app/main.py)

Il file main.py è il punto di ingresso dell'applicazione:

```python
from fastapi import FastAPI
from routers import books
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
app.include_router(books.router, tags=["books"])

templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)
```

Questo file:
1. Crea un'applicazione FastAPI
2. Integra il router delle API dei libri
3. Configura il sistema di templating Jinja2 per servire la pagina HTML
4. Definisce una route per la pagina principale
5. Avvia il server quando il file viene eseguito direttamente

## Front-end con HTML, CSS e JavaScript

La nostra applicazione front-end è contenuta in un unico file (`app/templates/home.html`), che include HTML, CSS e JavaScript.

### HTML

La struttura HTML organizza l'interfaccia in:
- Header con il titolo dell'applicazione
- Sezione principale con la tabella dei libri
- Form per aggiungere/modificare libri
- Form per aggiungere recensioni

I form sono inizialmente nascosti e vengono mostrati quando necessario.

### CSS

Il CSS è incorporato nell'HTML e definisce:
- Layout generale della pagina
- Stile delle tabelle
- Stile dei form e degli input
- Stile dei pulsanti
- Sistema di valutazione a stelle
- Design responsive per dispositivi mobili

### JavaScript

Il JavaScript gestisce:
1. Caricamento dei dati dal server
2. Aggiornamento dinamico dell'interfaccia
3. Gestione degli eventi utente (clic sui pulsanti, invio dei form)
4. Chiamate API al backend
5. Gestione degli errori e notifiche all'utente

## API e comunicazione client-server

La comunicazione tra frontend e backend avviene tramite chiamate API RESTful:

1. Il frontend invia richieste HTTP al backend (GET, POST, PUT, DELETE)
2. Il backend elabora le richieste e restituisce risposte in formato JSON
3. Il frontend aggiorna l'interfaccia in base alle risposte ricevute

Questa architettura permette una chiara separazione delle responsabilità:
- Il backend si occupa della logica di business e della gestione dei dati
- Il frontend si occupa dell'interfaccia utente e dell'esperienza utente

## Come eseguire l'applicazione

1. Assicurati di avere Python 3.7+ installato
2. Installa le dipendenze:
```bash
pip install fastapi uvicorn jinja2
```
3. Avvia l'applicazione:
```bash
cd lab2025
python -m app.main
```
4. Apri il browser e vai all'indirizzo: `http://localhost:8000`

## Esercizi proposti

Ecco alcuni esercizi per migliorare l'applicazione:

1. **Miglioramenti UI/UX**:
   - Aggiungi una modalità tema scuro
   - Migliora l'aspetto mobile
   - Aggiungi animazioni per le transizioni

2. **Funzionalità aggiuntive**:
   - Aggiungi la ricerca dei libri
   - Implementa categorie/generi per i libri
   - Aggiungi paginazione per la lista dei libri

3. **Persistenza dei dati**:
   - Sostituisci il "database" in-memory con SQLite
   - Aggiungi un database SQL più robusto come PostgreSQL
   - Implementa un ORM come SQLAlchemy

4. **Autenticazione**:
   - Aggiungi un sistema di login
   - Implementa diversi ruoli (utente, admin)
   - Limita alcune operazioni solo agli utenti autenticati

Buon divertimento con la programmazione web!

---

Questo progetto è stato creato per il Laboratorio di Programmazione Web 2025.
