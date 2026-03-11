from database.db import SessionLocal
from database.models import Event
from webhook.notifier import send_webhook


def save_events(events):

    db = SessionLocal()

    for e in events:

        existing_event = db.query(Event).filter(
            Event.title == e["title"],
            Event.date == e["date"],
            Event.time == e["time"]
        ).first()

        if existing_event:
            continue

        event = Event(
            title=e["title"],
            date=e["date"],
            time=e["time"],
            location=e["location"],
            description=e["description"],
            source_url=e["source_url"]
        )

        db.add(event)

        # send webhook for new event
        send_webhook(e)

    db.commit()
    db.close()