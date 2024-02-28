from adapter.rabbitmq.rabbitmq_publisher import RabbitMQPublisher
from main.dal.dao.search_music_dao import SearchMusicDao
from main.utils.singleton import Singleton


class SearchMusicLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_music_dao = SearchMusicDao()
        self.search_music_rabbit_publisher_adapter = RabbitMQPublisher()

    def search_music(self, email, audio):
        # save audio in s3

        search_music = self.search_music_dao.search_music_request(email=email)

        # write on rabbit
        self.search_music_rabbit_publisher_adapter.basic_publish(body=str(search_music.songID))


    # def
