"""Speech-to-text: turn microphone audio into text.

Run this file directly for continuous recognition, or import listen_once()
from another file to grab a single spoken phrase.
"""

import azure.cognitiveservices.speech as speechsdk

from speech_setup import get_speech_config


def make_recognizer():
    """Create a recognizer wired to the default microphone."""
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    return speechsdk.SpeechRecognizer(
        speech_config=get_speech_config(),
        audio_config=audio_config,
    )


def listen_once(prompt="Say something..."):
    """Listen for one phrase and return it as text, or None if nothing was heard."""
    recognizer = make_recognizer()

    if prompt:
        print(prompt)

    result = recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text

    if result.reason == speechsdk.ResultReason.NoMatch:
        print("Didn't catch that.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        details = result.cancellation_details
        print(f"Recognition canceled: {details.reason}")
        if details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {details.error_details}")

    return None


def listen_continuous():
    """Stream recognition results to the console until you press Enter."""
    recognizer = make_recognizer()

    recognizer.recognizing.connect(lambda evt: print(f"Recognizing: {evt.result.text}"))
    recognizer.recognized.connect(lambda evt: print(f"Recognized: {evt.result.text}"))

    recognizer.start_continuous_recognition()
    print("Say something...")
    input("Press Enter to stop...")
    recognizer.stop_continuous_recognition()


if __name__ == "__main__":
    listen_continuous()
