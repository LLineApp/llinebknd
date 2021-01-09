from django.conf import settings
from django.db import models

class Modelo(models.Model):
   token = models.TextField(blank=True)