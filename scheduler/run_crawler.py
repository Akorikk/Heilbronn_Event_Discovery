'''import schedule
import time

from crawler.scraper import crawl_heilbronn_events
from extractor.parser import parse_event
from extractor.ai_extractor import extract_event_with_ai
from pipeline.processor import save_events

def run_pipeline():
    print("Starting crawler...")

raw_events = crawl_heilbronn_events()

structured_events = []

for event in raw_events:

    # First try rule-based parser
    parsed = parse_event(event)

    # If parser fails, fallback to AI extraction
    if not parsed.get("title") or not parsed.get("location"):
        print("Parser incomplete, using AI extraction...")
        parsed = extract_event_with_ai(event["raw_text"])
        parsed["source_url"] = event["source_url"]

    structured_events.append(parsed)

save_events(structured_events)

print("Pipeline finished.")

# Run every 1 minutes we can chage it to run every 6 hourse or more 

schedule.every(1).minutes.do(run_pipeline)

print("Scheduler started...")

run_pipeline()

# Keep scheduler running

while True:
    schedule.run_pending()
    time.sleep(60)  '''

import schedule
import time

from crawler.scraper import crawl_heilbronn_events
from extractor.parser import parse_event
from pipeline.processor import save_events


def run_pipeline():
    print("Starting crawler...")

    try:
        raw_events = crawl_heilbronn_events()

        structured_events = []

        for event in raw_events:
            parsed = parse_event(event)
            structured_events.append(parsed)

        save_events(structured_events)

        print("Pipeline finished.")

    except Exception as e:
        print("Crawler error:", e)
        print("Skipping this run and continuing scheduler.")


# For testing run every 10 minutes
# For production you can change this to:
# schedule.every(6).hours.do(run_pipeline)

schedule.every(10).minutes.do(run_pipeline)

print("Scheduler started...")

# Run immediately once when program starts
run_pipeline()

# Keep scheduler running
while True:
    schedule.run_pending()
    time.sleep(60)