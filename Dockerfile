# Use slim Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Set environment variables for Spaces
ENV PORT=7860
ENV HOST=0.0.0.0

# Expose the port (important for Hugging Face Spaces)
EXPOSE 7860

# Use Gunicorn to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--workers", "2", "--threads", "4", "app:app"]
