"""
Django rest framework specific settings
https://www.django-rest-framework.org/api-guide/settings/
"""

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'CustomAuthClass',  # TODO: Release
    ],
}
