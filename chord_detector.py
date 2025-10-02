import librosa
import numpy as np

def extract_chords(audio_path):
    y, sr = librosa.load(audio_path)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    chord_sequence = []
    window_size = 30
    for i in range(0, chroma.shape[1], window_size):
        window = chroma[:, i:i+window_size]
        if window.shape[1] == 0:
            continue
        chroma_mean = window.mean(axis=1)
        root_idx = np.argmax(chroma_mean)
        chord_sequence.append(keys[root_idx])
    return chord_sequence