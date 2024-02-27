from main.dal.dao.search_music_dao import SearchMusicDao
from main.utils.singleton import Singleton


class SearchMusicLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_music_dao = SearchMusicDao()

    def search_music(self, email, audio):
        # save audio in s3

        self.search_music_dao.search_music_request(email=email)

        # write on rabbit




