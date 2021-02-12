import graphene

from graphene_django import DjangoObjectType

from .models import *
from django.db.models import Q

from .auth import getCPFFromAuth

from .inputs import *
from .outputs import *


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

class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None):
        cpfFromAuth = str(getCPFFromAuth(token))

        immovable_properties = profile_data.pop("immovable_properties")
        investor_experiences = profile_data.pop("investor_experiences")
        insurances = profile_data.pop("insurances")
        investment_portfolios = profile_data.pop("investment_portfolios")

        profile, created = Profile.objects.update_or_create(cpf=cpfFromAuth,
                                                            defaults={
                                                                **profile_data}
                                                            )
        if created:
            profile.save()

        if profile_data.phones:
            Phones.objects.filter(profile=profile).delete()
            for phone in profile_data.phones:
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
