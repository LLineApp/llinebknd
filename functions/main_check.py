from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *
from .outputs import *



def check_main_advisor(self, info, profile_id, advisor_id):
    data_main_advisor = ProfileAdvisors.objects.filter(Profile__exact=profile_id, advisor__exact=advisor_id).count()
    if data_main_advisor != 0:
        return True 
    else:
        return False