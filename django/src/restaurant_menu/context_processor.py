from django.conf import settings
from django.urls import reverse

from pastebin.models import PastebinPaste


def debug_context(request):
    return {'DEBUG': settings.DEBUG}


def api_context(request):
    return {
        'API_TOKEN': settings.DRF_STATIC_TOKEN,
        'API_URLS': {
            'dishes': reverse('dishes:api:dishes'),
        },
    }


def urls_context(request):
    return {
        'URLS': {
            'summary': reverse('dishes:dishes_summary'),
            'menu': reverse('dishes:dishes_menu'),
            'pastebin': PastebinPaste.objects.latest('id'),
        },
    }
