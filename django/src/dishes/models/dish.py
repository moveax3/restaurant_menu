from django.db import models
from model_utils.models import TimeStampedModel

from .category import Category
from .allergen import Allergen


class Dish(TimeStampedModel):
    """ Блюдо """

    name = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Название блюда",
    )

    price = models.IntegerField(
        null=False,
        verbose_name="Цена",
    )



    category = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.CASCADE,
        related_name="dishes",
        verbose_name="Категория",
    )

    allergens = models.ManyToManyField(
        Allergen,
        related_name="dishes",
        verbose_name="Аллергены",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
