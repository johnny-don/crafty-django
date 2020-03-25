from django.shortcuts import render
from products.models import Product


# Create your views here.
def find_item(request):
    products = Product.objects.filter(item__icontains=request.GET['q'])
    return render(request, "allproducts.html", {'products': products})