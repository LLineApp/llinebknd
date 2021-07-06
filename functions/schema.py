import graphene

from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import *
from django.db.models import Q, TextField, CharField

from .auth import getCPFFromAuth
from .advisor import advisorsLink

from .inputs import *
from .outputs import *

import math


class FinancialAdvisorsType(DjangoObjectType):
    class Meta:
        model = FinancialAdvisors


class setAdvisorsProfile(graphene.Mutation):
    advisorsProfile = graphene.Field(FinancialAdvisorsType)

    class Arguments:
        cpf = graphene.String(required=True)
        fullname = graphene.String(required=True)
        register = graphene.String(required=True)
        company = graphene.String(required=True)
        token = graphene.String(required=True)

    def mutate(self, info, cpf, fullname, register, company, token):
        cpfFromAuth = str(getCPFFromAuth(token))

        if cpfFromAuth:
            advisorsProfile = FinancialAdvisors(
                cpf=cpf,
                fullname=fullname,
                register=register,
                company=company,
            )
            advisorsProfile.save()
            return setAdvisorsProfile(advisorsProfile=advisorsProfile)


class setProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = [
            'fullname',
        ]

    phones = graphene.List(graphene.String)

    def resolve_phones(self, info):
        return Phones.objects.filter(profile__exact=str(self.id)).values_list(
            'phone', flat=True)

    children = graphene.List(ChildrenOutput)

    def resolve_children(self, info):
        return Children.objects.filter(profile__exact=str(self.id)).values()

    immovable_properties = graphene.List(ImmovablePropertiesOutput)

    def resolve_immovable_properties(self, info):
        return ImmovableProperties.objects.filter(
            profile__exact=str(self.id)).values()

    investor_experiences = graphene.List(InvestorExperiencesOutput)

    def resolve_investor_experiences(self, info):
        return InvestorExperiences.objects.filter(
            profile__exact=str(self.id)).values()

    insurances = graphene.List(InsurancesOutput)

    def resolve_insurances(self, info):
        return Insurances.objects.filter(profile__exact=str(self.id)).values()

    investment_portfolios = graphene.List(InvestmentPortfoliosOutput)

    def resolve_investment_portfolios(self, info):
        return InvestmentPortfolios.objects.filter(
            profile__exact=str(self.id)).values()

    personal_private_securities = graphene.List(
        PersonalPrivateSecuritiesOutput)

    def resolve_personal_private_securities(self, info):
        return PersonalPrivateSecurities.objects.filter(
            profile__exact=str(self.id)).values()

    fixed_income_securities = graphene.List(FixedIncomeSecuritiesOutput)

    def resolve_fixed_income_securities(self, info):
        return FixedIncomeSecurities.objects.filter(
            profile__exact=str(self.id)).values()

    is_advisor = graphene.Boolean()

    def resolve_is_advisor(self, info):
        return (FinancialAdvisors.objects.filter(cpf__exact=self.cpf).count() != 0)

    advisors = graphene.List(FinancialAdvisorsOutput)

    def resolve_advisors(self, info):
        profile_advisors = ProfileAdvisors.objects.filter(
            profile=self).values_list('advisor')
        return FinancialAdvisors.objects.filter(id__in=profile_advisors).values()


class setProfile(graphene.Mutation):
    profile = graphene.Field(setProfileType)

    class Arguments:
        token = graphene.String()
        profile_data = ProfileInput(required=True)

    def mutate(self, info, token, profile_data=None):

        financial_advisor = []
        if profile_data.financial_advisor:
            financial_advisor = profile_data.pop("financial_advisor")

        advisors = []
        if profile_data.advisors:
            advisors = profile_data.pop("advisors")

        phones = []
        if profile_data.phones:
            phones = profile_data.pop("phones")

        children = []
        if profile_data.children:
            children = profile_data.pop("children")

        immovable_properties = []
        if profile_data.immovable_properties:
            immovable_properties = profile_data.pop("immovable_properties")

        investor_experiences = []
        if profile_data.investor_experiences:
            investor_experiences = profile_data.pop("investor_experiences")

        insurances = []
        if profile_data.insurances:
            insurances = profile_data.pop("insurances")

        investment_portfolios = []
        if profile_data.investment_portfolios:
            investment_portfolios = profile_data.pop("investment_portfolios")

        personal_private_securities = []
        if profile_data.personal_private_securities:
            personal_private_securities = profile_data.pop(
                "personal_private_securities")

        fixed_income_securities = []
        if profile_data.fixed_income_securities:
            fixed_income_securities = profile_data.pop(
                "fixed_income_securities")

        if financial_advisor:
            _financial_advisor, created = FinancialAdvisors.objects.get_or_create(
                fullname=financial_advisor['fullname'],
                register=financial_advisor['register'],
                company=financial_advisor['company'],
            )
            if created:
                _financial_advisor.save()
            profile_data['financial_advisor'] = _financial_advisor

        if profile_data.cpf:
            profile, created = Profile.objects.update_or_create(cpf=profile_data.cpf,
                                                                defaults={**profile_data})
            if created:
                profile.save()
        else:
            profile = Profile.objects.create(**profile_data)
            profile.cpf = profile.id
            profile.save()

        if phones:
            Phones.objects.filter(profile=profile).delete()
            for phone in phones:
                phones = Phones(
                    profile=profile,
                    phone=phone,
                )
                phones.save()

        if advisors:
            for advisor in advisors:
                if FinancialAdvisors.objects.filter(id=advisor).exists():
                    _advisor, created = ProfileAdvisors.objects.get_or_create(
                        profile=profile,
                        advisor=FinancialAdvisors.objects.get(id=advisor),  
                    )

                    if created:
                        _advisor.save()

        if children:
            Children.objects.filter(profile=profile).delete()
            for child in children:
                children = Children(
                    profile=profile,
                    fullname=child['fullname'],
                    birthdate=child['birthdate'],
                    occupation_training=child['occupation_training'],
                    additional_info=child['additional_info'],
                )
                children.save()

        if immovable_properties:
            ImmovableProperties.objects.filter(profile=profile).delete()
            for immovable_property in immovable_properties:
                immovable_properties = ImmovableProperties(
                    profile=profile,
                    description=immovable_property['description'],
                    value=immovable_property['value'],
                    rented=immovable_property['rented'],
                    funded=immovable_property['funded'],
                    insurance_value=immovable_property['insurance_value'],
                    insurance_company=immovable_property['insurance_company'],
                )
                immovable_properties.save()

        if investor_experiences:
            InvestorExperiences.objects.filter(profile=profile).delete()
            for investor_experience in investor_experiences:
                investor_experiences = InvestorExperiences(
                    profile=profile,
                    kind=investor_experience['kind'],
                    value=investor_experience['value'],
                )
                investor_experiences.save()

        if insurances:
            Insurances.objects.filter(profile=profile).delete()
            for insurance in insurances:
                insurances = Insurances(
                    profile=profile,
                    kind=insurance['kind'],
                    value=insurance['value'],
                    monthly_fee=insurance['monthly_fee'],
                    coverage=insurance['coverage'],
                    company=insurance['company'],
                )
                insurances.save()

        if investment_portfolios:
            InvestmentPortfolios.objects.filter(profile=profile).delete()
            for investment_portfolio in investment_portfolios:
                investment_portfolios = InvestmentPortfolios(
                    profile=profile,
                    kind=investment_portfolio['kind'],
                    value=investment_portfolio['value'],
                    tx=investment_portfolio['tx'],
                    tx_type=investment_portfolio['tx_type']
                )
                investment_portfolios.save()

        if personal_private_securities:
            PersonalPrivateSecurities.objects.filter(profile=profile).delete()
            for personal_private_security in personal_private_securities:
                personal_private_securities = PersonalPrivateSecurities(
                    profile=profile,
                    bank=personal_private_security['bank'],
                    enterprise=personal_private_security['enterprise'],
                    cooperative=personal_private_security['cooperative'],
                    survival=personal_private_security['survival'],
                    table=personal_private_security['table'],
                    balance=personal_private_security['balance'],
                )
                personal_private_securities.save()

        if fixed_income_securities:
            FixedIncomeSecurities.objects.filter(profile=profile).delete()
            for fixed_income_security in fixed_income_securities:
                fixed_income_securities = FixedIncomeSecurities(
                    profile=profile,
                    kind=fixed_income_security['kind'],
                    value=fixed_income_security['value'],
                    tx=fixed_income_security['tx'],
                )
                fixed_income_securities.save()
        return setProfile(profile=profile)


class setAdvisorsLinkData(DjangoObjectType):
    class Meta:
        model = AdvisorsLink


class setAdvisorsLink(graphene.Mutation):
    advisorsLinkData = graphene.Field(setAdvisorsLinkData)

    class Arguments:
        token = graphene.String()
        link = graphene.String(required=False)

    def mutate(self, info, token, link=None):
        if token:
            cpf = str(getCPFFromAuth(token))
            if cpf:
                if link:
                    advisorsLinkData = advisorsLink.getAdvisorByLink(link)
                else:
                    advisorsLinkData = advisorsLink.createAdvisorsLink(cpf)

        return setAdvisorsLink(advisorsLinkData=advisorsLinkData)


class Mutation(graphene.ObjectType):
    set_profile = setProfile.Field()
    set_advisors_link = setAdvisorsLink.Field()
    set_advisors_profile = setAdvisorsProfile.Field()


items_per_page = 10


def normalize_page(page):
    page = page if page else 0
    if page > 0:
        return page - 1
    else:
        return 0


def searchProfileFor(containing):
    fields = [f for f in Profile._meta.fields if isinstance(
        f, (TextField, CharField))]
    queries = [Q(**{f.name + "__icontains": containing}) for f in fields]
    qs = Q()
    for query in queries:
        qs = qs | query

    return qs


def searchAdvisorsFor(containing):
    fields = [f for f in FinancialAdvisors._meta.fields if isinstance(
        f, (TextField, CharField))]
    queries = [Q(**{f.name + "__icontains": containing}) for f in fields]
    qs = Q()
    for query in queries:
        qs = qs | query

    return qs


class setPortfolioType(DjangoObjectType):
    class Meta:
        model = Profile


class setAdvisorsPortfolioType(graphene.ObjectType):

    portfolio = graphene.List(setPortfolioType)

    def resolve_portfolio(self, info):
        data = self['data']

        page = normalize_page(self['page'])

        offset = page * items_per_page
        limit = items_per_page + offset
        return data[offset:limit]

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self['data'].count()

    total_pages = graphene.Int()

    def resolve_total_pages(self, info):
        return math.ceil(self['data'].count() / items_per_page)

    current_page = graphene.Int()

    def resolve_current_page(self, info):
        return normalize_page(self['page']) + 1

    items_per_page = graphene.Int()

    def resolve_items_per_page(self, info):
        return items_per_page


class setAnyProfileType(graphene.ObjectType):

    profiles = graphene.List(setPortfolioType)

    def resolve_profiles(self, info):
        return self['data']

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self['data'].count()


class getAdvisorsType(DjangoObjectType):
    class Meta:
        model = FinancialAdvisors


class getFinancialAdvisorsType(graphene.ObjectType):

    advisors_list = graphene.List(getAdvisorsType)

    def resolve_advisors_list(self, info):
        data = self['data']

        if self['page'] == -1:
            return data

        page = normalize_page(self['page'])
        offset = page * items_per_page
        limit = items_per_page + offset
        return data[offset:limit]

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self['data'].count()

    total_pages = graphene.Int()

    def resolve_total_pages(self, info):
        return math.ceil(self['data'].count() / items_per_page)

    current_page = graphene.Int()

    def resolve_current_page(self, info):
        if self['page'] == -1:
            return -1
        return normalize_page(self['page']) + 1

    items_per_page = graphene.Int()

    def resolve_items_per_page(self, info):
        return items_per_page

class PortfolioFromAdvisorType(DjangoObjectType):
    class Meta:
        model = FinancialAdvisors


class getPortfolioFromAdvisorType(graphene.ObjectType):
    portfolio = graphene.List(setPortfolioType, description='Lista de clientes')

    def resolve_portfolio(self, info):
        data = self['data']
        return data
    
    advisor = graphene.Field(getAdvisorsType, description='Lista de assessores')

    def resolve_advisor(self, info):
        advisor = self['advisor']
        return advisor

class Query(graphene.ObjectType):
    get_profile = graphene.List(setProfileType,
                                token=graphene.String(),
                                cpf=graphene.String(),
                                )

    def resolve_get_profile(self, info, token, cpf=None, **kwargs):
        if token:
            if(cpf == "" or cpf == None):
                cpf = str(getCPFFromAuth(token))
            filter = (Q(cpf__exact=cpf))

            profile = Profile.objects.all().filter(filter)

            return profile

        pass

    get_advisors_portfolio = graphene.Field(setAdvisorsPortfolioType,
                                            token=graphene.String(),
                                            page=graphene.Int(),
                                            containing=graphene.String())

    def resolve_get_advisors_portfolio(self, info, token, page, containing=None, **kwargs):
        if token:
            cpfFromAuth = str(getCPFFromAuth(token))
            advisor = FinancialAdvisors.objects.get(cpf__exact=cpfFromAuth)
            filter = (Q(financial_advisor__exact=advisor))

            if containing:
                filter = filter & searchProfileFor(containing)

            data = Profile.objects.all().filter(filter)
            return {'data': data, 'page': page}

        pass

    get_prospect_profile = graphene.Field(setAdvisorsPortfolioType,
                                          token=graphene.String(),
                                          page=graphene.Int(),
                                          containing=graphene.String())

    def resolve_get_prospect_profile(self, info, token, page, containing=None, **kwargs):
        if token:
            cpfFromAuth = str(getCPFFromAuth(token))
            if cpfFromAuth:
                filter = (Q(accept_financial_advisor_contact__exact=True) &
                          Q(financial_advisor__isnull=True))

                if containing:
                    filter = filter & searchProfileFor(containing)

                data = Profile.objects.all().filter(filter)
                return {'data': data, 'page': page}
        pass

    get_any_profile = graphene.Field(setAnyProfileType,
                                     token=graphene.String(),
                                     containing=graphene.String(required=True))

    def resolve_get_any_profile(self, info, token, containing=None, **kwargs):
        if token:
            cpfFromAuth = str(getCPFFromAuth(token))
            if cpfFromAuth:
                if containing:
                    data = Profile.objects.all().filter(searchProfileFor(containing))
                    return {'data': data}
                else:
                    raise GraphQLError('You must set a filter')
        pass

    get_advisors = graphene.Field(getFinancialAdvisorsType,
                                  token=graphene.String(),
                                  page=graphene.Int(required=False),
                                  containing=graphene.String())

    def resolve_get_advisors(self, info, token, page, containing=None, **kwargs):
        if token:
            cpfFromAuth = str(getCPFFromAuth(token))

            if not cpfFromAuth:
                pass

            data = FinancialAdvisors.objects.all()
            if containing:
                filter = searchAdvisorsFor(containing)
                data = data.filter(filter)
            return {'data': data, 'page': page}

        pass
    
    get_clients_portfolio_from_advisor = graphene.Field(getPortfolioFromAdvisorType,
                                          token=graphene.String(description='Token de acesso'),
                                          cpf=graphene.String(description='CPF do assessor'),
                                          containing=graphene.String(description='Filtro da lista de Clientes'),
                                          description='Retorna lista de cliente por assessor')
    
    def resolve_get_clients_portfolio_from_advisor(self, info, token, cpf, containing=None, **kwargs):
        if token == 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c':
            advisor = FinancialAdvisors.objects.get(cpf__exact=cpf)
            profileAdvisors = ProfileAdvisors.objects.filter(advisor__exact=advisor).values_list('profile')
            filter = (Q(id__in=profileAdvisors))
            if containing:
                filter = filter & searchProfileFor(containing)
            
            data = Profile.objects.all().filter(filter)
            return {'data': data, 'advisor': advisor}  
        pass      