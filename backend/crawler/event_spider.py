import asyncio
import re
from urllib.parse import urljoin

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

from backend.extraction.event_schema import Event


BASE_URL = "https://www.heilbronnlebt.de"
EVENTS_URL = "https://www.heilbronnlebt.de/events"


def clean(text):
    if not text:
        return None
    return re.sub(r"\s+", " ", text).strip()


async def crawl_events():

    events = []

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()

        print("Opening events page...")

        await page.goto(EVENTS_URL, wait_until="domcontentloaded", timeout=60000)

        await page.wait_for_selector("article")

        html = await page.content()

        soup = BeautifulSoup(html, "html.parser")

        cards = soup.find_all("article")

        print("Event cards detected:", len(cards))

        for card in cards:

            try:

                title_tag = card.find(["h2","h3","a"])

                if not title_tag:
                    continue

                title = clean(title_tag.text)

                link_tag = card.find("a", href=True)

                if not link_tag:
                    continue

                event_url = urljoin(BASE_URL, link_tag["href"])

                text = clean(card.get_text())

                date_match = re.search(r"\d{1,2}\.\s?[A-Za-zÄÖÜäöü]+", text)
                time_match = re.search(r"\d{1,2}:\d{2}", text)

                date = date_match.group() if date_match else None
                time = time_match.group() if time_match else None

                location_match = re.search(r"\d{5}\s[A-Za-zÄÖÜäöü]+", text)

                location = location_match.group() if location_match else "Heilbronn"

                desc_tag = card.find("p")

                description = clean(desc_tag.text) if desc_tag else None

                event = Event(
                    title=title,
                    date=date,
                    time=time,
                    location=location,
                    description=description,
                    source_url=event_url
                )

                events.append(event)

            except Exception as e:

                print("Error parsing card:", e)

        await browser.close()

    print("\nTotal clean events extracted:", len(events), "\n")

    return events


async def main():

    events = await crawl_events()

    for event in events:
        print(event.model_dump())


if __name__ == "__main__":
    asyncio.run(main())