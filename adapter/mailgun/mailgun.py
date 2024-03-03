import requests

from project.configuration.config import Config


class Mailgun:
    def __init__(self):
        pass

    def send(self, receiver, message):
        return requests.post(
            url=Config.MAIL_URL,
            auth=("api", Config.MAIL_API_KEY),
            data={
                "from": f"Excited User <mailgun@{Config.MAIL_DOMAIN_NAME}>",
                "to": ["bar@example.com", f"YOU@YOUR_DOMAIN_NAME"],
                "subject": "Hello",
                "text": "Testing some Mailgun awesomeness!"
            }
        )
