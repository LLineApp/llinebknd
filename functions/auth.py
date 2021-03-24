from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import json
from llinebknd.settings import AUTH_URL

transport = RequestsHTTPTransport(
    url=AUTH_URL)


client = Client(transport=transport, fetch_schema_from_transport=True)

mutation = gql(
    """
    mutation verifyTokenName ($token: String!) {
      verifyToken(token: $token) {
        payload
      }
    }
"""
)


class getCPFFromAuth(str):
    def __init__(self, token):
        self.token = token

    def __str__(self):
        params = {"token": self.token}

        response = client.execute(mutation, variable_values=params)
        return response["verifyToken"]["payload"]["cpf"]
