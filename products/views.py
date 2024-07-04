from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    featured_products = Products.objects.order_by('priority')[:4]
    latest_products = Products.objects.order_by('-id')[:4]
    
    context = { 'featured_products': featured_products, 'latest_products': latest_products }

    return render(request, 'index.html', context)

def product_list(request):
    page = request.GET.get('page', 1)  
    products = Products.objects.all()
    product_paginator = Paginator(products, 4)
    products = product_paginator.get_page(page)
    context = {'products': products}
    return render(request, 'products.html', context)

def product_detail(request,pk):
    product = Products.objects.get(pk=pk)
    context = {'product': product}
    print(context, 'cntext data')
    return render(request, 'product_details.html', context)

def contact_us(request):
    return render(request, 'contact_us.html')