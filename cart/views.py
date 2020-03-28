
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    """renders the cart contents page"""
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """Add a quantity"""
    

    cart = request.session.get('cart' )
    if id in cart:
        cart[id] = int(cart[id])     
    else:
        cart[id] = cart.get(id) 

    request.session['cart'] = cart
    return redirect(reverse('allproducts'))


