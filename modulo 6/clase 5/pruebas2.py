import os
from pydub import AudioSegment
from openai import OpenAI

SRC = "WhatsApp-Audio-2025-08-13-at-10.57.51-AM.mp3"
WAV = "audio.wav"

# 1) Convertir a WAV 16 kHz mono (mejora la precisión)
audio = AudioSegment.from_file(SRC)
audio = audio.set_frame_rate(16000).set_channels(1)
audio.export(WAV, format="wav")

# 2) Transcribir con Whisper API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
with open(WAV, "rb") as f:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=f,
        language="es",
        temperature=0.0,
        response_format="text"  # también "json" o "srt"
    )

print(transcript)

# Guardar a .txt
with open("transcripcion.txt", "w", encoding="utf-8") as out:
    out.write(transcript if isinstance(transcript, str) else transcript.text)
print("Transcripción guardada en transcripcion.txt")