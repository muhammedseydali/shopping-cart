from django.urls import path, include
from . import views

urlpatterns = [
    path('account', views.accounts, name='accounts'),
    path('logout', views.signout, name='signout')
]
