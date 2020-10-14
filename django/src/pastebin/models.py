from django.db import models
from model_utils.models import TimeStampedModel


class PastebinPaste(TimeStampedModel):
    link = models.URLField(null=False)

    def __str__(self) -> str:
        return self.link
