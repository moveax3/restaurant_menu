from rest_framework import serializers

from dishes.models import (
    Allergen,
    Category,
    Dish,
    DishPicture,
    NutritionalValue,
)


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class DishPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishPicture
        fields = ['dish', 'picture']


class NutritionalValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalValue
        fields = ['proteins', 'fats', 'carbohydrates', 'calories']


class DishesListSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    picture = DishPictureSerializer(read_only=True)
    nutritional_value = NutritionalValueSerializer(read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'price', 'nutritional_value', 'category', 'allergens', 'picture']


class DishesCreateSerializer(serializers.ModelSerializer):
    category = serializers.IntegerField(required=True)
    nutritional_value = NutritionalValueSerializer(required=True)

    def create(self, validated_data):
        nutritional_value = validated_data.pop('nutritional_value')
        dish = Dish.objects.create(**validated_data)
        NutritionalValue.objects.create(dish=dish, **nutritional_value)
        return dish

    def validate_category(self, value):
        try:
            category = Category.objects.get(id=int(value))
            return category
        except Category.DoesNotExist:
            raise serializers.ValidationError("incorrect category")

    class Meta:
        model = Dish
        fields = ['name', 'price', 'nutritional_value', 'category']


class DishesPictureSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        picture = DishPicture.objects.create(**validated_data)
        return picture

    class Meta:
        model = DishPicture
        fields = ['dish', 'picture']
