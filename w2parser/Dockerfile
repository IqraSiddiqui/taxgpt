# Use Python as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# Set up SQLite database (create migrations and apply them)
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port 8000 (Django's default port)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
