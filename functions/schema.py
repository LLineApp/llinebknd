import graphene

from graphene_django import DjangoObjectType

from .models import *
from django.db.models import Q

from .auth import getCPFFromAuth

from .inputs import *
from .outputs import *


class FinancialAdvisorsType(DjangoObjectType):
    class Meta:
        model = FinancialAdvisors


class setType(DjangoObjectType):
    class Meta:
        model = Profile

    phones = graphene.List(graphene.String)

    def resolve_phones(self, info):
        return Phones.objects.filter(
            profile__in=str(self.id)).values_list('phone', flat=True)

    immovable_properties = graphene.List(ImmovablePropertiesOutput)

    def resolve_immovable_properties(self, info):
        return ImmovableProperties.objects.filter(
            profile__in=str(self.id)).values()

    investor_experiences = graphene.List(InvestorExperiencesOutput)

    def resolve_investor_experiences(self, info):
        return InvestorExperiences.objects.filter(
            profile__in=str(self.id)).values()

    insurances = graphene.List(InsurancesOutput)

    def resolve_insurances(self, info):
        return Insurances.objects.filter(
            profile__in=str(self.id)).values()

    investment_portfolios = graphene.List(InvestmentPortfoliosOutput)

    def resolve_investment_portfolios(self, info):
        return InvestmentPortfolios.objects.filter(
            profile__in=str(self.id)).values()

    personal_private_securities = graphene.List(
        PersonalPrivateSecuritiesOutput)

    def resolve_personal_private_securities(self, info):
        return PersonalPrivateSecurities.objects.filter(
            profile__in=str(self.id)).values()

    fixed_income_securities = graphene.List(FixedIncomeSecuritiesOutput)

    def resolve_fixed_income_securities(self, info):
        return FixedIncomeSecurities.objects.filter(
            profile__in=str(self.id)).values()


class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None):
        cpfFromAuth = str(getCPFFromAuth(token))

        phones = profile_data.pop("phones")
        immovable_properties = profile_data.pop("immovable_properties")
        investor_experiences = profile_data.pop("investor_experiences")
        insurances = profile_data.pop("insurances")
        investment_portfolios = profile_data.pop("investment_portfolios")
        personal_private_securities = profile_data.pop(
            "personal_private_securities")
        fixed_income_securities = profile_data.pop("fixed_income_securities")
        financial_advisor = profile_data.pop("financial_advisor")

        if financial_advisor:
            financial_advisor, created = FinancialAdvisors.objects.get_or_create(fullname=financial_advisor['fullname'],
                                                                                 register=financial_advisor['register'],
                                                                                 company=financial_advisor['company'],
                                                                                 )
            if created:
                financial_advisor.save()

        profile_data['financial_advisor_id'] = financial_advisor.id

        profile, created = Profile.objects.update_or_create(cpf=cpfFromAuth,
                                                            defaults={
                                                                **profile_data}
                                                            )
        if created:
            profile.save()

        if phones:
            Phones.objects.filter(profile=profile).delete()
            for phone in phones:
                phones = Phones(profile=profile,
                                phone=phone,
                                )
                phones.save()

        if immovable_properties:
            ImmovableProperties.objects.filter(profile=profile).delete()
            for immovable_property in immovable_properties:
                immovable_properties = ImmovableProperties(profile=profile,
                                                           description=immovable_property['description'],
                                                           value=immovable_property['value'],
                                                           rented=immovable_property['rented'],
                                                           funded=immovable_property['funded'],
                                                           insurance_value=immovable_property['insurance_value'],
                                                           insurance_company=immovable_property['insurance_company'],
                                                           )
                immovable_properties.save()

        if investor_experiences:
            InvestorExperiences.objects.filter(profile=profile).delete()
            for investor_experience in investor_experiences:
                investor_experiences = InvestorExperiences(profile=profile,
                                                           kind=investor_experience['kind'],
                                                           value=investor_experience['value'],
                                                           )
                investor_experiences.save()

        if insurances:
            Insurances.objects.filter(profile=profile).delete()
            for insurance in insurances:
                insurances = Insurances(profile=profile,
                                        kind=insurance['kind'],
                                        value=insurance['value'],
                                        monthly_fee=insurance['monthly_fee'],
                                        coverage=insurance['coverage'],
                                        company=insurance['company'],


                                        )
                insurances.save()

        if investment_portfolios:
            InvestmentPortfolios.objects.filter(profile=profile).delete()
            for investment_portfolio in investment_portfolios:
                investment_portfolios = InvestmentPortfolios(profile=profile,
                                                             kind=investment_portfolio['kind'],
                                                             value=investment_portfolio['value'],
                                                             tx=investment_portfolio['tx'],
                                                             )
                investment_portfolios.save()

        if personal_private_securities:
            PersonalPrivateSecurities.objects.filter(profile=profile).delete()
            for personal_private_security in personal_private_securities:
                personal_private_securities = PersonalPrivateSecurities(profile=profile,
                                                                        bank=personal_private_security['bank'],
                                                                        enterprise=personal_private_security[
                                                                            'enterprise'],
                                                                        cooperative=personal_private_security[
                                                                            'cooperative'],
                                                                        survival=personal_private_security['survival'],
                                                                        table=personal_private_security['table'],
                                                                        balance=personal_private_security['balance'],
                                                                        )
                personal_private_securities.save()

        if fixed_income_securities:
            FixedIncomeSecurities.objects.filter(profile=profile).delete()
            for fixed_income_security in fixed_income_securities:
                fixed_income_securities = FixedIncomeSecurities(profile=profile,
                                                                kind=fixed_income_security['kind'],
                                                                value=fixed_income_security['value'],
                                                                tx=fixed_income_security['tx'],
                                                                )
                fixed_income_securities.save()


class Mutation(graphene.ObjectType):
    set_profile = setProfile.Field()


class Query(graphene.ObjectType):
    get_profile = graphene.List(setType,
                                token=graphene.String(),
                                )

    def resolve_get_profile(self, info, token=None, **kwargs):
        if token:
            cpf = str(getCPFFromAuth(token))
            filter = (
                Q(cpf__exact=cpf)
            )

            profile = Profile.objects.all().filter(filter)

            return profile

        pass
