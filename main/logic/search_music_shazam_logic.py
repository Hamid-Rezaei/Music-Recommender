from ShazamAPI import Shazam

from adapter.s3.s3 import SimpleStorageService
from main.utils.singleton import Singleton


class SearchMusicShazamLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s3 = SimpleStorageService()

    def recognize_music_by_shazam(self, audio_uri):
        mp3_file_content_to_recognize = self.s3.download_object(object_uri=audio_uri)

        shazam = Shazam(
            mp3_file_content_to_recognize,
            # lang='en',
            # time_zone='Europe/Paris'
        )
        recognize_generator = shazam.recognizeSong()
        while True:
            print(next(recognize_generator))
