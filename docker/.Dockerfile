# As Django/Carrot runs on Python, I choose the official Python 3 Docker image.
FROM python:3.11.3

# set environment variables, grab via os.environ
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl ca-certificates wget build-essential portaudio19-dev ffmpeg

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app

# Set the working directory to /app.
WORKDIR /app

# Run the Web Server when the container launches.
CMD python3 main.py