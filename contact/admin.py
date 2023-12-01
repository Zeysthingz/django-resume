from django.contrib import admin
from .models import *

@admin.register(Messages)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'subject',
        'message',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'name',
        'email',
        'subject',
    ]
    list_editable = [
        'name',
        'email',
        'subject',
        'message',
    ]

    class Meta:
        model = Messages

