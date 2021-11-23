from rest_framework import viewsets
from backend.api.serializers import *
from backend.models import *

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AddressViewSets(viewsets.ModelViewSet):
    queryset =  Address.objects.all()
    serializer_class = AddressSerializer

class NewsArticleViewSets(viewsets.ModelViewSet):
    queryset =  NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class CurrencyViewSets(viewsets.ModelViewSet):
    queryset =  Currency.objects.all()
    serializer_class = CurrencySerializer

class ProfileViewSets(viewsets.ModelViewSet):
    queryset =  Profile.objects.all()
    serializer_class = ProfileSerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSets(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CartViewSets(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartItemViewSets(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderItemViewSets(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class WishListViewSets(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


