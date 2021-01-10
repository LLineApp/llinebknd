import graphene
import graphql_jwt

import functions.schema

class Mutation(functions.schema.Mutation,
graphene.ObjectType,):
    pass


class Query(functions.schema.Query,
graphene.ObjectType,):
    pass

schema = graphene.Schema(mutation=Mutation,query=Query)