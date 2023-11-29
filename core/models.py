from django.db import models


class GeneralSettings(models.Model):
    site_name = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True
    )
    description = models.CharField(
        default='',
        max_length=256,
        null=True,
    )

    parameters = models.CharField(
        default='',
        max_length=256,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    def __str__(self):
        return self.site_name
