FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY src ./src

# Set PYTHONPATH to include /app
ENV PYTHONPATH=/app

# Expose FastAPI port
EXPOSE 8000

# Run server
CMD ["uvicorn", "src:app", "--host", "0.0.0.0", "--port", "8000"]