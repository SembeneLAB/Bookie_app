from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from shop.models import Cart, Products
from django.contrib import messages
# Create your views here.

@login_required
def cart(request):
    
    if request.user.is_authenticated:
        # user is logged in
        return render(request, 'cart.html', {})
    else:
        # user is not logged in
        return redirect('login:login')
      

def add_to_cart(request, id):
     product = Products.objects.all()
     context = {
        'product' : product}
    
     return redirect('cart:cart')
    #return HttpResponse(content=id)
    
    
def view_cart(request):
    cart_item = Cart.objects.filter(user=request.user)
    context = {'cart_item': cart_item}
    return render(request, 'cart.html', context)