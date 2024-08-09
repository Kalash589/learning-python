import requests
from bs4 import BeautifulSoup
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "cda1e10619e448ca9065b7142c771169"
CLIENT_SECRET = "941bd0ffdfb94c68a990c5a6ed70a0d7"
USER_ID = "31yjqyk7dyolnkkfvtt2zhi4ehgm"


date = input("select date in format YYYY-MM-DD:")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
data = response.text

soup = BeautifulSoup(data ,  "html.parser")
# year = int(input("year: "))
# month = int(input("month: "))
# day = int(input("day: "))
# weekday = datetime.
# date1 = datetime.date(year ,month , day)
# date1.strftime("%A" "%B" "%d" "%Y")
# print(date1)
# time = datetime.date.weekday
# print(time)
song_tags = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_tags]
# print(song_names)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Kalash",
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(song_uris)

user_playlist =sp.user_playlist_create(user=USER_ID , name="onkar mc", public=False, collaborative=False ,)
sp.playlist_add_items(playlist_id=user_playlist["id"], items=song_uris)