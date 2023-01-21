"""bookie_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='index')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('contact/', include('contact.urls', namespace="reach")),
    path('checkout1/', include('checkout.urls', namespace='checkout1')),
    path('checkout2/', include('checkout.urls', namespace='checkout2')),
    path('checkout3/', include('checkout.urls', namespace="checkout3")),
    path('checkout4/', include('checkout.urls', namespace="checkout4")),
    path('product/', include('product.urls', namespace="product")),
    path('login/', include('login.urls', namespace="login")),
    path('shop/', include('product.urls', namespace="shop")),
    path('signup/', include('signup.urls', namespace="signup")),
    path('accounts/', include('login.urls', namespace="account_login")),
    path('add_to_cart/', include('cart.urls', namespace="add_to_cart")),
]
