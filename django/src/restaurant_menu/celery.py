from celery import Celery
from django.conf import settings

app = Celery(
    'restaurant_menu',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=['pastebin.tasks',]
)

if __name__ == '__main__':
    app.start()
