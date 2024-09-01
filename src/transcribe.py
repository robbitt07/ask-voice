import whisper

from datetime import date
from pathlib import Path
import os
from time import time

whisper_model = whisper.load_model("base.en")


def transcribe_audio(audio_bytes: bytes) -> str:
    date_str = date.today().strftime("%y%m%d")
    file_time = time()
    fl = f"./data/{date_str}/audi_{file_time}.wav"
    Path(os.path.dirname(fl)).mkdir(parents=True, exist_ok=True)
    with open(fl, "wb") as f:
        f.write(audio_bytes)

    result = whisper_model.transcribe(fl, temperature=0, fp16=False)
    fl = f"./data/{date_str}/transcribe_{file_time}.txt"
    with open(fl, "w") as f:
        f.write(result["text"])
    return result["text"]
