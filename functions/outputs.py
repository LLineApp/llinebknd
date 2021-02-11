import graphene
from graphene_django import DjangoObjectType


class InvestorExperienceOutput(graphene.ObjectType):
    profile = graphene.Id()
    portfolio_type = graphene.String(required=False)
    value = graphene.Float(required=False)


class ImmovablePropertiesOutput(graphene.ObjectType):
    description = graphene.String(required=False)
    value = graphene.Float(required=False)
    rented = graphene.Boolean(required=False)
    funded = graphene.Boolean(required=False)
    insurance_value = graphene.Float(required=False)
    insurance_company = graphene.String(required=False)
