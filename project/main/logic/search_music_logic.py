from project.main.utils.singleton import Singleton


class SearchMusicLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
