from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from cart.models import Cart
# Create your views here.
def index(request):
    product_list = Product.objects.all()
    return render(request, 'main/index.html', context={
        'product_list':product_list
    })


def add_product(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        user_id = request.POST.get('user_id')

        user = User.objects.get(id=user_id)
        prod = Product.objects.get(id=prod_id)
        print(user)
        print(prod)
        Cart.objects.create(user=user, product=prod)
        return redirect('index')