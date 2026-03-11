#!/bin/bash

echo "Creating project structure..."

mkdir -p backend/crawler
mkdir -p backend/extraction
mkdir -p backend/pipeline
mkdir -p backend/api
mkdir -p backend/database
mkdir -p backend/scheduler

mkdir -p frontend
mkdir -p logs
mkdir -p data

touch backend/crawler/__init__.py
touch backend/crawler/event_spider.py
touch backend/crawler/instagram_scraper.py
touch backend/crawler/sources.py

touch backend/extraction/__init__.py
touch backend/extraction/ai_parser.py
touch backend/extraction/event_schema.py

touch backend/pipeline/__init__.py
touch backend/pipeline/deduplication.py
touch backend/pipeline/event_processor.py

touch backend/api/__init__.py
touch backend/api/main.py
touch backend/api/routes.py

touch backend/database/__init__.py
touch backend/database/models.py
touch backend/database/db.py

touch backend/scheduler/__init__.py
touch backend/scheduler/crawler_job.py

touch requirements.txt
touch README.md
touch .env

echo "Project structure created successfully!"