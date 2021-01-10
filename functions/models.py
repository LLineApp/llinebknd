from django.conf import settings
from django.db import models

class Profile(models.Model):
   token = models.TextField(blank=True)
   email = models.TextField(blank=True)
   fullname = models.TextField(blank=True)
   birthdate = models.TextField(blank=True)
   phones = models.TextField(blank=True)
   preferred_contact = models.TextField(blank=True)