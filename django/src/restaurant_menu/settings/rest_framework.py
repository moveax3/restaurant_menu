"""
Django rest framework specific settings
https://www.django-rest-framework.org/api-guide/settings/
"""

DRF_STATIC_TOKEN = "123456"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'restaurant_menu.authentication.StaticTokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
