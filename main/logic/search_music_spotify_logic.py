import requests

from main.dal.dao.search_music_dao import SearchMusicDao
from main.utils.singleton import Singleton
from project.configuration.config import Config
from project.configuration.configuration import Configuration


class SearchMusicSpotifyLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_music_dao = SearchMusicDao()

    def spotify_search_music(self, track):
        # find spotify id

        url = Config.SPOTIFY_SEARCH_URL

        querystring = {"q": f"{track}", "type": "tracks", "offset": "5", "limit": "5", "numberOfTopResults": "5"}

        headers = {
            "X-RapidAPI-Key": Config.SPOTIFY_API_KEY,
            "X-RapidAPI-Host": Config.SPOTIFY_HOST
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        songId = data['tracks']['items'][0]['data']['id']
        return songId

    def spotify_recommends_music(self, songId):
        url = Config.SPOTIFY_RECOMMENDATION_URL

        querystring = {"limit": "5", "seed_tracks": f"{songId}"}

        headers = {
            "X-RapidAPI-Key": Config.SPOTIFY_API_KEY,
            "X-RapidAPI-Host": Config.SPOTIFY_HOST
        }

        response = requests.get(url, headers=headers, params=querystring)

        response = response.json()
        recommended_tracks = ""
        for i in range(5):
            recommended_tracks += response['tracks'][i]['name']

        return recommended_tracks


if __name__ == "__main__":
    Configuration.configure(Config)
    print(SearchMusicSpotifyLogic().spotify_search_music('Believer'))
