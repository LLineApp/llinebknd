from django.conf import settings
from django.db import models

class Phone(models.Model):
   phones = models.TextField(blank=True,null=True)


class Profile(models.Model):
   cpf = models.TextField(blank=False)
   email = models.TextField(blank=True, null=True)
   fullname = models.TextField(blank=True, null=True)
   birthdate = models.TextField(blank=True, null=True)
   phones = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)
   preferred_contact = models.TextField(blank=True, null=True)

