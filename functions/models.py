from django.conf import settings
from django.db import models


class Profile(models.Model):
    cpf = models.TextField(blank=False)
    email = models.TextField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    birthdate = models.TextField(blank=True, null=True)
    preferred_contact = models.TextField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    business_email = models.TextField(blank=True, null=True)
    business_kind = models.TextField(blank=True, null=True)
    business_field = models.TextField(blank=True, null=True)
    company_has_private_insurance = models.NullBooleanField(blank=True, null=True)
    social_security_value = models.TextField(blank=True, null=True)
    private_security_your_value = models.TextField(blank=True, null=True)
    private_security_company_value = models.TextField(blank=True, null=True)
    private_security_current_balance = models.TextField(blank=True, null=True)
    income_tax_declaration_type = models.TextField(blank=True, null=True)




class Phones(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone = models.TextField(blank=True, null=True)
