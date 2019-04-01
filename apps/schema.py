import graphene

import apps.ingredient.schema
from apps.ingredient.mutation import IngredientMutation


class Mutations(graphene.ObjectType):
    creatOrUpdateIngredient = IngredientMutation.Field()


class Query(apps.ingredient.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
