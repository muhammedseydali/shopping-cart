from django.urls import path, include
from . import views

urlpatterns = [
    path('cart', views.show_cart, name='cart'),
    path('add_cart', views.add_cart, name='add_to_cart')

]
