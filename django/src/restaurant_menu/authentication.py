from django.conf import settings
from django.contrib.auth.models import AnonymousUser

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class StaticTokenAuthentication(BaseAuthentication):
    """
    DRF authentication class for auth requests by static token, passed through header
    """
    def authenticate(self, request):
        token = request.headers.get('TOKEN')
        if token and token == settings.DRF_STATIC_TOKEN:
            return (AnonymousUser(), None)
        raise AuthenticationFailed()
