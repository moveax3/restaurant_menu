from django.contrib import admin

from .models import (
    Dish,
    DishPicture,
    NutritionalValue,
    Allergen,
    Category,
)


class NutritionalValueInline(admin.StackedInline):
    model = NutritionalValue


class DishPictureInline(admin.StackedInline):
    model = DishPicture


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = [
        NutritionalValueInline,
        DishPictureInline,
    ]

