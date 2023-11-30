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


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'file',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'name',
        'file',
    ]
    list_editable = [
        'name',
        'file',
    ]

    class Meta:
        model = ImageSetting
