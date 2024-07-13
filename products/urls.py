from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product_list/', views.product_list,  name='list_products'),
    path('product-details/<int:pk>/', views.product_detail, name= 'product-details'),
    path('contact-us', views.contact_us, name='contact-us')
    
]
