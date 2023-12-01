from core.models import AbstractModel
from django.db import models


class Messages(AbstractModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Name',
        help_text='',

    )
    email = models.EmailField(
        default='',
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Email',
        help_text='',

    )
    subject = models.CharField(
        default='',
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Subject',
        help_text='',

    )
    message = models.TextField(
        default='',
        blank=True,
        null=True,
        verbose_name='Message',
        help_text='',

    )

    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
