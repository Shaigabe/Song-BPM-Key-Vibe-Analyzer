import librosa

def detect_bpm(audio_path):
    y, sr = librosa.load(audio_path)
    # Use onset strength for robust tempo estimation
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    return tempo