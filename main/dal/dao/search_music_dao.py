from main.models import SearchRequestEntity, RequestStatusType


class SearchMusicDao:
    def __init__(self):
        ...

    def search_music_request(self, email):
        SearchRequestEntity.objects.create(email=email, status=RequestStatusType.PENDING)
