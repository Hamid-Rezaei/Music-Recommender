import uuid

from django.db import models
from django.utils import timezone


class RequestStatusType(models.TextChoices):
    PENDING = 'pending'
    FAILURE = 'failure'
    READY = 'ready'
    DONE = 'done'


class SearchRequestEntity(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField()
    status = models.CharField(
        choices=RequestStatusType.choices,
        default=RequestStatusType.PENDING,
        max_length=32
    )
    songID = models.CharField(max_length=100)
    creation_time = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'main'
        db_table = 'search_request'

