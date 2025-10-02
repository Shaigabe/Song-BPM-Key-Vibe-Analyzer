import requests

def get_lyrics(song_title, artist_name):
    url = f"https://api.lyrics.ovh/v1/{artist_name}/{song_title}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lyrics = response.json().get('lyrics', '').strip()
            if lyrics:
                return lyrics
            else:
                return "Lyrics not found for this song."
        else:
            return f"Error fetching lyrics: {response.status_code}"
    except Exception as e:
        return f"Lyrics fetch failed: {str(e)}"