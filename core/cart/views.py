from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart(request):
    cart_list = Cart.objects.all()
    return render(request, 'cart/cart.html', context={
        'cart_list':cart_list
    })