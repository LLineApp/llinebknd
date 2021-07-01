from graphql_jwt.utils import get_payload


class getCPFFromAuth(str):
    def __init__(self, token):
        self.token = token

    def __str__(self):
        payload = get_payload(self.token)
        return payload["cpf"]
