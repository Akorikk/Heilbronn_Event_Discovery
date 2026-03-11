from backend.database.db import SessionLocal
from backend.database.models import Event


def save_events(events):

    db = SessionLocal()

    for e in events:

        event = Event(
            title=e.title,
            date=e.date,
            time=e.time,
            location=e.location,
            description=e.description,
            source_url=e.source_url
        )

        db.add(event)

    db.commit()
    db.close()