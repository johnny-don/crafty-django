from django.conf.urls import url, include
from .views import get_products, sell_product
from accounts.views import login

urlpatterns = [
    url(r'$', get_products, name='products'),
    url(r'^sellproduct/$', sell_product),
    url(r'^login/$', get_products, name="products"),
    
   
    ]
