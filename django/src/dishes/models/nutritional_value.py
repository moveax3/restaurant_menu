from django.db import models
from model_utils.models import TimeStampedModel

from .dish import Dish


class NutritionalValue(TimeStampedModel):
    """ Пищевая ценность """

    dish = models.OneToOneField(
        Dish,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="nutritional_value",
        verbose_name="Блюдо",
    )

    proteins = models.FloatField(
        null=False,
        verbose_name="Протеины"
    )

    fats = models.FloatField(
        null=False,
        verbose_name="Жиры"
    )

    carbohydrates = models.FloatField(
        null=False,
        verbose_name="Углеводы"
    )

    calories = models.IntegerField(
        null=False,
        verbose_name="Калории"
    )

    def __str__(self):
        return f"{self.dish.name} prot: {self.proteins} fat: {self.fats} carb: {self.carbohydrates} cal: {self.calories}"

    class Meta:
        verbose_name = "Пищевая ценность"
        verbose_name_plural = "Пищевая ценность"
