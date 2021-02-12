import graphene
from graphene_django import DjangoObjectType


class InvestorExperienceOutput(graphene.ObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)


class ImmovablePropertiesOutput(graphene.ObjectType):
    description = graphene.String(required=False)
    value = graphene.Float(required=False)
    rented = graphene.Boolean(required=False)
    funded = graphene.Boolean(required=False)
    insurance_value = graphene.Float(required=False)
    insurance_company = graphene.String(required=False)



class InsurancesOutput(graphene.ObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)
    monthly_fee = graphene.Boolean(required=False)
    coverage = graphene.Float(required=False)
    company = graphene.String(required=False)