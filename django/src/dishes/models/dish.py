import datetime
import json

from django.db import models
from django.core import serializers
from model_utils.models import TimeStampedModel

from .category import Category
from .allergen import Allergen

from pastebin.tasks import post_paste


class DishManager(models.Manager):
    def get_json_descriptions(self) -> str:
        return serializers.serialize("json", self.all().values('name', 'price'))


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
        """
        Override save method for creating new Pastebin paste after save
        :param args:
        :param kwargs:
        :return:
        """
        super().save(*args, **kwargs)
        post_paste.delay(
            paste_name=datetime.datetime.now(),
            paste_text=Dish.objects.get_json_descriptions(),
        )

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
