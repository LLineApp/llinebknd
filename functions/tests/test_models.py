from django.test import TestCase, Client
from django.contrib import admin
from graphene.types.scalars import String
from functions.models import Profile


class TestModels(TestCase):
    def setUp(self):
        self.profile1 = Profile.objects.create(
            cpf='19176206831',
            email='renato@lline.com.br',
            fullname='Renato da Silva',
            birthdate='1975-06-19',
            preferred_contact='(48) 988379329',
            maritalStatus='casado',
            maritalHowManyYears=25,
            spouseName='Kátia da Silva',
            spouseOccupation='Confeiteira',
            parentsAreThemSupportedByYou=False,
            parentsHowMuchYouSuportThem=0.00,
            parentsIsThereAPossibilityOfInheritance=False,
            parentsOfWhom='',
            parentsWhatIsTheEstimatedValue=0.00,
            occupation='Programador',
            role='Programador',
            company_name='LLine',
            business_email='renato@lline.com.br',
            business_kind='Desenvolvimento de software',
            business_field='Tecnologia',
            business_phones='(48) 98837-9329',
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
            health='Nem me fala',
            plans_and_projects='Pobre não tem planos nem projetos',
            have_financial_concerns='Todos',
            additional_info='Isso é só um teste',
            portfolio_income=0.00,
            page=19
        )

    def test_profile(self):
        expected_count = 1
        expected_fullname = 'Renato da Silva'
        found = Profile.objects.all()
        self.assertEquals(found.count(), expected_count)
        self.assertEqual(found.first().fullname, expected_fullname)
