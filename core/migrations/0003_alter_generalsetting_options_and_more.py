# Generated by Django 4.2.7 on 2023-11-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.RemoveField(
            model_name='generalsetting',
            name='site_name',
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='site_title',
            field=models.CharField(blank=True, default='', help_text='Site name', max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameters',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Parameters'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
