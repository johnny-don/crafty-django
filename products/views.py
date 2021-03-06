# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product
from products.forms import SellProductForm

# Create your views here.
@login_required
def get_products(request):
    """Get the products from the database and Display all the products """
    products = Product.objects.all()
    return render(request, "allproducts.html", {"products": products})
    
@login_required
def sell_product(request):
    """Save the new product in the database"""
    if request.method =='POST':
        sell_form = SellProductForm(request.POST, request.FILES)
        
        
        if sell_form.is_valid():
            sell_form.save()
            return redirect(reverse('allproducts'))
            
        else:
             messages.error(request, "Sorry! Unable to post your product at this time")
             
    else:
        sell_form = SellProductForm()
        
    
    return render(request, "sellproduct.html", {'sell_form': sell_form})