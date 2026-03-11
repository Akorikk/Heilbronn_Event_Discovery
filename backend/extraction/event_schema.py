from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Event(BaseModel):
    title: str
    date: Optional[str]
    time: Optional[str]
    location: Optional[str]
    description: Optional[str]
    source_url: str
    scraped_at: datetime = datetime.utcnow()