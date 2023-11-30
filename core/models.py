from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class AbastractModel(models.Model):
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
        abstract = True


class GeneralSetting(AbastractModel):
    site_title = models.CharField(
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

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('site_title',)

    def __str__(self):
        return self.site_title


class ImageSetting(AbastractModel):
    name = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        blank=True,
        null=True,
        verbose_name='Image',
        help_text='',
        upload_to='images/',
    )

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

    def __str__(self):
        return self.name


class SkillModel(AbastractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Description',
        help_text='',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    class Meta:
        verbose_name = 'Skill Setting'
        verbose_name_plural = 'Skill Settings'
        ordering = ('order',)

    def __str__(self):
        return self.name


class ExperienceModel(AbastractModel):
    company_name = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Company Name',
        help_text='',
    )

    job_title = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Job Title',
        help_text='',
    )
    job_location = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Job Location',
        help_text='',
    )
    start_date = models.DateField(
        verbose_name='Start Date'

    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='End Date'

    )
    class Meta:
        verbose_name = 'Experience Setting'
        verbose_name_plural = 'Experience Settings'
        ordering = ('start_date',)

    def __str__(self):
        return self.company_name


