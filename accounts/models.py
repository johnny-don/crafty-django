# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True, related_name='user')
    first_name = models.CharField(max_length=12, blank=True)
    last_name = models.CharField(max_length=12, blank=True)
    username = models.CharField( max_length=150)
    address_one = models.CharField(max_length=100, blank=True)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
    experience = models.CharField(max_length=300, blank=True)
    style = models.CharField(max_length=200, blank=True)
    wood_source = models.BooleanField( default=True)
    
    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
