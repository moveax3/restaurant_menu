from django.db import models
from model_utils.models import TimeStampedModel


class Allergen(TimeStampedModel):
    """ Аллергены """

    name = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Название"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аллерген"
        verbose_name_plural = "Аллергены"
