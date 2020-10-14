from django.urls import path

from .viewsets import (
    DishesViewSet,
    DishPictureViewSet,
)

urlpatterns = [
    path(
        '',
        DishesViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='dishes',
    ),
    path(
        'image',
        DishPictureViewSet.as_view({'post': 'create'}),
        name='dish_image'
    )
]
