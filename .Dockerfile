FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first to take advantage of Docker caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Expose the port that Flask uses (5000)
EXPOSE 5000

# Define environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
