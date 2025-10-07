# Song BPM, Key, Vibe Analyzer

A Python tool to analyze audio tracks for BPM, musical key, chord estimation, vibe/mood, and lyrics. This version is deployed as a web API on Railway for easy access.

## Features

- **Accurate BPM Detection** (librosa, multiple features)
- **Key Detection** (librosa, chroma features)
- **Chord Estimation** (audio-based chroma, advanced mapping)
- **Lyrics Fetching** (lyrics.ovh API, robust error handling)
- **Vibe/Mood Analysis** (audio features, simple ML/heuristics)
- **Web API** (Flask-based with endpoints for healthcheck and analysis)

## Installation

```bash
pip install -r requirements.txt
