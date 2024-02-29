import requests

from main.utils.singleton import Singleton


class SearchMusicShazamLogic(metaclass=Singleton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_music_by_shazam(self, audio):
        url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"

        payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"upload_file\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
        headers = {
            "content-type": "multipart/form-data; boundary=---011000010111000001101001",
            "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
            "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
        }

        response = requests.post(url, data=payload, headers=headers)

        print(response.json())
