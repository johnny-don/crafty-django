from django.db import models
from products.models import Product
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    first_name = User.first_name
    last_name = User.last_name
  
    country = Profile.country
    postcode = Profile.postcode
    city = Profile.city
    street_address1 = Profile.address_one
    street_address2 = Profile.address_two
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)
  

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.item, self.product.price)