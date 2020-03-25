
from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('allproducts'))


def adjust_cart(request, id):
    """
    Adjust the quantity
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
