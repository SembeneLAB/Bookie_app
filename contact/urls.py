from django.urls import path

from . import views

app_name = "reach"

urlpatterns = [
  path('contact', views.contact, name= 'reach')
]

