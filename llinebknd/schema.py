import graphene
import graphql_jwt

import functions.schema
import users.schema


class Mutation(
        functions.schema.Mutation,
        users.schema.Mutation,
        graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(
        functions.schema.Query,
        users.schema.Query,
        graphene.ObjectType,):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
