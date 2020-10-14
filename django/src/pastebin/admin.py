from django.contrib import admin

from .models import PastebinPaste

@admin.register(PastebinPaste)
class PastebinPasteAdmin(admin.ModelAdmin):
    pass
