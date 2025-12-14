# FastAPI CRUD Mini-Projekt

## Projektbeschreibung
Dieses Mini-Projekt implementiert eine einfache RESTful API mit FastAPI zur Verwaltung von Items. Ziel des Projekts ist es, grundlegende Konzepte moderner Backend-Entwicklung zu demonstrieren, insbesondere HTTP-Methoden, Request-Validierung, persistente Datenspeicherung und API-Tests mit Postman. Die Anwendung wurde im Rahmen eines Lernprojekts im Bereich Data Science und AI Engineering erstellt.

## Technischer Überblick
Die API stellt klassische CRUD-Funktionalitäten (Create, Read, Update, Delete) bereit. Die Datenhaltung erfolgt über eine SQLite-Datenbank, wobei SQLModel für die Modellierung und ORM-Zugriffe genutzt wird. Zur Validierung und Serialisierung der Daten wird Pydantic verwendet. Das Projekt verwendet den modernen Python-Paketmanager **uv** zur Abhängigkeitsverwaltung und Ausführung.

## Verfügbare Endpunkte
- `POST /items/` – Erstellen eines neuen Items  
- `GET /items/` – Abrufen aller Items  
- `GET /items/{item_id}` – Abrufen eines einzelnen Items  
- `PUT /items/{item_id}` – Aktualisieren eines bestehenden Items  
- `DELETE /items/{item_id}` – Löschen eines Items

Alle Endpunkte liefern standardisierte Responses, die über Pydantic Response-Modelle definiert sind.

## Serverstart
Der Server wird lokal über den Paketmanager **uv** gestartet:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000
```

Nach dem Start ist die API unter `http://127.0.0.1:8000` erreichbar. Die automatisch generierte OpenAPI-Dokumentation steht unter `/docs` zur Verfügung.

## Testing
Die Endpunkte können manuell mit Postman getestet werden. Dabei werden folgende Aspekte überprüft:
- Erstellung, Abruf, Aktualisierung und Löschung von Items
- Persistenz der Daten in SQLite
- Konsistenz der Response-Strukturen laut Pydantic-Modellen

## Zielsetzung
Das Projekt dient als kompakte Übungsgrundlage zum Verständnis von REST-APIs, FastAPI-Grundlagen, ORM-Datenbanken und API-Testing-Workflows. Es bildet eine solide Basis für weiterführende, datengetriebene Backend-Anwendungen, inklusive potenzieller Integration von ML-Modellen oder erweiterten Data-Science-Funktionalitäten.

