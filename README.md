# Heilbronn_Event_Discovery

python -m scheduler.run_crawler
uvicorn api.main:app --reload
http://127.0.0.1:8000/events
streamlit run frontend/streamlit_app.py
http://localhost:8501