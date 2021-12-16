from users.api.schema import Query as UQuery
from backend.api.schema import Query as BQquery
import  graphene
class RootQuery(UQuery,BQquery):
    pass

schema=graphene.Schema(query=RootQuery)