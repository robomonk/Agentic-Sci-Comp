# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY batch_runner.py .

# Define the default command to run the script
CMD ["python", "batch_runner.py"]