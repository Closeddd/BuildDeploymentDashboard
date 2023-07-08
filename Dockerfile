# Use an appropriate base image for your Django application
FROM python:3.11

# Set the working directory to the current directory (Backend folder)
WORKDIR /Backend

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire Backend directory into the Docker image
COPY . .

# Expose the necessary port (e.g., 8000 for Django)
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]