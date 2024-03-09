import uuid

from main.dal.dao.search_music_dao import SearchMusicDao
from main.utils.singleton import Singleton


class SearchMusicSpotifyLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_music_dao = SearchMusicDao()

    def spotify_search_music(self, track):

        # find spotify id

        return uuid.uuid4()
