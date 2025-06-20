# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Set environment variables (optional)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run migrations (optional, for entrypoint)
# CMD and ENTRYPOINT will be discussed later

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
