import librosa
import numpy as np

def detect_key(audio_path):
    y, sr = librosa.load(audio_path)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = chroma.mean(axis=1)
    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key_idx = np.argmax(chroma_mean)
    brightness = librosa.feature.spectral_centroid(y=y, sr=sr).mean()
    mode = "major" if brightness > 2000 else "minor"
    return {"key": keys[key_idx], "mode": mode}