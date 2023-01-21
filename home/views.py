from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Products

# Create your views here.

def home(request):
  
  product = Products.objects.all()
  context = {
        'product' : product}
       
  
      
  return render(request, 'index.html', context)
