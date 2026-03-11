from crawler.scraper import crawl_heilbronn_events
from extractor.parser import parse_event
from pipeline.processor import save_events


if __name__ == "__main__":

    raw_events = crawl_heilbronn_events()

    structured_events = []

    for event in raw_events:

        parsed = parse_event(event)

        structured_events.append(parsed)

    save_events(structured_events)

    print("Events saved:", structured_events)