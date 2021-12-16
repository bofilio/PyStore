from backend.models import *
from graphene_django import DjangoObjectType, DjangoListField
import graphene
from django.shortcuts import get_object_or_404


########################################################################ObjectTypes
class CategoryType(DjangoObjectType):
    error=graphene.String()
    class Meta:
        model = Category
        fields = "__all__"


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
        fields = "__all__"

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = "__all__"

class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = "__all__"

class PromoCodeType(DjangoObjectType):
    class Meta:
        model = PromoCode
        fields = "__all__"

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = "__all__"

class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        fields = "__all__"

##################################################################################Queries
class CategoryQuery(graphene.ObjectType):
    categories = DjangoListField(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int())

    def resolve_category(self, info, id):
        return get_object_or_404(Category, pk=id)


class ProductQuery(graphene.ObjectType):
    products = DjangoListField(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int())

    def resolve_product(self, info, id):
        return get_object_or_404(Product, pk=id)

class ProductImageQuery(graphene.ObjectType):
    product_images = DjangoListField(ProductImageType)

class OrderQuery(graphene.ObjectType):
    orders = DjangoListField(OrderType)
    order = graphene.Field(OrderType, id=graphene.Int())

    def resolve_order(self, info, id):
        return get_object_or_404(Order, pk=id)

class OrderItemQuery(graphene.ObjectType):
    orderitems = DjangoListField(OrderItemType)

class TagQuery(graphene.ObjectType):
    tags = DjangoListField(TagType)
    tag = graphene.Field(TagType, id=graphene.Int())

    def resolve_tag(self, info, id):
        return get_object_or_404(Tag, pk=id)

class CodePromoQuery(graphene.ObjectType):
    promocodes = DjangoListField(PromoCodeType)
    promocode = graphene.Field(PromoCodeType, id=graphene.Int())

    def resolve_promocode(self, info, id):
        return get_object_or_404(PromoCode, pk=id)

class RestaurantQuery(graphene.ObjectType):
    restaurants = DjangoListField(RestaurantType)
    restaurant = graphene.Field(RestaurantType, id=graphene.Int())
    def resolve_product(self, info, id):
        return get_object_or_404(Product, pk=id)

class ReviewQuery(graphene.ObjectType):
    reviews=DjangoListField(ReviewType)
    product_review = graphene.Field(ReviewType, productid=graphene.Int(required=True))
    restaurant_review = graphene.Field(ReviewType, restaurantid=graphene.Int(required=True))
    def resolve_product_review(self, info, productid):
        product= Product.objects.select_related('review').get(pk=productid)
        return product.review

#####################################################################################Mutation

###################################################################################"Schema
class Query(CategoryQuery, ProductQuery,ProductImageQuery,RestaurantQuery,ReviewQuery,CodePromoQuery,TagQuery,OrderQuery,OrderItemQuery):
    pass


