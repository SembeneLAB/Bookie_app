from django.urls import path

from . import views

app_name = 'checkout'

urlpatterns = [
  path('checkout1', views.checkout, name='checkout1'),
  path('checkout2', views.checkoutpayment, name='checkout2'),
  path('checkout3', views.checkoutinfo, name='checkout3'),
  path('checkout4', views.checkoutshipping, name='checkout4')
]