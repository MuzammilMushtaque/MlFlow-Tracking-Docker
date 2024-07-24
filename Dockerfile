# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Update the package list
RUN apt-get update

# Install Git and other dependencies
RUN apt-get install -y git --fix-missing

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY MLFlow_2.py .

# Run the Python script and then start MLflow UI
CMD python MLFlow_2.py && mlflow ui --host 0.0.0.0
