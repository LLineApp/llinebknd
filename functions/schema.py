import graphene

from graphene_django import DjangoObjectType

from .models import *
from django.db.models import Q
from .puts import *

from .auth import getCPFFromAuth


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

    insurance = graphene.List(InsuranceOutPut)

    def relsove_insurance(self, info):
        return Insurance.objects.filter(
            profile__in=str(self.id)).values()

class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None):
        cpfFromAuth = str(getCPFFromAuth(token))

        immovable_properties = profile_data.pop("immovable_properties")
        insurance = profile_data.pop("insurance")

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

        if insurance:
            Insurance.objects.filter(profile=profile).delete()
            for insurancy in insurance:
                insurance = Insurance(profile=profile,
                                      insurance_type=insurancy['insurance_type'],
                                      value=insurancy['value'],
                                      monthly_fee=insurancy['monthly_fee'],
                                      coverage=insurancy['coverage'],
                                      company=insuracy['company'],
                                    
                                      
                )


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
