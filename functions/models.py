from django.conf import settings
from django.db import models


class Profile(models.Model):
    cpf = models.TextField(blank=False)
    email = models.TextField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    birthdate = models.TextField(blank=True, null=True)
    preferred_contact = models.TextField(blank=True, null=True)


class Phones(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone = models.TextField(blank=True, null=True)
