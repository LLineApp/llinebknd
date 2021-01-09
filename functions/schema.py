import graphene

from graphene_django import DjangoObjectType

from .models import Modelo

class setType(DjangoObjectType):
    class Meta:
        model = Modelo

class setProfile(graphene.Mutation):
    token = graphene.Field(setType)

    class Arguments:
        token = graphene.String()

    def mutate(self,info,token,):
        token = Modelo(token = token)
        token.save()
        
        
        return setProfile(
            token=token)
           


class Mutation(graphene.ObjectType):
    set_profile = setProfile.Field()

class Query(graphene.ObjectType):
    dados = graphene.List(setType)
    
    def resolve_dados(self, info,):
        return Modelo.objects.all()
