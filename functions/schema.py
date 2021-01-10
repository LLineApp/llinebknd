import graphene

from graphene_django import DjangoObjectType

from .models import Profile
from django.db.models import Q

class setType(DjangoObjectType):
    class Meta:
        model = Profile

class setProfile(graphene.Mutation):
    profile = graphene.Field(setType)
    
    
    class Arguments:
        token = graphene.String()
        email = graphene.String()
        fullname = graphene.String()
        birthdate = graphene.String()
        phones = graphene.List(graphene.String)
        preferred_contact = graphene.String()

    def mutate(self,info,token, email, fullname, birthdate, phones, preferred_contact, *profile):
        profile = Profile(token=token, 
        email=email, 
        fullname=fullname,
        birthdate=birthdate,
        phones=phones,
        preferred_contact=preferred_contact)
        profile.save()
        
        
        return setProfile(
            profile=profile)
           


class Mutation(graphene.ObjectType):
    set_profile = setProfile.Field()

class Query(graphene.ObjectType):
    get_profile = graphene.List(setType, 
    token=graphene.String(),
    )
    
    def resolve_getprofile(self, info, profile,token=None,**kwargs):
        if token:
            filter = (
                Q(profile__icontains=token)
            )
            return Profile.objects.filter(filter)
        
        return Profile.objects.all()
