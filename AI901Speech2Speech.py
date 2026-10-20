"""Speech-to-speech: listen to the microphone, then say it back.

Both halves are imported from the other files in this folder -- this file
contains no speech SDK code of its own.
"""

from AI901Speech import listen_once
from AI901TextToSpeech import speak
from script import *

STOP_WORDS = {"stop", "quit", "exit", "goodbye"}


def echo_loop():
    print('Speech-to-speech. Say "stop" to quit.\n')

    while True:
        text = listen_once("Listening...")
        if not text:
            continue

        print(f"You said: {text}")

        if text.strip().lower().rstrip(".!?") in STOP_WORDS:
            speak("Goodbye.")
            break

        response_message = create_Asnwer(text)
        speak(response_message)


if __name__ == "__main__":
    echo_loop()
