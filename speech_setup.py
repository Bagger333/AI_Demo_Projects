"""Shared Azure Speech configuration used by the other AI901 speech scripts."""

import os

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_ENDPOINT = os.getenv("SPEECH_ENDPOINT")
DEFAULT_VOICE = os.getenv("SPEECH_VOICE", "en-US-Ava:DragonHDLatestNeural")


def get_speech_config(voice=None):
    """Build a SpeechConfig from the values in .env."""
    if not SPEECH_KEY or not SPEECH_ENDPOINT:
        raise RuntimeError("Set SPEECH_KEY and SPEECH_ENDPOINT in your .env file.")

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        endpoint=SPEECH_ENDPOINT,
    )
    speech_config.speech_synthesis_voice_name = voice or DEFAULT_VOICE
    return speech_config
