# Generated by Django 2.2 on 2021-08-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0012_investmenttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialadvisors',
            name='active',
            field=models.NullBooleanField(True),
        ),
    ]
