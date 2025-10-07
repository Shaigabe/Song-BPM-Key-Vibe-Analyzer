from flask import Flask, request, jsonify
import librosa
import os
import requests
from bpm_detector import detect_bpm
from key_detector import detect_key
from chord_detector import extract_chords
from lyrics_fetcher import get_lyrics
from vibe_analyzer import analyze_vibe

app = Flask(__name__)

def analyze_audio(audio_path, song_title=None, artist_name=None):
    try:
        # Load audio
        y, sr = librosa.load(audio_path)
        
        # Call analysis modules
        tempo = detect_bpm(audio_path)
        key = detect_key(audio_path)
        chords = extract_chords(audio_path)
        vibe = analyze_vibe(audio_path)
        lyrics = None
        if song_title and artist_name:
            lyrics = get_lyrics(song_title, artist_name)
        
        return {
            "bpm": float(tempo) if isinstance(tempo, (int, float)) else tempo,
            "key": key,
            "vibe": vibe,
            "chords": chords,
            "lyrics": lyrics
        }
    except Exception as e:
        return {"error": str(e)}

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'audio' not in request.files and 'audio_path' not in request.form:
        return jsonify({"error": "No audio file or path provided"}), 400
    
    song_title = request.form.get('song_title')
    artist_name = request.form.get('artist_name')
    
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_path = os.path.join("uploads", audio_file.filename)
        os.makedirs("uploads", exist_ok=True)
        audio_file.save(audio_path)
    else:
        audio_path = request.form['audio_path']
    
    result = analyze_audio(audio_path, song_title, artist_name)
    
    if 'audio' in request.files and os.path.exists(audio_path):
        os.remove(audio_path)
    
    return jsonify(result), 200 if "error" not in result else 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
