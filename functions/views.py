import os
from llinebknd.settings import BASE_DIR
from django.http import HttpResponse
from django.shortcuts import render

def get_clients_portfolio_from_advisor_help(request):
    print(os.path.join(BASE_DIR, 'llinebknd/templates/help/getClientsPortfolioFromAdvisor.html'))
    return render(request, 'help/getClientsPortfolioFromAdvisor.html')
#    return render(request, os.path.join(BASE_DIR, 'llinebknd/templates/help/getClientsPortfolioFromAdvisor.html'))
