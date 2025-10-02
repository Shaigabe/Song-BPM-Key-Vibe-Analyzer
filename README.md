# BPM, Track Analyzer, Key of Song, Vibe of the Song

A Python tool to analyze audio tracks for BPM, musical key, chord estimation, vibe/mood, and lyrics.

## Features
- **Accurate BPM Detection** (librosa, multiple features)
- **Key Detection** (librosa, chroma features)
- **Chord Estimation** (audio-based chroma, advanced mapping)
- **Lyrics Fetching** (lyrics.ovh API, robust error handling)
- **Vibe/Mood Analysis** (audio features, simple ML/heuristics)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py <audio_path> [<song_title> <artist_name>]
```

## Notes

- Most accurate results for commercial/popular tracks when providing song title and artist for lyrics.
- Chord estimation is based on dominant chroma features; for best results, use high-quality audio.
- For advanced chord detection, consider integrating with Chordino or other ML models.

## Contributing
Open an issue or PR with suggestions!