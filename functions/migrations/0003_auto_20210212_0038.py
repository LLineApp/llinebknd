# Generated by Django 2.1.4 on 2021-02-12 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0002_auto_20210211_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialAdvisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(null=True)),
                ('register', models.TextField(null=True)),
                ('company', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='accept_financial_advisor_contact',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='profile',
            name='financial_advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='functions.FinancialAdvisors'),
        ),
    ]
