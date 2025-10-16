# Use a lightweight, official Python base image
FROM python:3.10-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the batch_runner.py script into the working directory
COPY batch_runner.py .

# Define the default command to execute the script
CMD ["python", "batch_runner.py"]