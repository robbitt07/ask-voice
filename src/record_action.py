import speech_recognition as sr
from speech_recognition.audio import AudioData
import ssl
import whisper

from time import time

ssl._create_default_https_context = ssl._create_unverified_context


def transcribe_audio(audio: AudioData) -> str:
    fl = f"./data/sample_{time()}.wav"
    with open(fl, "wb") as f:
        f.write(audio.get_wav_data())

    result = whisper_model.transcribe(fl, temperature=0)
    return result["text"]


def run_question_answer():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
        result = transcribe_audio(audio=audio)
        return result


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    whisper_model = whisper.load_model("base.en")
    # whisper_model = whisper.load_model("medium.en")
    result = run_question_answer()
