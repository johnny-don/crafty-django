from django import forms
from .models import Product

class SellProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields= ['image', 'item', 'description', 'style', 'wood', 'price']