import requests

from project.configuration.config import Config
from project.configuration.configuration import Configuration


class Mailgun:
    def __init__(self):
        pass

    def send(self, receiver, message, attachments):
        request = requests.post(
            url=Config.MAIL_URL,
            auth=("api", Config.MAIL_API_KEY),
            files=[("attachment", attachments)],
            data={
                "from": f"mailgun@{Config.MAIL_DOMAIN_NAME}",
                "to": f"{receiver}",
                "subject": "Music",
                "text": message
            }
        )
        print(f'Email sent to {receiver} with status code {request.status_code}')


if __name__ == "__main__":
    Configuration.configure(Config)
    mailgun = Mailgun()
    attachments_ = open(
        "/home/hamid/Myworkspace/cloud/music-recommender-system/0453f14e-4bc5-475c-8ad1-32dbfa7233c8.mp3",
        'rb'
    )

    mailgun.send("rezaeih061@gmail.com", "Hello", attachments_)
