import graphene

from graphene_django import DjangoObjectType

from .models import Profile
from django.db.models import Q

class setType(DjangoObjectType):
    class Meta:
        model = Profile

class setProfile(graphene.Mutation):
    token = graphene.Field(setType)

    class Arguments:
        token = graphene.String()

    def mutate(self,info,token,):
        token = Profile(token = token)
        token.save()
        
        
        return setProfile(
            token=token)
           


class Mutation(graphene.ObjectType):
    set_profile = setProfile.Field()

class Query(graphene.ObjectType):
    getProfile = graphene.List(setType, 
    token=graphene.String(),
    )
    
    def resolve_getProfile(self, info, token=None, **kwargs,):
        if token:
            filter = (
                Q(token__icontains=token)
            )
            return Profile.objects.filter(filter)
        
        return Profile.objects.all()
