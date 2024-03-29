import graphene
from graphene_django import DjangoObjectType
from .models import *

class TargetsOutput(graphene.ObjectType):
    responsible_cpf = graphene.String(required=False)
    date = graphene.Date(required=False)
    present_value = graphene.Float(required=False)
    monthly_investment = graphene.Float(required=False)
    year_to_start_withdraw = graphene.Int(required=False)
    suitability = graphene.Int(required=False)

class ProfileAdvisorsOutput(graphene.ObjectType):
    profile_id = graphene.Int(required=True)
    advisors_id = graphene.Int(required=True)
    main_advisor = graphene.Boolean(required=True)

class FinancialAdvisorsOutput(graphene.ObjectType):
    id = graphene.Int(required=False)                                                
    fullname = graphene.String(required=False)
    register = graphene.String(required=False)
    company = graphene.String(required=False)
    cpf = graphene.String(required=False)
    profileadvisors__main_advisor = graphene.Boolean(required=False, 
                                                    name='mainAdvisor')


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
    tx_type = graphene.String(required=False)


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
