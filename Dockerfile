# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
