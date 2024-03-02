import os
from pathlib import Path
from openai import OpenAI
client = OpenAI()

def create_audio_from_summary(summary):
    speech_file_path = Path(__file__).parent / "news.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=summary
    )

    response.stream_to_file(speech_file_path)
