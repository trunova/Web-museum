# Generated by Django 2.2 on 2022-11-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20221124_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum_piece',
            name='date_of_creation',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]
