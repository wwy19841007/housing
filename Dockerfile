# Use an official Python runtime as a parent image
FROM python:2.7

# Copy the current directory contents into the container at /app
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install scrapy

# Set the working directory to /app
#WORKDIR /housing

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["scrapy", "crawl", "anjuke"]