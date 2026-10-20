"""Text-to-speech: turn text into audio on the default speaker.

Run this file directly to type something and hear it, or import speak()
from another file.
"""

import azure.cognitiveservices.speech as speechsdk

from speech_setup import get_speech_config


def speak(text, voice=None):
    """Speak `text` through the default speaker. Returns True on success."""
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=get_speech_config(voice),
        audio_config=audio_config,
    )

    result = synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return True

    if result.reason == speechsdk.ResultReason.Canceled:
        details = result.cancellation_details
        print(f"Speech synthesis canceled: {details.reason}")
        if details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {details.error_details}")
            print("Did you set the speech resource key and endpoint values?")

    return False


if __name__ == "__main__":
    print("Enter some text that you want to speak >")
    text = input()
    if speak(text):
        print(f"Speech synthesized for text [{text}]")
