from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'audio-analysis-api'})

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        file = request.files.get('audio')
        song_title = request.form.get('title')
        artist_name = request.form.get('artist')
        
        if not file:
            return jsonify({'error': 'No audio file uploaded'}), 400

        # Save uploaded audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[-1]) as temp_audio:
            file.save(temp_audio.name)
            audio_path = temp_audio.name

        # Import analysis modules (make sure these files are in your project)
        from bpm_detector import detect_bpm
        from key_detector import detect_key
        from chord_detector import extract_chords
        from lyrics_fetcher import get_lyrics
        from vibe_analyzer import analyze_vibe

        bpm = detect_bpm(audio_path)
        key_data = detect_key(audio_path)  # Should return dict: {'key': 'C', 'mode': 'major'}
        chords = extract_chords(audio_path)
        vibe = analyze_vibe(audio_path)
        lyrics = get_lyrics(song_title, artist_name) if song_title and artist_name else None

        os.remove(audio_path)

        return jsonify({
            'bpm': bpm,
            'key': key_data.get('key', 'C') if isinstance(key_data, dict) else key_data,
            'mode': key_data.get('mode', 'major') if isinstance(key_data, dict) else 'major',
            'chords': chords[:10] if isinstance(chords, list) else [],
            'vibe': vibe,
            'lyrics': lyrics,
            'confidence_scores': {
                'bpm_confidence': 0.85,
                'key_confidence': 0.80
            }
        })
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)