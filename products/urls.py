from django.conf.urls import url, include
from .views import get_products, sell_product


urlpatterns = [
    url(r'$', get_products, name='allproducts'),
    url(r'^sellproduct/$', sell_product, name="sellproduct"),
    
    
   
    ]
