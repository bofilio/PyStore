from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User


########################################################################################Review
class Review(models.Model):
    review_score = models.IntegerField(help_text="totla reviews score")
    total_reviews = models.IntegerField(help_text="totale score")


########################################################################################PromoCode
class PromoCode(models.Model):
    code = models.CharField(max_length=255)
    discount = models.FloatField()
    users = models.ManyToManyField(to=User, related_name="promocodes")


########################################################################################Tags
class Tag(models.Model):
    name = models.CharField(max_length=255)


##########################################################################################Restaurant
class Restaurant(models.Model):
    owners = models.ManyToManyField(to=User, related_name='restaurants', help_text="users who possess the restaurant")
    name = models.CharField(max_length=255)
    logo = models.ImageField()
    cover = models.ImageField(null=True)
    tags = models.ManyToManyField(to=Tag, related_name="restaurants")
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    review = models.OneToOneField(to=Review, null=True, on_delete=models.PROTECT)


################################################################################################Category

class Category(models.Model):
    title = models.CharField(max_length=200)
    color = ColorField(default="#FF0000")
    icon = models.FileField(null=True)

    def __str__(self):
        return self.title


################################################################################################Product
class Product(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True, blank=True)
    shipping_price = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    description = models.TextField()
    categories = models.ManyToManyField(to=Category, related_name="products")
    discount = models.FloatField(default=0)
    review = models.OneToOneField(to=Review, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField()
    is_main = models.BooleanField(default=False)
    product = models.ForeignKey(to=Product, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.image.path


################################################################################################Order
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
    user = models.ForeignKey(to=User, null=True, related_name="orders", on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, null=True)
    shipping_date = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    total_tax = models.FloatField(default=0)
    shipping = models.FloatField(default=0)
    total_price = models.FloatField()
    status = models.CharField(max_length=255, choices=odrer_status)
    payment_status = models.CharField(max_length=255, choices=payment_status)

    def __str__(self):
        return self.code


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.FloatField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
################################################################################################Card
