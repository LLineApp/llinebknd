# Generated by Django 2.2 on 2021-03-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0002_auto_20210304_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='page',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
