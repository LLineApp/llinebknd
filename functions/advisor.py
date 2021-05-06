from .models import *
import datetime
import hashlib
import base64


class advisorsLink:
    def createAdvisorsLink(self):
        advisor = FinancialAdvisors.objects.get(cpf__exact=self)
        if advisor:
            now = datetime.datetime.now()
            link = str(now).encode() + advisor.cpf.encode()
            link = hashlib.md5(link).digest()
            link = base64.urlsafe_b64encode(
                link).decode('ascii').replace("=", "")

            _advisor = AdvisorsLink.objects.create(
                advisor=advisor, created_at=now.date(), link=link)
            _advisor.save()

            return _advisor
        pass

    def getAdvisorByLink(self):
        return AdvisorsLink.objects.get(link__exact=self)
