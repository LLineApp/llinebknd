import graphene

from graphene_django import DjangoObjectType

from .models import *
from django.db.models import Q

from .auth import getCPFFromAuth


class ImmovablePropertiesInput(graphene.InputObjectType):
    profile = graphene.ID()
    description = graphene.String(required=False)
    value = graphene.Float(required=False)
    rented = graphene.Boolean(required=False)
    funded = graphene.Boolean(required=False)
    insurance_value = graphene.Float(required=False)
    insurance_company = graphene.String(required=False)


class ImmovablePropertiesOutput(graphene.ObjectType):
    description = graphene.String(required=False)
    value = graphene.Float(required=False)
    rented = graphene.Boolean(required=False)
    funded = graphene.Boolean(required=False)
    insurance_value = graphene.Float(required=False)
    insurance_company = graphene.String(required=False)


class ProfileInput(graphene.InputObjectType):
    email = graphene.String(required=False)
    fullname = graphene.String(required=False)
    birthdate = graphene.Date(required=False)
    preferred_contact = graphene.String(required=False)
    occupation = graphene.String(required=False)
    role = graphene.String(required=False)
    company_name = graphene.String(required=False)
    business_email = graphene.String(required=False)
    business_kind = graphene.String(required=False)
    business_field = graphene.String(required=False)
    company_has_private_insurance = graphene.Boolean(required=False)
    income_tax_declaration_type = graphene.String(required=False)
    social_security_value = graphene.Float(required=False)
    private_security_your_value = graphene.Float(required=False)
    private_security_company_value = graphene.Float(required=False)
    private_security_current_balance = graphene.Float(required=False)
    monthly_expenses = graphene.Float(required=False)
    costs_with_dependents = graphene.Float(required=False)
    how_much_you_save = graphene.Float(required=False)
    debt_loans = graphene.Float(required=False)
    partner_in_company = graphene.Float(required=False)
    health = graphene.String(required=False)
    plans_and_projects = graphene.String(required=False)
    current_investment_process = graphene.String(required=False)
    accepts_info_about_courses = graphene.Boolean(required=False)
    follow_economic_news = graphene.Boolean(required=False)
    have_financial_concerns = graphene.String(required=False)
    additional_info = graphene.String(required=False)
    phones = graphene.List(graphene.String, required=False)
    immovable_properties = graphene.List(
        ImmovablePropertiesInput, required=False)


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


class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None):
        cpfFromAuth = str(getCPFFromAuth(token))

        immovable_properties = profile_data.pop("immovable_properties")

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
