import graphene
from graphene_django import DjangoObjectType


class ProfileAdvisorsInput(graphene.InputObjectType):
    profile = graphene.Int(required=True)
    advisors = graphene.Int(required=True)
    main_advisor = graphene.Boolean(required=True)

class FinancialAdvisorsInput(graphene.InputObjectType):
    fullname = graphene.String(required=False)
    register = graphene.String(required=False)
    company = graphene.String(required=False)


class ProfileAdvisorsInput(graphene.InputObjectType):
    profile_id = graphene.Int(required=True)
    advisor_id = graphene.Int(required=True)


class FixedIncomeSecuritiesInput(graphene.InputObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)
    tx = graphene.Float(required=False)


class PersonalPrivateSecuritiesInput(graphene.InputObjectType):
    bank = graphene.String(required=False)
    enterprise = graphene.Boolean(required=False)
    cooperative = graphene.Boolean(required=False)
    survival = graphene.String(required=False)
    table = graphene.String(required=False)
    balance = graphene.Float(required=False)


class InvestmentPortfoliosInput(graphene.InputObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)
    tx = graphene.Float(required=False)
    tx_type = graphene.String(required=False)


class InsurancesInput(graphene.InputObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)
    monthly_fee = graphene.Boolean(required=False)
    coverage = graphene.Float(required=False)
    company = graphene.String(required=False)


class InvestorExperiencesInput(graphene.InputObjectType):
    kind = graphene.String(required=False)
    value = graphene.Float(required=False)


class ImmovablePropertiesInput(graphene.InputObjectType):
    description = graphene.String(required=False)
    value = graphene.Float(required=False)
    rented = graphene.Boolean(required=False)
    funded = graphene.Boolean(required=False)
    insurance_value = graphene.Float(required=False)
    insurance_company = graphene.String(required=False)


class ChildrenInput(graphene.InputObjectType):
    fullname = graphene.String(required=False)
    birthdate = graphene.Date(required=False)
    occupation_training = graphene.String(required=False)
    additional_info = graphene.String(required=False)


class ProfileInput(graphene.InputObjectType):
    email = graphene.String(required=False)
    fullname = graphene.String(required=False)
    cpf = graphene.String(required=False)
    birthdate = graphene.Date(required=False)
    preferred_contact = graphene.String(required=False)
    maritalStatus = graphene.String(required=False)
    maritalHowManyYears = graphene.Int(required=False)
    spouseName = graphene.String(required=False)
    spouseOccupation = graphene.String(required=False)
    parentsAreThemSupportedByYou = graphene.Boolean(required=False)
    parentsHowMuchYouSuportThem = graphene.Float(required=False)
    parentsIsThereAPossibilityOfInheritance = graphene.Boolean(required=False)
    parentsOfWhom = graphene.String(required=False)
    parentsWhatIsTheEstimatedValue = graphene.Float(required=False)
    occupation = graphene.String(required=False)
    role = graphene.String(required=False)
    company_name = graphene.String(required=False)
    business_email = graphene.String(required=False)
    business_kind = graphene.String(required=False)
    business_field = graphene.String(required=False)
    business_phones = graphene.String(required=False)
    company_has_private_insurance = graphene.Boolean(required=False)
    income_tax_declaration_type = graphene.String(required=False)
    social_security_value = graphene.Float(required=False)
    private_security_your_value = graphene.Float(required=False)
    private_security_company_value = graphene.Float(required=False)
    private_security_current_balance = graphene.Float(required=False)
    monthly_expenses = graphene.Float(required=False)
    costs_with_dependents = graphene.Float(required=False)
    how_much_you_save = graphene.Float(required=False)
    debt_loans = graphene.Float(required=False)
    partner_in_company = graphene.Float(required=False)
    health = graphene.String(required=False)
    plans_and_projects = graphene.String(required=False)
    current_investment_process = graphene.String(required=False)
    accepts_info_about_courses = graphene.Boolean(required=False)
    follow_economic_news = graphene.Boolean(required=False)
    have_financial_concerns = graphene.String(required=False)
    additional_info = graphene.String(required=False)
    portfolio_income = graphene.Float(required=False)
    phones = graphene.List(graphene.String, required=False)
    children = graphene.List(ChildrenInput, required=False)
    immovable_properties = graphene.List(
        ImmovablePropertiesInput, required=False)
    investor_experiences = graphene.List(
        InvestorExperiencesInput, required=False)
    insurances = graphene.List(InsurancesInput, required=False)
    investment_portfolios = graphene.List(
        InvestmentPortfoliosInput, required=False)
    personal_private_securities = graphene.List(
        PersonalPrivateSecuritiesInput, required=False)
    fixed_income_securities = graphene.List(
        FixedIncomeSecuritiesInput, required=False)
    financial_advisor = graphene.Field(FinancialAdvisorsInput, required=False)
    advisors = graphene.List(graphene.Int, required=False)
    accept_financial_advisor_contact = graphene.Boolean(required=False)
    page = graphene.Int(required=False)
    level = graphene.Int(required=False)