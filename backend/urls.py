from rest_framework.routers import DefaultRouter
from backend.api.views import *
from django.urls import path,include
from graphene_django.views import GraphQLView
from backend.api.schema import schema


router = DefaultRouter()
router.register('users',UserViewSets)
router.register('categories',CategoryViewSets)
router.register('adresses',AddressViewSets)
router.register('news',NewsArticleViewSets)
router.register('currencies',CurrencyViewSets)
router.register('profiles',ProfileViewSets)
router.register('products',ProductViewSets)
router.register('product_images',ProductImageViewSets)
router.register('carts',CartViewSets)
router.register('orders',OrderViewSets)
router.register('cart_items',CartItemViewSets)
router.register('order_items',OrderItemViewSets)
router.register('wishlists',WishListViewSets)
urlpatterns = [
    path('', include(router.urls)),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]