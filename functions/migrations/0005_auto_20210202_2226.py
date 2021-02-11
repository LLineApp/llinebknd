# Generated by Django 2.1.4 on 2021-02-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0004_auto_20210122_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='business_email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='business_field',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='business_kind',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_has_private_insurance',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='income_tax_declaration_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='private_security_company_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='private_security_current_balance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='private_security_your_value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_security_value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
