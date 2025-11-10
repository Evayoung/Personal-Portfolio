# Use Python 3.11 (more stable than 3.13 for Reflex)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies INCLUDING unzip
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Initialize Reflex and export the app
RUN reflex init && \
    reflex export --no-zip

# Expose port (Render will override with $PORT)
EXPOSE 8000

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV REFLEX_ENV=prod

# Start command - single process, no workers
CMD reflex run --env prod --loglevel info --backend-host 0.0.0.0 --backend-port $PORT