from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import admin


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    # def test_admin(self):
    #     response = self.client.get(reverse('admin'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, admin.site.urls)

    # def test_graphql(self):
    #     response = self.client.get(reverse('graphql'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'graphiql')

    def test_password_reset(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset.html")

    # def test_password_reset_confirm(self):
    #     response = self.client.get(reverse('password_reset_confirm'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/password_reset_confirm.html')

    def test_password_reset_done(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset_done.html')

    def test_password_reset_complete(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset_complete.html')

    def test_get_clients_portfolio_from_advisor_help(self):
        response = self.client.get(reverse('getClientsPortfolioFromAdvisor'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'help/getClientsPortfolioFromAdvisor.html')
