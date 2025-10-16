# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY batch_runner.py .

# Define the entrypoint to execute the script
# This allows command-line arguments to be passed directly to the script
ENTRYPOINT ["python", "batch_runner.py"]
