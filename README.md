# Ask Voice

Simple project for Voice to Action using OpenAI Whisper and OpenAI/Groq function
calling.

## Setup

Add `.env` in `src` directory with OpenAI/Groq API key, need one or the other.

### Local

```
python -m venv venv 
source venv/scripts/activate
```

```
pip install -r requirement.txt
```

Setup OpenAI Whisper for Voice to Text, [Github](https://github.com/openai/whisper) instructions.

Install `ffmpeg`

Mac

```
brew install ffmpeg
```

Windows
```
choco install ffmpeg
```

`PyAudio` dependencies

Mac
```
brew install portaudio
```
### Docker

Install Docker and Docker Compose, depending on install the initial command might
be `docker-compose` or `docker compose`, use accordantly.

Windows 

```
docker-compose -p ask-voice -f docker-compose.yaml up --build -d
```

Mac/Linux

```
docker compose -p ask-voice -f docker-compose.yaml up --build -d
```

## Usage

Initial web server start might take a few seconds (5-30) to download the Whisper 
model.  Either way open a web browser and navigate to `http://localhost:9675`.