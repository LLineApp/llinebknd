import graphene

from graphene_django import DjangoObjectType

from .models import Profile, Phones
from django.db.models import Q

from .auth import getCPFFromAuth

import json


class ProfileInput(graphene.InputObjectType):
    email = graphene.String(required=False)
    fullname = graphene.String(required=False)
    birthdate = graphene.String(required=False)
    phones = graphene.List(graphene.String, required=False)
    preferred_contact = graphene.String(required=False)
    occupation = graphene.String(required=False)
    role = graphene.String(required=False)
    company_name = graphene.String(required=False)
    business_email = graphene.String(required=False)
    business_kind = graphene.String(required=False)
    business_field = graphene.String(required=False)
    income_tax_declaration_type = graphene.String(required=False)
    company_has_private_insurance = graphene.Boolean(required=False)
    social_security_value = graphene.Int(required=False)
    private_security_your_value = graphene.Int(required=False)
    private_security_company_value = graphene.Int(required=False)
    private_security_current_balance = graphene.Int(required=False)


    
class setType(DjangoObjectType):
    class Meta:
        model = Profile


    phones = graphene.List(graphene.String)

    def resolve_phones(self, info):
        return Phones.objects.filter(
            profile__in=str(self.id)).values_list('phone', flat=True)



class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None):
        cpfFromAuth = str(getCPFFromAuth(token))
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

        return setProfile(
            profile=profile)


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
