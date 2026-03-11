#!/bin/bash

echo "Creating project structure..."

# Create directories

mkdir -p crawler
mkdir -p extractor
mkdir -p pipeline
mkdir -p database
mkdir -p api
mkdir -p webhook
mkdir -p scheduler
mkdir -p frontend

# Create Python files

touch crawler/scraper.py
touch crawler/instagram_scraper.py

touch extractor/parser.py
touch extractor/ai_extractor.py

touch pipeline/deduplicate.py
touch pipeline/processor.py

touch database/models.py
touch database/db.py

touch api/main.py
touch api/routes.py

touch webhook/notifier.py

touch scheduler/run_crawler.py

touch frontend/streamlit_app.py

# Root files

touch requirements.txt
touch Dockerfile
touch README.md

echo "Project structure created successfully!"

tree
