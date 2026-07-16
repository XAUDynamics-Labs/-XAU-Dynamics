# XAU Dynamics - Data Pipeline Microservice
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY config.py .
COPY pipeline.py .

# Environment variables defaults
ENV GOLD_FEED_URL="wss://stream-api.xau-dynamics.io/v3/gold"

CMD ["python", "pipeline.py"]
