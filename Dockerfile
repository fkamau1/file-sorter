# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY . /app

# Install any needed packages specified in requirements.txt and watchdog library
RUN pip install --no-cache-dir -r requirements.txt
    
# Make port 80 available to the world outside this container
EXPOSE 80

# Run file-sorter.py when the container launches
CMD ["python", "./file-sorter.py"]