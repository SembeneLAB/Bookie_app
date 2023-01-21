from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def checkout(request):
  return render(request, 'checkout-1.html', {})

def checkoutpayment(request):
  return render(request, 'checkout-4.html', {})

def checkoutshipping(request):
  return render(request, 'checkout-2.html', {})

def checkoutinfo(request):
  return render(request, 'checkout-3.html', {})


