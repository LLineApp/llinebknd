import graphene

from graphene_django import DjangoObjectType

from .models import Profile
from django.db.models import Q

from .auth import getCPFFromAuth


class ProfileInput(graphene.InputObjectType):
    email = graphene.String(required=False)
    fullname = graphene.String(required=False)
    birthdate = graphene.String(required=False)
    phones = graphene.List(graphene.String, required=False)
    preferred_contact = graphene.String(required=False)


class setType(DjangoObjectType):
    class Meta:
        model = Profile


class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None, *profile):
        cpf = getCPFFromAuth(token)

        profile = Profile(token=cpf, #Aqui eu não estou conseguindo passar o CPF no lugar do token
                          email=profile_data.email,
                          fullname=profile_data.fullname,
                          birthdate=profile_data.birthdate,
                          phones=profile_data.phones,
                          preferred_contact=profile_data.preferred_contact
                          )
        profile.save()

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
            filter = (
                Q(token__exact=token)
            )
            return Profile.objects.all().filter(filter)

        pass
