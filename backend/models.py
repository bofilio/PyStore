from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Address(models.Model):
    title = models.CharField(max_length=200);

class Category(models.Model):
    title = models.CharField(max_length=200)
    brief = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=20, null=True)
    icon = models.ImageField(null=True)

    def __str__(self):
        return self.title


news_status = (
    ("featured", "Featured"),
    ("new", "New"),
    ("hot", "Hot"),
)

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=news_status)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField();
    def __str__(self):
        return self.title

curencies = (
    ("usd", "USD"),
    ("eur", "EUR"),
    ("da", "DA"),
)
class Currency(models.Model):
    is_default = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=255, choices=curencies)
    change = models.FloatField()

    def __str__(self):
        return self.code


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.ForeignKey(to=Address, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return "{}".format(self.user.username)

class Product(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=news_status)
    price = models.FloatField(null=True, blank=True)
    shipping_price = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    currency = models.ForeignKey(to=Currency, on_delete=models.PROTECT)
    description = models.TextField()
    categories = models.ManyToManyField(to=Category, related_name="products")
    discount = models.FloatField(default=0)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    image = models.ImageField()
    is_main = models.BooleanField(default=False);
    product = models.ForeignKey(to=Product, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.image.path

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    sub_total = models.FloatField();
    def __str__(self):
        if self.user:
            return "{} Cart".format( self.user.username)
        else:
            return "{} Cart".format(None)



odrer_status = (
    ("pending", "Pending"),
    ("shipped", "Shipped"),
    ("comming", "Comming"),
    ("completed", "Completed"),
)
payment_status = (
    ("pending", "Pending"),
    ("verified", "Verified"),
)

class Order(models.Model):
    code = models.CharField(max_length=255)
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    shipping_address=models.CharField(max_length=255)
    shipping_date=models.DateField(null=True,blank=True)
    comment=models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    total_tax = models.FloatField(default=0)
    shipping = models.FloatField(default=0)
    total_price = models.FloatField()
    status = models.CharField(max_length=255, choices=odrer_status)
    payment_status = models.CharField(max_length=255, choices=payment_status)

    def __str__(self):
        return self.code

class Item(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.FloatField(default=1)

    class Meta:
        abstract = True

        def __str__(self):
            return self.id

class CartItem(Item):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name="items")

class OrderItem(Item):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="items")

class WishList(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product)
    def __str__(self):
        return "{} Wisthlist".format(self.user.username)
