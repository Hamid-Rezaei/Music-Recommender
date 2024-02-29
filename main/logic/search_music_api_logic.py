from datetime import datetime

from adapter.rabbitmq.rabbitmq_publisher import RabbitMQPublisher
from adapter.s3.s3 import SimpleStorageService
from main.dal.dao.search_music_dao import SearchMusicDao
from main.utils.singleton import Singleton


class SearchMusicLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_music_dao = SearchMusicDao()
        self.search_music_rabbit_publisher_adapter = RabbitMQPublisher()
        self.s3_adapter = SimpleStorageService()

    def _generate_audio_uri(self, search_music_id: str, filename: str):
        year = datetime.now().year
        updated_file_name = f'{search_music_id}.{filename.rsplit(".")[-1]}'
        return '/'.join([str(year), 'audio', updated_file_name])

    def search_music(self, email, audio):
        search_music = self.search_music_dao.search_music_request(email=email)

        # save audio in s3
        audio_uri = self._generate_audio_uri(str(search_music.id), filename=audio.name)
        self.s3_adapter.upload_object(file=audio.file, object_uri=audio_uri)

        # write on rabbit
        self.search_music_rabbit_publisher_adapter.basic_publish(body=audio_uri)
