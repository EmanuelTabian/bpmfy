import requests


# Replace with your actual API key
API_KEY = "your_api_key"

# Replace with the song you want to search
song_title = "metallica"

# Base URL from GetSongBPM API documentation
url = "https://api.getsongbpm.co/search/"

# Parameters for the GET request
params = {
    "api_key": API_KEY,
    "type": "artist",      # depending on API docs, may be "search" or "song"
    "lookup": song_title
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # raise error for bad status codes

    data = response.json()
    # Inspect the returned JSON
    print("Response JSON:", data)

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except Exception as e:
    print("Error:", e)
