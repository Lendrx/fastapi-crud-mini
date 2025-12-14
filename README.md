# FastAPI CRUD Projekt mit SQLite und Postman

In diesem Projekt hab ich FastAPI genommen, weil es super einfach ist, schnelle APIs zu bauen.
Als Paketmanager setze ich auf uv – für mich aktuell der absolute Gamechanger, um Dependencies sauber zu halten und das Ding schnell zu starten

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688)
![SQLite](https://img.shields.io/badge/SQLite-persistence-green)
![uv](https://img.shields.io/badge/uv-package%20manager-purple)

## Worum geht’s?
Dieses Projekt zeigt, wie man mit FastAPI eine kleine API erstellt, um Items zu verwalten. CRUD ist am Start: Items erstellen, lesen, updaten und löschen. Alles wird jetzt in SQLite gespeichert, also bleiben die Daten auch nach einem Neustart erhalten. Meiner Meinung nach ein guter Einstieg in persistente Daten und ORM.

## Endpunkte
- `POST /items/` – Neues Item anlegen. Hier könnt ihr den Body als JSON rüberschicken.
- `GET /items/` – Alle Items abholen.
- `GET /items/{item_id}` – Ein einzelnes Item abholen.
- `PUT /items/{item_id}` – Ein Item updaten.
- `DELETE /items/{item_id}` – Item löschen.

Die Responses sind clean durch Pydantic Response-Modelle. Kein unnötiger Kram in der Ausgabe.

## Server starten

Um die API lokal auszuführen, starte den Server mit uvicorn über den Paketmanager uv:

```bash
uv run uvicorn main:app
```

## Testen mit Postman
Hier könnt ihr Postman nehmen, um alle Endpunkte auszuprobieren. Einfach die URL eingeben, Header auf JSON setzen und los geht’s. So könnt ihr sehen, dass alles funktioniert – Items erstellen, lesen, updaten, löschen. Macht auch Spaß zu sehen, dass die Daten in SQLite bleiben.

## Warum das Ganze?
Das Projekt ist eine gute Übung, um FastAPI, SQLite und API-Tests zu kombinieren. Ihr lernt, wie man Daten persistent speichert, saubere Responses liefert und APIs testet. Außerdem eine Basis, falls ihr später ML-Modelle oder andere Data-Science-Sachen über eine API servieren wollt.
