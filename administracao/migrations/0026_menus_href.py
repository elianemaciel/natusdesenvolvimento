# Generated by Django 2.2.4 on 2022-07-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0025_menus'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='href',
            field=models.CharField(default='', max_length=200, verbose_name='Link'),
            preserve_default=False,
        ),
    ]
