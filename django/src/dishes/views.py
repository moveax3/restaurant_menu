from django.conf import settings
from django.shortcuts import render


def menu_view(request):
    # TODO: token to decorator
    return render(
        request,
        'dishes/menu.html',
        {'API_TOKEN': settings.DRF_STATIC_TOKEN}
    )


def summary_view(request):
    # TODO: token to decorator
    return render(
        request,
        'dishes/summary.html',
        {'API_TOKEN': settings.DRF_STATIC_TOKEN}
    )
