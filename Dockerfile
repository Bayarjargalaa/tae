# Base image
FROM python:3.11-slim

# Work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
