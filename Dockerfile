FROM python:3.12-slim

# Install build tools for llama-cpp
RUN apt-get update && apt-get install -y \
    build-essential cmake curl git && \
    apt-get clean

# Set workdir
WORKDIR /app

# Copy code
COPY app.py requirements.txt ./
COPY models ./models

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
