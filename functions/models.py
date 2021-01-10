from django.conf import settings
from django.db import models

class Profile(models.Model):
   token = models.TextField(blank=True)