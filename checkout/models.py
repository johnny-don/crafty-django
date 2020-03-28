from django.db import models
from products.models import Product


# Create your models here.


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False, default="")
    phone_number = models.CharField(max_length=20, blank=False, default="")
    country = models.CharField(max_length=40, blank=False, default="")
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False, default="")
    street_address1 = models.CharField(max_length=40, blank=False, default="")
    street_address2 = models.CharField(max_length=40, blank=False, default="")
    county = models.CharField(max_length=40, blank=False, default="")
    
    
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    
  

    def __str__(self):
        return "{0} @ {1}".format(
            self.product.item, self.product.price)