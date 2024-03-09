import json
import logging

from django.db import transaction

from adapter.rabbitmq.rabbitmq_consumer import RabbitMQConsumer
from main.dal.dao.search_music_dao import SearchMusicDao
from main.logic.search_music_shazam_logic import SearchMusicShazamLogic
from main.logic.search_music_spotify_logic import SearchMusicSpotifyLogic

_LOGGER = logging.getLogger(__name__)


class SearchEventConsumerService:
    def __init__(self):
        super().__init__()
        self.search_music_rabbit_consumer_adapter = RabbitMQConsumer()
        self.search_music_shazam_logic = SearchMusicShazamLogic()
        self.search_music_spotify_logic = SearchMusicSpotifyLogic()
        self.search_music_dao = SearchMusicDao()

    def callback(self, ch, method, properties, body: bytes):
        body = json.loads(body)
        print(" [x] Received %r" % body)
        self.serve_event(event=body)

    def consume(self):
        self.search_music_rabbit_consumer_adapter.basic_consume_(callback=self.callback)

    def start(self):
        self.consume()

    def serve_event(self, event):
        print('SERVICE', event)

        with transaction.atomic():
            # shazam
            music_title = self.search_music_shazam_logic.recognize_music_by_shazam(audio_uri=event['audio_uri'])

            # spotify
            spotify_id = self.search_music_spotify_logic.spotify_search_music(track=music_title)

            # database
            self.search_music_dao.save_search_music_request_songID(event['search_id'], spotify_id)

        _LOGGER.log(msg="Successfully served event", level=logging.INFO)
