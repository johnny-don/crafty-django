# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100)
    experience = models.CharField(max_length=300)
    style = models.CharField(max_length=200)
    wood_source = models.BooleanField()
    
    def __str__(self):
        return self.user.username




