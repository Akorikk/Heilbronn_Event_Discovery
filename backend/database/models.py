from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)
    date = Column(String)
    time = Column(String)

    location = Column(String)

    description = Column(Text)

    source_url = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)