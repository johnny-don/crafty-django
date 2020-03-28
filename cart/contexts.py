from django.shortcuts import get_object_or_404  
from products.models import Product


def cart_contents(request):
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    
    for id in cart.items():
        product = get_object_or_404(Product, pk=id)
        total ==  product.price
        
        cart_items.append({'id':id, 'product': product})
        
    return {'cart_items': cart_items, 'total': total}