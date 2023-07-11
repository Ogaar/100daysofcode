import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import scipy
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures

# Video file path
video_path = 'C:\\Users\\oscar\\OneDrive\\Pictures\\100daysofcode\\sample_video.mp4'

def transcribe_video(video_path):
    try:
        # Load video
        clip = VideoFileClip(video_path)

        # Save audio file
        audio_path = 'temp_audio.wav'
        clip.audio.write_audiofile(audio_path)

        # Initialize recognizer
        r = sr.Recognizer()

        # Transcribe audio file
        with sr.AudioFile(audio_path) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)

        # Clean up audio file
        # os.remove(audio_path)

        # Return transcribed text
        return text

    except Exception as e:
        print(e)

def record_audio():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Starting: Speak now!")
    sd.wait()  # Wait until recording is finished
    print("finished")
    wav.write('output.wav', fs, my_recording)  # Save as WAV file

def callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("|" * int(volume_norm))  # Display the volume in the console.

    if volume_norm < 3:
        print("Silence detected, stopping recording")
        raise sd.CallbackStop()

def main():
    transcription = transcribe_video(video_path)
    print(transcription)

main()

