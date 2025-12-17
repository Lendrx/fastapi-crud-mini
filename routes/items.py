from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import get_session
from models import Item, ItemCreate, ItemResponse

# Router für Item-Endpoints
router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    """Erstellt ein neues Item in der Datenbank."""
    db_item = Item.model_validate(item)
    with get_session() as session:
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
    return db_item

@router.get("/", response_model=list[ItemResponse])
def read_items():
    """Gibt alle Items aus der Datenbank zurück."""
    with get_session() as session:
        items = session.exec(select(Item)).all()
    return items

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: str):
    """Gibt ein spezifisches Item anhand der ID zurück."""
    with get_session() as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item wurde nicht gefunden")
        return item

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, item: ItemCreate):
    """Aktualisiert ein bestehendes Item."""
    with get_session() as session:
        db_item = session.get(Item, item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item wurde nicht gefunden")
        db_item.name = item.name
        db_item.description = item.description
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: str):
    """Löscht ein Item aus der Datenbank."""
    with get_session() as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item wurde nicht gefunden")
        session.delete(item)
        session.commit()
        return item
