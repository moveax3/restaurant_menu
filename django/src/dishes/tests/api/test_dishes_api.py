import json
import os

import pytest

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import Client
from django.urls import reverse
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_201_CREATED,
)

from dishes.models import Dish


@pytest.fixture
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'dishes.json')


@pytest.fixture
def dish_test_data():
    return {
        'name': 'TestName',
        'price': 999,
        'nutritional_value': {
            'proteins': 0.1,
            'fats': 0.2,
            'carbohydrates': 0.3,
            'calories': 4000,
        },
        'category': 1,
    }


@pytest.mark.django_db
def test_unauth_request(load_fixtures):
    client = Client()
    url = reverse('dishes:api:dishes')
    response = client.get(url)
    assert response.status_code == HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_get_dishes(load_fixtures):
    client = Client(X_TOKEN=settings.DRF_STATIC_TOKEN)
    url = reverse('dishes:api:dishes')
    response = client.get(url)
    assert response.status_code == HTTP_200_OK
    data = json.loads(response.content)
    assert Dish.objects.all().count() == len(data)

    for response_dish in data:
        original_dish = Dish.objects.get(id=response_dish['id'])
        assert original_dish.name == response_dish['name']
        assert original_dish.price == response_dish['price']
        assert original_dish.picture.picture.path == response_dish['picture']['picture']
        assert original_dish.category.name == response_dish['category']['name']
        assert original_dish.nutritional_value.proteins == response_dish['nutritional_value']['proteins']
        assert original_dish.nutritional_value.fats == response_dish['nutritional_value']['fats']
        assert original_dish.nutritional_value.carbohydrates == response_dish['nutritional_value']['carbohydrates']
        assert original_dish.nutritional_value.calories == response_dish['nutritional_value']['calories']
        original_allergens = [allergen.id for allergen in original_dish.allergens.all()]
        response_allergens = [allergen['id'] for allergen in data[0]['allergens']]
        assert original_allergens.sort() == response_allergens.sort()


@pytest.mark.django_db
def test_create_dish(load_fixtures, dish_test_data):
    client = Client(X_TOKEN=settings.DRF_STATIC_TOKEN)
    url = reverse('dishes:api:dishes')
    response = client.post(url, data=dish_test_data, content_type='application/json')
    assert response.status_code == HTTP_201_CREATED
    dish = Dish.objects.get(id=response.data.pop('id'))
    assert dish.name == dish_test_data['name']
    assert dish.price == dish_test_data['price']
    assert dish.nutritional_value.proteins == dish_test_data['nutritional_value']['proteins']
    assert dish.nutritional_value.fats == dish_test_data['nutritional_value']['fats']
    assert dish.nutritional_value.carbohydrates == dish_test_data['nutritional_value']['carbohydrates']
    assert dish.nutritional_value.calories == dish_test_data['nutritional_value']['calories']
    assert dish.category.id == dish_test_data['category']


@pytest.mark.django_db
def test_upload_dish_picture(load_fixtures, dish_test_data):
    client = Client(X_TOKEN=settings.DRF_STATIC_TOKEN)
    url = reverse('dishes:api:dishes')
    response = client.post(url, data=dish_test_data, content_type='application/json')
    dish_id = response.data.pop('id')
    url = reverse('dishes:api:dish_image')
    file_content = (
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52'
        b'\x00\x00\x01\x00\x00\x00\x01\x00\x01\x03\x00\x00\x00\x66\xBC\x3A'
        b'\x25\x00\x00\x00\x03\x50\x4C\x54\x45\xB5\xD0\xD0\x63\x04\x16\xEA'
        b'\x00\x00\x00\x1F\x49\x44\x41\x54\x68\x81\xED\xC1\x01\x0D\x00\x00'
        b'\x00\xC2\xA0\xF7\x4F\x6D\x0E\x37\xA0\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\xBE\x0D\x21\x00\x00\x01\x9A\x60\xE1\xD5\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'
    )
    dish_picture = SimpleUploadedFile("file.jpg", file_content, content_type="image/png")
    response = client.post(url, {'dish': dish_id, 'picture': dish_picture}, format='multipart')
    assert response.status_code == HTTP_201_CREATED
    assert Dish.objects.get(id=dish_id).picture.picture.read() == file_content
