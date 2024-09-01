import argparse
from glob import glob
import os
from pathlib import Path
import ssl
import whisper


ssl._create_default_https_context = ssl._create_unverified_context


if __name__ == "__main__":
    whisper_model = whisper.load_model("base.en")

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="File")
    parser.add_argument("-l", "--list", action="store_true", help="List Files?")
    args = parser.parse_args()
    if args.list:
        print(glob(os.path.join("data", "raw", "*")))

    else:
        result = whisper_model.transcribe(args.file, temperature=0)
        print(result["text"])

        # Write results
        out_file_name = os.path.join(
            "data", "transcribed",
            Path(os.path.basename(args.file)).with_suffix('.transcript')
        )
        with open(out_file_name, "w") as f:
            f.write(result["text"])
