# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required dependencies
# If you have a requirements.txt file, include it in the image
RUN pip install --no-cache-dir requests

# Expose the port (if your app runs on a specific port, update this)
EXPOSE 8000

# Command to run your script
CMD ["python", "app.py"]
