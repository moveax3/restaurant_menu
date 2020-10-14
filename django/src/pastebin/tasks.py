import os

import requests
from celery import shared_task

from .models import PastebinPaste


@shared_task
def post_paste(paste_name: str, paste_text: str):
    """
    Make new paste in pastebin.com and save paste url to PastebinPaste model.
    https://pastebin.com/doc_api
    :param paste_name:
    :param paste_text:
    :return:
    """
    data = {
        'api_option': 'paste',
        'api_dev_key': os.getenv('PASTEBIN_KEY'),
        'api_paste_private': 0,
        'api_paste_name': paste_name,
        'api_paste_expire_date': '1Y',
        'api_paste_format': 'json',
        'api_paste_code': paste_text,
    }
    PASTEBIN_POST_URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(PASTEBIN_POST_URL, data=data)
    if response.status_code == 200:
        PastebinPaste.objects.create(link=response.text)
