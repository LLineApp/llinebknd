from django.conf import settings
from django.db import models


class Profile(models.Model):
    cpf = models.TextField(blank=False)
    email = models.EmailField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    preferred_contact = models.TextField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    business_kind = models.TextField(blank=True, null=True)
    business_field = models.TextField(blank=True, null=True)
    company_has_private_insurance = models.NullBooleanField(blank=True, null=True)
    social_security_value = models.FloatField(blank=True, null=True)
    private_security_your_value = models.FloatField(blank=True, null=True)
    private_security_company_value = models.FloatField(blank=True, null=True)
    private_security_current_balance = models.FloatField(blank=True, null=True)
    income_tax_declaration_type = models.TextField(blank=True, null=True)
    monthly_expenses = models.FloatField(blank=True, null=True)
    costs_with_dependents = models.FloatField(blank=True, null=True)
    how_much_you_save = models.FloatField(blank=True, null=True)
    debt_loans = models.FloatField(blank=True, null=True)
    partner_in_company = models.FloatField(blank=True, null=True)
    health = models.TextField(blank=True, null=True)
    plans_and_projects = models.TextField(blank=True, null=True)
    current_investment_process = models.TextField(blank=True, null=True)
    follow_economic_news = models.NullBooleanField(blank=True, null=True)
    accepts_info_about_courses = models.NullBooleanField(blank=True, null=True)
    have_financial_concerns = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    portfolio_income = models.FloatField(blank=True, null=True)

class ImmovableProperties(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    rented = models.NullBooleanField(blank=True, null=True)
    funded = models.NullBooleanField(blank=True, null=True)
    insurance_value = models.FloatField(blank=True, null=True)
    insurance_company = models.TextField(blank=True, null=True)


class Phones(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone = models.TextField(blank=True, null=True)


class InvestorExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    portfolio_type = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)


class Insurance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    insurance_type = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    monthly_fee = models.NullBooleanField(blank=True, null=True)
    coverage = models.FloatField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    
    