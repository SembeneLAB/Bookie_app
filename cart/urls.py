from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ='cart'
urlpatterns = [
  path('cart', views.cart, name='cart'),
  path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)