from adapter.mailgun.mailgun import Mailgun
from main.dal.dao.search_music_dao import SearchMusicDao
from main.models import RequestStatusType


class Jobs:
    def __init__(self):
        self.search_music_dao = SearchMusicDao()
        self.mail_adapter = Mailgun()

    def update_search_request_status(self):
        ready_requests = self.search_music_dao.get_ready_search_music_requests()

        for ready_request in ready_requests:
            # send email
            attachments = open(
                "/home/hamid/Myworkspace/cloud/music-recommender-system/0453f14e-4bc5-475c-8ad1-32dbfa7233c8.mp3",
                'rb'
            )
            self.mail_adapter.send(receiver=ready_request.email, message="This is your music.", attachments=attachments)

            # update status to done
            self.search_music_dao.update_search_music_request_status(
                search_id=ready_request.id,
                status=RequestStatusType.DONE
            )

            print('One Task was Done')
