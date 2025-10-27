import requests


# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

# Replace with the song you want to search
song_title = "Blinding Lights"

# Base URL from GetSongBPM API documentation
url = "https://api.getsongbpm.com/search/"

# Parameters for the GET request
params = {
    "api_key": API_KEY,
    "type": "search",      # depending on API docs, may be "search" or "song"
    "query": song_title
}

try:
    response = requests.get(url, params=params, headers={
        "User-Agent": "Mozilla/5.0"
    })
    response.raise_for_status()  # raise error for bad status codes

    data = response.json()
    # Inspect the returned JSON
    print("Response JSON:", data)

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except Exception as e:
    print("Error:", e)
