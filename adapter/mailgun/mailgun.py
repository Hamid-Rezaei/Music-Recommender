import requests

from project.configuration.config import Config
from project.configuration.configuration import Configuration


class Mailgun:
    def __init__(self):
        pass

    def send(self, receiver, message):
        return requests.post(
            url=Config.MAIL_URL,
            auth=("api", Config.MAIL_API_KEY),
            files=[("attachment", open(
                "/home/h.rezaei@asax.local/MyWorkspace/cloud/music-recommender-system/0453f14e-4bc5-475c-8ad1-32dbfa7233c8.mp3",
                'rb')), ],
            data={
                "from": "rezaeih061@gmail.com",
                "to": f"{receiver}",
                "subject": "Music",
                "text": "This is your music."
            }
        )


if __name__ == "__main__":
    Configuration.configure(Config)
    mailgun = Mailgun()
    mailgun.send("hamidrezaei.ce@gmail.com", "Hello")
