from django.conf.urls import include
from django.urls import path

from .views import (
    menu_view,
    summary_view,
)

app_name = 'dishes'

urlpatterns = [
    path('', menu_view, name='dishes_menu'),
    path('summary/', summary_view, name='dishes_summary'),
    path('api/', include(('dishes.api.urls', 'api'))),
]
