from django.db import models


class GeneralSetting(models.Model):
    site_title= models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Name',
        help_text='Site name',
    )
    description = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Description',
        help_text='',
    )

    parameters = models.CharField(
        default='',
        max_length=10000,
        blank=True,
        null=True,
        verbose_name='Parameters',
        help_text='',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated',
        help_text='',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created',
        help_text='',
    )

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('site_title',)

    def __str__(self):
        return self.site_title
