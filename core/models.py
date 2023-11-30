from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class AbstractModel(models.Model):
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


class GeneralSetting(AbstractModel):
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


class ImageSetting(AbstractModel):
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


class SkillModel(AbstractModel):
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


class ExperienceModel(AbstractModel):
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


class EducationModel(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='School Name',
        help_text='',
    )
    major_title = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Major Title',
        help_text='',
    )
    school_location = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='School Location',
        help_text='',
    )
    start_date = models.DateField(
        verbose_name='Start Date'

    )

    class Meta:
        verbose_name = 'Education Setting'
        verbose_name_plural = 'Education Settings'
        ordering = ('start_date',)

    def __str__(self):
        return self.school_name


class SocialMediaModel(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    url = models.URLField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='URL',
        help_text='',
    )
    icon = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Icon',
        help_text='',
    )

    class Meta:
        verbose_name = 'Social Media Setting'
        verbose_name_plural = 'Social Media Settings'
        ordering = ('order',)

    def __str__(self):
        return self.url

class DocumentModel(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    slug=models.SlugField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Slug Name',
        help_text='',
    )

    file = models.FileField(
        default='',
        blank=True,
        null=True,
        verbose_name='File',
        help_text='',
        upload_to='documents/',
    )
    button_text = models.CharField(
        default='',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Button Text',
        help_text='',
    )

    class Meta:
        verbose_name = 'Document Setting'
        verbose_name_plural = 'Document Settings'
        ordering = ('order',)

    def __str__(self):
        return self.button_text