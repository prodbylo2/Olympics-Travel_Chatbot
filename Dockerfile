# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable (optional if needed)
# ENV FLASK_ENV=development

# Run app2.py when the container launches
CMD python ./app2.py
