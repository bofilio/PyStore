from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
    title = models.CharField(max_length=200);

class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.ForeignKey(to=Address, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return "{}".format(self.user.username)