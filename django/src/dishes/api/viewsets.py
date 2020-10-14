from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet


from .serializers import (
    DishesListSerializer,
    DishesCreateSerializer,
    DishesPictureSerializer,
)
from ..models import Dish


class DishesViewSet(ModelViewSet):

    def get_queryset(self):
        return Dish.objects.all().select_related(
            'category',
            'nutritional_value',
        ).prefetch_related(
            'allergens',
        )

    def get_serializer_class(self):
        if self.action == 'list':
            return DishesListSerializer
        elif self.action == 'create':
            return DishesCreateSerializer

    def list(self, request):

        try:
            dishes_ids = [int(dish_id) for dish_id in request.GET.get('dishes', '').split(',') if dish_id]
        except ValueError:
            dishes_ids = []
        queryset = self.get_queryset()
        if dishes_ids:
            queryset = queryset.filter(id__in=dishes_ids)

        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            dish = serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={'id': dish.id})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DishPictureViewSet(ViewSet):

    parser_classes = (MultiPartParser, FormParser)

    def create(self, request):
        serializer = DishesPictureSerializer(data=request.data)
        if serializer.is_valid():
            picture = serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={'url': picture.picture.path})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
