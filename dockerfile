# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the movie recommendation script and movies.txt file into the container
COPY watch_next.py .
COPY movies.txt .


# Set the entrypoint command to run the next movie recommendation script
CMD [ "python", "watch_next.py" ]
