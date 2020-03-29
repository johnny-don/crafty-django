from django import forms
from .models import Product

"""The form that creates a product to be sold"""

class SellProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields= ['image', 'item', 'description', 'style', 'wood', 'price']