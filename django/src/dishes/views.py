from django.shortcuts import render


def menu_view(request):
    return render(
        request,
        'dishes/menu.html',
    )


def summary_view(request):
    return render(
        request,
        'dishes/summary.html',
    )
