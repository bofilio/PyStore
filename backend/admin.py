from django.contrib import admin
from backend.models import *


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields if field.name != "id"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields if field.name != "id"]

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NewsArticle._meta.fields if field.name != "id"]

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currency._meta.fields if field.name != "id"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields if field.name != "id"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields if field.name != "id"]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields if field.name != "id"]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields if field.name != "id"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields if field.name != "id"]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartItem._meta.fields if field.name != "id"]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields if field.name != "id"]

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WishList._meta.fields if field.name != "id"]


