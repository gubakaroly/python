# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy the project files
COPY demo /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Python script
CMD ["python", "demo/first-deom.py"]
