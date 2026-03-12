import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/events"

st.set_page_config(page_title="Heilbronn Event Discovery", layout="wide")

st.title("🎉 Heilbronn Event Discovery")
st.write("Automatically discovered public events in Heilbronn and surrounding areas.")

# Fetch events from API
try:
    response = requests.get(API_URL)
    events = response.json()
except Exception as e:
    st.error("Failed to fetch events from API.")
    st.stop()


if not events:
    st.warning("No events found.")
else:

    st.subheader(f"📅 {len(events)} Events Found")

    for event in events:

        with st.container():

            st.markdown("---")

            st.subheader(event["title"])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("📆 Date")
                st.write(event["date"])

            with col2:
                st.write("⏰ Time")
                st.write(event["time"])

            with col3:
                st.write("📍 Location")
                st.write(event["location"])

            st.write("📝 Description")
            st.write(event["description"])

            st.markdown(f"[Source Link]({event['source_url']})")

"""import sys
import os

# Fix module path so Streamlit can find project folders
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import requests

from crawler.scraper import crawl_heilbronn_events
from extractor.parser import parse_event
from pipeline.processor import save_events

API_URL = "http://127.0.0.1:8000/events"

st.set_page_config(
    page_title="Heilbronn Event Discovery",
    page_icon="🎉",
    layout="wide"
)

# Sidebar (Control Panel)
st.sidebar.title("⚙️ Control Panel")

search_query = st.sidebar.text_input("Search Events")

discover = st.sidebar.button("🔎 Discover Events")

st.sidebar.markdown("---")
st.sidebar.caption("Heilbronn Event Discovery Platform")

# Main Header
st.title("🎉 Heilbronn Event Discovery Platform")
st.caption("Automated discovery of public events in Heilbronn and surrounding areas")

st.divider()

# Run crawler when button clicked
if discover:

    with st.spinner("Crawling event websites..."):

        raw_events = crawl_heilbronn_events()

        structured_events = []

        for event in raw_events:
            parsed = parse_event(event)
            structured_events.append(parsed)

        save_events(structured_events)

        st.success("Events discovered and saved successfully!")

st.divider()

# Fetch events from API
try:
    response = requests.get(API_URL)
    events = response.json()
except:
    st.warning("⚠️ API not running. Start FastAPI server.")
    events = []

# Dashboard Metrics
col1, col2 = st.columns(2)

col1.metric("📅 Total Events", len(events))
col2.metric("🌐 Sources Crawled", "3")

st.divider()

# Search Filter
if search_query:
    events = [
        e for e in events
        if search_query.lower() in e["title"].lower()
    ]

# Display Events
if not events:

    st.info("No events found. Click 'Discover Events' to crawl websites.")

else:

    for event in events:

        with st.container():

            st.markdown(f"### {event['title']}")

            col1, col2, col3 = st.columns(3)

            col1.write(f"📆 **Date:** {event['date']}")
            col2.write(f"⏰ **Time:** {event['time']}")
            col3.write(f"📍 **Location:** {event['location']}")

            st.write(event["description"])

            st.markdown(f"[🔗 Source Link]({event['source_url']})")

            st.divider()

# Footer
st.caption("⚙️ Powered by FastAPI • Playwright • Streamlit • Webhooks")"""