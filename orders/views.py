from django.shortcuts import render, redirect
from .models import Order, OrderedItem
from products.models import Products

# Create your views here.

def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Order.objects.get_or_create(owner=customer, order_status = Order.CART_STAGE)
    context = {'cart':cart_obj}
    return render(request, 'cart.html', context)


def add_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        print(customer, 'customer is here')
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST('product_id')
        cart_obj = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
        products = Products.objects.get(pk=product_id)

        ordered_item, created = OrderedItem.objects.get_or_create(product_id=products, owner = cart_obj)
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity + ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')