from django.contrib import admin
from .models import *


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'site_title',
        'description',
        'parameters',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'site_title',
        'description',
        'parameters',
    ]
    list_editable = [
        'description',
        'parameters',
    ]

    class Meta:
        model = GeneralSetting
