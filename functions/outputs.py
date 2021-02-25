import graphene
from graphene_django import DjangoObjectType
from .models import *


class InvestorExperiencesOutput(graphene.ObjectType):
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


class InvestmentPortfoliosOutput(graphene.ObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)
    tx = graphene.Float(required=False)


class PersonalPrivateSecuritiesOutput(graphene.ObjectType):
    bank = graphene.String(required=False)
    enterprise = graphene.Boolean(required=False)
    cooperative = graphene.Boolean(required=False)
    survival = graphene.String(required=False)
    table = graphene.String(required=False)
    balance = graphene.Float(required=False)

class FixedIncomeSecuritiesOutput(graphene.ObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)
    tx = graphene.Float(required=False)

class ChildrenOutput(graphene.ObjectType):
    fullname = graphene.String(required=False)
    birthdate = graphene.Date(required=False)
    occupation_training = graphene.String(required=False)
    additional_info = graphene.String(required=False)
