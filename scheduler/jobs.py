from adapter.mailgun.mailgun import Mailgun
from main.dal.dao.search_music_dao import SearchMusicDao
from main.logic.search_music_spotify_logic import SearchMusicSpotifyLogic
from main.models import RequestStatusType


class Jobs:
    def __init__(self):
        self.search_music_dao = SearchMusicDao()
        self.search_music_spotify_logic = SearchMusicSpotifyLogic()
        self.mail_adapter = Mailgun()

    def update_search_request_status(self):
        print("update search request status")
        ready_requests = self.search_music_dao.get_ready_search_music_requests()

        for ready_request in ready_requests:
            # send email
            recommended_songs = self.search_music_spotify_logic.spotify_recommends_music(songId=ready_request.songID)
            self.mail_adapter.send(receiver=ready_request.email, message=f"I recommend you listening to: {recommended_songs}")

            # update status to done
            self.search_music_dao.update_search_music_request_status(
                search_id=ready_request.id,
                status=RequestStatusType.DONE
            )

            print('One Task was Done')
