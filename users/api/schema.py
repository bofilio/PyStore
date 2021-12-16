import graphene
from graphene_django import DjangoObjectType,DjangoListField
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
class UserType(DjangoObjectType):
    class Meta:
        model=User
        fields=('username','email')

class UserQuery(graphene.ObjectType):
    users=DjangoListField(UserType)
    user=graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self,info,id):
        return get_object_or_404(User, pk=id)

class Query(UserQuery):
    pass