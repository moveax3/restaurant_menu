import datetime
import json

from django.db import models
from model_utils.models import TimeStampedModel

from .category import Category
from .allergen import Allergen

from pastebin.tasks import post_paste


class DishManager(models.Manager):
    def get_json_descriptions(self) -> str:
        dishes: list = list(self.all().values('name', 'price'))
        return json.dumps(dishes, ensure_ascii=False)


class Dish(TimeStampedModel):
    """ Блюдо """
    objects = DishManager()

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        post_paste.delay(
            paste_name=datetime.datetime.now(),
            paste_text=Dish.objects.get_json_descriptions(),
        )

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
