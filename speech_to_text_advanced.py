import os
import speech_recognition as sr
from google.cloud import speech_v1p1beta1 as speech
import json
import io
import numpy as np
import librosa

# Replace this with the path to your JSON API key file
API_KEY_JSON_PATH = r"path\YOUR_API_KEY.json"

# Function to transcribe speech using Google Cloud Speech API
def transcribe_google(audio_data):
    # Replace the API key with your own
    client = speech.SpeechClient.from_service_account_json(API_KEY_JSON_PATH)

    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript

# Function to get pitch contour from audio data
def get_pitch_contour(audio_data):
    # Convert the audio data to a format librosa can work with
    audio, sr = librosa.load(io.BytesIO(audio_data), sr=44100)

    # Extract the pitch using the librosa.piptrack method
    pitches, _ = librosa.piptrack(y=audio, sr=sr)

    # Calculate the mean pitch
    mean_pitch = np.mean(pitches)

    return mean_pitch

# Function to listen to audio and transcribe speech
def listen_and_transcribe():
    microphone = sr.Microphone()

    player = 1

    while True:
        recognizer = sr.Recognizer()

        print(f"Player {player} listening...")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, phrase_time_limit=5)

        # Initialize the client using the API_KEY_JSON_PATH
        client = speech.SpeechClient.from_service_account_json(API_KEY_JSON_PATH)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
        )

        # Create a RecognitionAudio object from the audio data
        recognition_audio = speech.RecognitionAudio(content=audio.get_wav_data())

        response = client.recognize(config=config, audio=recognition_audio)

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript

        print(f"Transcription: {transcript}")

        dialogue = f"Player {player}: {transcript}"
        print(dialogue)

        # Estimate gender based on pitch contour
        pitch_contour = get_pitch_contour(audio.get_wav_data())
        gender = "Female" if pitch_contour > 165 else "Male"
        print(f"Estimated gender: {gender}")

        player = 2 if player == 1 else 1

if __name__ == "__main__":
    listen_and_transcribe()

