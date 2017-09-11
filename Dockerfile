FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app
ADD . /app
RUN pip install Flask
EXPOSE 8001:8001
# Run app.py when the container launches
CMD ["python", "app.py"]

