from django.db import models
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    """ Категория блюда """

    name = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Название"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
