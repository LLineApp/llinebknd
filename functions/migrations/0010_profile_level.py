# Generated by Django 2.2 on 2021-08-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0009_auto_20210707_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
