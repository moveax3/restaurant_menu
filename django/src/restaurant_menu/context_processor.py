from django.conf import settings
from django.urls import reverse

from pastebin.models import PastebinPaste


def debug_context(request):
    return {'DEBUG': settings.DEBUG}


def api_context(request):
    """
    API params context like static token and API endpoints
    :param request:
    :return:
    """
    return {
        'API_TOKEN': settings.DRF_STATIC_TOKEN,
        'API_URLS': {
            'dishes': reverse('dishes:api:dishes'),
        },
    }


def urls_context(request):
    """
    Urls endpoints context like pages or external urls
    :param request:
    :return:
    """
    try:
        pastebin_url = PastebinPaste.objects.latest('id')
    except PastebinPaste.DoesNotExist:
        pastebin_url = ''
    return {
        'URLS': {
            'summary': reverse('dishes:dishes_summary'),
            'menu': reverse('dishes:dishes_menu'),
            'pastebin': pastebin_url,
        },
    }
