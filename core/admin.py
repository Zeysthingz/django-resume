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

@admin.register(SkillModel)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order',
        'name',
        'description',
        'percentage',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'name',
    ]
    list_editable = [
        'description',
        'percentage',
        'order',
    ]

    class Meta:
        model = SkillModel


@admin.register(ExperienceModel)
class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company_name',
        'job_title',
        'job_location',
        'start_date',
        'end_date',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'company_name',
        'job_title',
        'job_location'
    ]
    list_editable = [
        'company_name',
        'job_title',
        'job_location',
        'start_date',
        'end_date',
    ]

    class Meta:
        model = ExperienceModel

@admin.register(EducationModel)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'school_name',
        'school_location',
        'major_title',
        'start_date',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'school_name',
        'school_location',
    ]
    list_editable = [
        'school_name',
        'school_location',
    ]

    class Meta:
        model = EducationModel

@admin.register(SocialMediaModel)
class SocialMediaModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'url',
        'icon',
        'order',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'url',
        'icon',
    ]
    list_editable = [
        'url',
        'icon',
        'order',
    ]

    class Meta:
        model = SocialMediaModel
