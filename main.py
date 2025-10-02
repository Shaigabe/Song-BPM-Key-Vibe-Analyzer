import sys
from bpm_detector import detect_bpm
from key_detector import detect_key
from chord_detector import extract_chords
from lyrics_fetcher import get_lyrics
from vibe_analyzer import analyze_vibe

def main(audio_path, song_title=None, artist_name=None):
    print(f"Analyzing: {audio_path}")
    bpm = detect_bpm(audio_path)
    key = detect_key(audio_path)
    chords = extract_chords(audio_path)
    vibe = analyze_vibe(audio_path)
    lyrics = None
    if song_title and artist_name:
        lyrics = get_lyrics(song_title, artist_name)
    print(f"BPM: {bpm:.2f}")
    print(f"Key: {key}")
    print(f"Chords (top 10 estimates): {chords[:10]}")
    print(f"Vibe: {vibe}")
    if lyrics:
        print(f"\nLyrics:\n{lyrics}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_path> [<song_title> <artist_name>]")
    else:
        audio_path = sys.argv[1]
        song_title = sys.argv[2] if len(sys.argv) > 2 else None
        artist_name = sys.argv[3] if len(sys.argv) > 3 else None
        main(audio_path, song_title, artist_name)