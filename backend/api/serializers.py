from rest_framework import serializers
from backend.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["id","username","first_name","last_name","email"]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Category
        fields='__all__'
        

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True,)
    class Meta:
        model= Product
        fields = '__all__'
        

class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Address
        fields = '__all__'
        

class NewsArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= NewsArticle
        fields = '__all__'
        

class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Currency
        fields = '__all__'
        

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Profile
        fields = '__all__'
        



class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= ProductImage
        fields = '__all__'
        


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Cart
        fields = '__all__'
        

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Order
        fields = '__all__'
        


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= CartItem
        fields = '__all__'
        

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= OrderItem
        fields = '__all__'
        

class WishListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= WishList
        fields = '__all__'
        
