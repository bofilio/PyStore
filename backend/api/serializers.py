from rest_framework import serializers
from backend.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["id","username","first_name","last_name","email"]
################################################################################### category apis
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields='__all__'
################################################################################### currency  apis
class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Currency
        fields = '__all__'

################################################################################### product  apis
class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= ProductImage
        fields = '__all__'

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    images=ProductImageSerializer(many=True,required=False,read_only=True)
    categories = CategorySerializer(many=True,read_only=True)
    class Meta:
        model= Product
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Product
        fields = ['url','title','price']

################################################################################### adress  apis
class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Address
        fields = '__all__'
        
################################################################################### adress  apis
class NewsArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= NewsArticle
        fields = ['id','title','image']

class NewsArticleDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= NewsArticle
        fields = '__all__'
        


        

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Profile
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
        
