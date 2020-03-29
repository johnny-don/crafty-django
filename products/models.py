# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import User


# Create your models here.

class Product(models.Model):
    """The model of the products"""
    item = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    wood = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self):
        return self.item
