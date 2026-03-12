"""from playwright.sync_api import sync_playwright


def crawl_heilbronn_events():

    url = "https://www.heilbronnlebt.de/events"

    events = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(url)

        page.wait_for_timeout(5000)

        cards = page.query_selector_all("article")

        for card in cards:

            text = card.inner_text()

            events.append({
                "raw_text": text,
                "source_url": url
            })

        browser.close()

    return events"""

from playwright.sync_api import sync_playwright


EVENT_SOURCES = [
    "https://www.heilbronnlebt.de/events",
    "https://www.heilbronn.de/tourismus/events.html",
    "https://www.eventbrite.com/d/germany--heilbronn/events/"
]


def crawl_heilbronn_events():

    events = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in EVENT_SOURCES:

            print(f"Crawling source: {url}")

            try:
                page.goto(url, timeout=60000)

                page.wait_for_timeout(3000)

                page_content = page.inner_text("body")

                events.append({
                    "raw_text": page_content,
                    "source_url": url
                })

            except Exception as e:
                print(f"Failed to crawl {url}: {e}")

        browser.close()

    return events