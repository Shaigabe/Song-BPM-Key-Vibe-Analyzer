from flask import Flask, request, jsonify
import librosa
import traceback

app = Flask(__name__)

@app.route('/analyzeAudioAdvanced', methods=['POST'])
def analyze_audio_advanced():
    try:
        file = request.files['audio']
        if not file:
            return jsonify({'error': 'No audio file provided.'}), 400
        
        # Save the file
        filepath = f"/tmp/{file.filename}"
        file.save(filepath)
        
        # Run analysis (replace with your analyzer logic)
        y, sr = librosa.load(filepath)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        # Add more analysis here
        
        result = {
            'bpm': tempo,
            # Add more results
        }
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()