from typing import Dict
from models import Item
from sqlmodel import SQLModel, create_engine, Session

# In-Memory Dictionary für Items (wird aktuell nicht verwendet)
items: Dict[str, Item] = {}

# Datenbank-URL für SQLite
DATABASE_URL = "sqlite:///database.db"

# Datenbank-Engine erstellen
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """Erstellt die Datenbank und alle Tabellen."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Gibt eine neue Datenbank-Session zurück."""
    return Session(engine)