# Generated by Django 2.2.4 on 2022-07-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0024_auto_20210330_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('ordem', models.IntegerField(verbose_name='Ordem')),
            ],
        ),
    ]
