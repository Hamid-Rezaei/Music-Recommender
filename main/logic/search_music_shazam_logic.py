import requests

from adapter.s3.s3 import SimpleStorageService
from main.utils.singleton import Singleton
from project.configuration.config import Config
from project.configuration.configuration import Configuration


class SearchMusicShazamLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s3 = SimpleStorageService()

    def recognize_music_by_shazam(self, audio_uri):
        # audio_name = '0453f14e-4bc5-475c-8ad1-32dbfa7233c8.mp3'
        files = {"upload_file": open(Config.FILES_FOLDER + audio_uri, 'rb')}
        headers = {
            "X-RapidAPI-Key": Config.SHAZAM_API_KEY,
            "X-RapidAPI-Host": Config.SHAZAM_HOST
        }

        response = requests.post(url=Config.SHAZAM_URL, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['track']['title']
        else:
            print(f"Shazam Error: {response.status_code}")
            raise


if __name__ == '__main__':
    Configuration.configure(Config)

    search_shazam_logic = SearchMusicShazamLogic()
    search_shazam_logic.recognize_music_by_shazam(
        '0453f14e-4bc5-475c-8ad1-32dbfa7233c8.mp3'
    )
