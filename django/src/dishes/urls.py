from django.conf.urls import include
from django.urls import path

app_name = 'dishes'

urlpatterns = [
    path('api/', include(('dishes.api.urls', 'api'))),
]
