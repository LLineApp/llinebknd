from django.test import TestCase, Client
from django.contrib import admin
from graphene.types.scalars import String
from functions.models import Profile


class TestModels(TestCase):
    def setUp(self):
        self.profile1 = Profile.objects.create(
            cpf='98765432101',
            email='yoda@jedi.org',
            fullname='Mestre Yoda',
            birthdate='1975-06-19',
            preferred_contact='(48) 999999999',
            maritalStatus='solteiro',
            maritalHowManyYears=25,
            parentsAreThemSupportedByYou=False,
            parentsHowMuchYouSuportThem=0.00,
            parentsIsThereAPossibilityOfInheritance=False,
            parentsOfWhom='',
            parentsWhatIsTheEstimatedValue=0.00,
            occupation='Jedi',
            role='Mestre',
            company_name='Republica Galática',
            business_email='yoda@republica.gov',
            business_kind='Treinamento de padawans',
            business_field='Arte Jedi',
            company_has_private_insurance=False,
            social_security_value=0.00,
            private_security_your_value=0.00,
            private_security_company_value=0.00,
            private_security_current_balance=0.00,
            income_tax_declaration_type='',
            monthly_expenses=0.00,
            costs_with_dependents=0.00,
            how_much_you_save=0.00,
            debt_loans=0.00,
            partner_in_company=0.00,
            health='Saude muito eu ter',
            plans_and_projects='Com você esteja a força',
            have_financial_concerns='Nenhum',
            additional_info='Isso é só um teste',
            portfolio_income=0.00,
            page=19
        )

    def test_profile(self):
        expected_count = 1
        expected_fullname = 'Mestre Yoda'
        found = Profile.objects.all()
        self.assertEquals(found.count(), expected_count)
        self.assertEquals(found.first().fullname, expected_fullname)
