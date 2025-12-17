from fastapi import FastAPI
from database import create_db_and_tables
from routes.items import router as items_router

# FastAPI-Anwendung erstellen
app = FastAPI()

@app.on_event("startup")
def on_startup():
    """Wird beim Start der Anwendung ausgeführt - erstellt Datenbank-Tabellen."""
    create_db_and_tables()

# Item-Router zur Anwendung hinzufügen
app.include_router(items_router)
