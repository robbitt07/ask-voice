from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

import base64
from decouple import config

from db import Database
from functions import tools
from service import route_action
from text_to_object import text_to_object
from transcribe import transcribe_audio

from logging import getLogger

logger = getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

db = Database()


@app.route("/speech-to-action", methods=["POST"])
def speech_to_action():
    try:
        data = request.json
        if "audio" in data:
            audio_base64 = data["audio"]
            if not audio_base64:
                return jsonify({"error": "No Audio"}), 400

            audio_bytes = base64.b64decode(audio_base64)
            transcribed_result = transcribe_audio(audio_bytes=audio_bytes)

            # Get Action
            actions = text_to_object(text=transcribed_result, tools=tools)

            # Execute Action
            action_result = route_action(db=db, actions=actions)

            return jsonify({
                "message": transcribed_result,
                "actions": actions,
                "action_result": action_result
            }), 200
        else:
            return jsonify({"error": "No audio data provided"}), 400
    except Exception as e:
        logger.error(str(e), exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/text-to-action", methods=["POST"])
def text_to_action():
    try:
        data = request.json
        if "message" in data:
            message = data["message"]

            # Get Action
            actions = text_to_object(prompt=message)

            # Execute Action
            action_result = route_action(db=db, actions=actions)

            return jsonify({
                "message": message,
                "actions": actions,
                "action_result": action_result
            }), 200
        else:
            return jsonify({"error": "No audio data provided"}), 400
    except Exception as e:
        logger.error(str(e), exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/")
def index():
    return send_file("index.html")


if __name__ == "__main__":
    app.run(
        host=config("API_HOST", cast=str, default="0.0.0.0"),
        port=config("API_PORT", cast=int, default=8080),
        debug=config("DEBUG", cast=bool, default=True)
    )
