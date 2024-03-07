from typing import List

from main.models import SearchRequestEntity, RequestStatusType
from main.utils.singleton import Singleton


class SearchMusicDao(metaclass=Singleton):
    def __init__(self):
        ...

    def search_music_request(self, email) -> SearchRequestEntity:
        search_request: SearchRequestEntity = SearchRequestEntity.objects.create(
            email=email,
            status=RequestStatusType.PENDING
        )
        return search_request

    def get_search_music_request(self, search_id) -> SearchRequestEntity:
        return SearchRequestEntity.objects.filter(id=search_id).first()

    def update_search_music_request_status(self, search_id, status: str):
        search_request: SearchRequestEntity = self.get_search_music_request(search_id=search_id)
        search_request.status = status
        search_request.save()

    def save_search_music_request_songID(self, search_id, songID):
        search_request: SearchRequestEntity = self.get_search_music_request(search_id=search_id)
        search_request.songID = songID
        search_request.save()

    def get_ready_search_music_requests(self) -> List[SearchRequestEntity]:
        return SearchRequestEntity.objects.filter(status=RequestStatusType.READY).all()
