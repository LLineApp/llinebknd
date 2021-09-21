from django.test import TestCase, Client
from functions.models import Profile
import json


class TestSchema(TestCase):

    def setUp(self):
        self.client = Client()
        self.createUser = self.client.post(
            '/graphql/?query=mutation{createUser(cpf:"12345678901", password:"123456") {user{id}}}')
        self.tokenAuth = self.client.post(
            '/graphql/?query=mutation{tokenAuth(cpf:"12345678901",password:"123456"){token}}')
        tokenauthData = json.loads(self.tokenAuth.content)
        self.token = tokenauthData['data']['tokenAuth']['token']

    '''Testing mutations'''
    
    def test_createUser(self):
        response = self.createUser
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data["data"]["createUser"]["user"]["id"], "1")

    def test_tokenAuth(self):
        self.assertEquals(self.tokenAuth.status_code, 200)

    def test_setProfile(self):
        response = self.client.post(
            '/graphql/?query=mutation{setProfile(token:"' + self.token + '", profileData: {fullname:"Obi Wan Kenobi"}){profile{fullname}}}')
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(response.content, '{"data":{"setProfile":{"profile":{"fullname":"Obi Wan Kenobi"}}}}')
        model_profile = Profile.objects.all()
        self.assertEquals(model_profile.first().fullname, "Obi Wan Kenobi")

    '''
    setAdvisorsLink(link: String, token: String): setAdvisorsLink
    setAdvisorsProfile(company: String!, cpf: String!. fullname: String!, register: String!, token: String!): setAdvisorsProfile
    addAdvisorToProfile(advisorId: Int, profileId: Int, token: String): addAdvisorToProfile
    removeAdvisorFromProfile(advisorId: Int, profile, Id: Int, token: String): removeAdvisorFromProfile
    changeMainAdvisorOfProfile(advisorId: Int, profileId: Int, token: String): changeMainAdvisorOfProfile
    addTarget(clientCpf: String!, monthlyInvestment: Float!, presentValue: Float!, suitability: Int!, token: String!, yearToStartWithdraw: Int!): addTarget
    verifyToken(token: String): Verify
    refreshToken(token: String): Refresh
    '''

    '''Testing queries'''

    def test_getProfile(self):
        Profile.objects.create(cpf='12345678901', fullname='Anakin Skywalker')
        response = self.client.get(
            '/graphql/?query={getProfile(token:"' + self.token + '"){fullname}}')
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(response.content, '{"data": {"getProfile": [{"fullname": "Anakin Skywalker"}]}}')





    '''
    getAdvisorsPortfolio(token: String, page: Int, containing: String): setAdvisorsPortfolioType
    getProspectProfile(token: String, page: Int, containing: String): setAdvisorsPortfolioType
    getAnyProfile(token: String, containing: String!): setAnyProfileType
    getAdvisors(token: String, page: Int, containing: String): getFinancialAdvisorsType
    getClientsPortfolioFromAdvisor(token: String, cpf: String, containing: String): getPortfolioFromAdvisorType
    getParams(token: String): suitabilityType
    '''