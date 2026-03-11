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