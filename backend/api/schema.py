from backend.models import *
from graphene_django import  DjangoObjectType,DjangoListField
import graphene

class CategoryType(DjangoObjectType):
    class Meta:
        model= Category
        fields=("id","title","brief","color","icon")

class ProductType(DjangoObjectType):
    class Meta:
        model=Product
        fields=("title","price")

class Query(graphene.ObjectType):
    all_categories=graphene.List(CategoryType)
    category=graphene.Field(CategoryType, id=graphene.Int())
    productsByCat= graphene.List(ProductType, catid=graphene.Int())
    def resolve_all_categories(root,info):
        return Category.objects.all()
    def resolve_category(root,info,id):
        return Category.objects.get(pk=id)
    def resolve_productsByCat(root,info,catid):
        return Product.objects.filter(categories__id= catid)

class CategoryMutation(graphene.Mutation):
    class Arguments:
        title= graphene.String(required=True)
        color= graphene.String(required=True)
    category=graphene.Field(CategoryType)
    @classmethod
    def mutate(cls,root,info,title,color):
        cat=Category(title=title, color=color)
        cat.save()
        return CategoryMutation(category=cat)
class Mutation(graphene.ObjectType):
    setCategory= CategoryMutation.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)