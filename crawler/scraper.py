from playwright.sync_api import sync_playwright


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

    return events