import sounddevice as sd
import numpy as np

import whisper

# Load Whisper model
model = whisper.load_model("base")

SAMPLE_RATE = 16000
DURATION = 4  # seconds per recording chunk

def record_audio():
    print("Listening...")                          # duration * samplerate = total samples
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1,
                   dtype='float32')
    sd.wait()
    return np.squeeze(audio)

while True:
    audio_data = record_audio()

    result = model.transcribe(audio_data, fp16=False)
    text = result["text"].strip()

    print("You said:", text)