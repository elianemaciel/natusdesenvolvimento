# Generated by Django 2.2.4 on 2021-01-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0021_banner_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='file',
        ),
    ]
