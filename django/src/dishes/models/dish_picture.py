from django.db import models
from model_utils.models import TimeStampedModel

from .dish import Dish


class DishPicture(TimeStampedModel):
    """ Изображение блюда """

    dish = models.OneToOneField(
        Dish,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="picture",
        verbose_name="Блюдо",
    )

    picture = models.ImageField(
        null=False,
        upload_to='dishes/',
        verbose_name="Изображение",
    )

    def __str__(self):
        return f"{self.dish.name} image"

    class Meta:
        verbose_name = "Изображение блюда"
        verbose_name_plural = "Изображения блюд"
