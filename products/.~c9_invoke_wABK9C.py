# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product

# Create your views here.

def get_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
@login_required()
def sell_product(request):
    
    
    return redirect("products.html")


