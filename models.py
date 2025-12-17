from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional
import uuid

# Pydantic-Modelle für Request/Response-Validierung
class ItemCreate(BaseModel):
    name: str
    description: str | None = None

class Item(BaseModel):
    id: str
    name: str
    description: str | None = None

class ItemResponse(BaseModel):
    id: str
    name: str
    description: str | None = None

# SQLModel für Datenbank-Tabelle
class Item(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str
    description: Optional[str] = None

# SQLModel für Item-Erstellung
class ItemCreate(SQLModel):
    name: str
    description: Optional[str] = None