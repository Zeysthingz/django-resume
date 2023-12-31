# Generated by Django 4.2.7 on 2023-11-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_educationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('url', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='URL')),
                ('icon', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social Media Setting',
                'verbose_name_plural': 'Social Media Settings',
                'ordering': ('order',),
            },
        ),
    ]
