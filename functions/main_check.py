from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from .models import *
from .outputs import *



def check_main_advisor(self, info, profile_id, advisor_id):
    data_main_advisor = ProfileAdvisors.objects.filter(Profile__exact=profile_id, advisor__exact=advisor_id).count()
    return not(data_main_advisor)