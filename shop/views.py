from django.shortcuts import render
from .models import *
from users.models import Customer
# Create your views here.
def store(request):
    
    
    context = {
        
    }
    return render(request, 'shop/store.html', context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'shop/checkout.html', context)