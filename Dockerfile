# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first (for better caching)
COPY requirements.txt .

# Install dependencies
# Make sure gunicorn is in your requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Cloud Run expects the app to listen on the PORT environment variable (default 8080)
ENV PORT=8080

# Command to run the application using Gunicorn (Production Server)
# Replace 'app:app' with 'filename:flask_instance_name'
# e.g., if your file is main.py and flask app is called 'app', use 'main:app'
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app