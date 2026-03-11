from fastapi import FastAPI
from database.db import SessionLocal
from database.models import Event

app = FastAPI(title="Heilbronn Event Discovery API")


@app.get("/events")
def get_events():

    db = SessionLocal()

    events = db.query(Event).all()

    result = []

    for e in events:
        result.append({
            "title": e.title,
            "date": e.date,
            "time": e.time,
            "location": e.location,
            "description": e.description,
            "source_url": e.source_url
        })

    db.close()

    return result