import librosa
import numpy as np

def analyze_vibe(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr).mean()
    zcr = librosa.feature.zero_crossing_rate(y).mean()
    rms = librosa.feature.rms(y=y).mean()
    if tempo > 125 and spectral_centroid > 3000 and rms > 0.03:
        return "Energetic"
    elif tempo < 90 and zcr < 0.05:
        return "Calm"
    elif spectral_centroid < 2000 and rms < 0.015:
        return "Warm/Mellow"
    elif rms > 0.04:
        return "Aggressive"
    else:
        return "Neutral"