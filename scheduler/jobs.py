from main.dal.dao.search_music_dao import SearchMusicDao
from main.models import RequestStatusType


class Jobs:
    def __init__(self):
        self.search_music_dao = SearchMusicDao()

    def update_search_request_status(self):
        ready_requests = self.search_music_dao.get_ready_search_music_requests()
        print('injam')

        for ready_request in ready_requests:
            # TODO: send email
            print("email")

            # update status to done
            self.search_music_dao.update_search_music_request_status(
                search_id=ready_request.id,
                status=RequestStatusType.DONE.name
            )
