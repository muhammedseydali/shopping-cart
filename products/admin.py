from django.contrib import admin
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('id', 'title', 'price', 'description', 'images', 'priority','delete_status','created_at', 'updated_at')

admin.site.register(Products, ProductAdmin)



