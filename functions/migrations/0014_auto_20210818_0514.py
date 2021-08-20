# Generated by Django 2.2 on 2021-08-18 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0013_financialadvisors_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targets',
            name='lower_variation',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='upper_variation',
        ),
        migrations.AddField(
            model_name='targets',
            name='investmentType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='functions.InvestmentType'),
        ),
        migrations.AlterField(
            model_name='financialadvisors',
            name='active',
            field=models.NullBooleanField(default=True),
        ),
    ]
