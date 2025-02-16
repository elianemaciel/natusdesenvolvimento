# Generated by Django 2.2.4 on 2020-10-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0015_auto_20200828_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='banner/'),
        ),
        migrations.AlterField(
            model_name='configuracao',
            name='imagem_fundadora',
            field=models.ImageField(blank=True, null=True, upload_to='settings/'),
        ),
        migrations.AlterField(
            model_name='configuracao',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='settings/'),
        ),
        migrations.AlterField(
            model_name='depoimentos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
