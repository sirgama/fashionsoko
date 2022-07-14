import json
from unicodedata import category
from urllib import response
from django.shortcuts import render
from django.urls import reverse
from .models import *
from users.models import Customer
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def store(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0795680980'
    amount = 1
    account_reference = 'Test Django'
    transaction_desc = 'Tryng test'
    callback_url = 'https://darajambili.herokuapp.com/c2b/validation'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)
    
    # context = {
        
    # }
    # return render(request, 'shop/store.html', context)

def stk_push_callback(request):
        data = request.body
        # You can do whatever you want with the notification received from MPESA here.

@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'items':items,
        'order':order,
        'cartitems':cartitems
    }
    return render(request, 'shop/cart.html', context)
@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'items':items,
        'order':order,
        'cartitems':cartitems,
    }
    return render(request, 'shop/checkout.html', context)
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item added', safe=False)

@login_required
def processOrder(request):
    transactionid = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transactionid
        
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        Shipping.objects.create(
            customer=customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            county = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
            
        )
            
    else:
        print('user not logged in')
    
    return JsonResponse('Payment complete', safe=False)

@login_required
def men(request):
    
    mens= Categories.objects.get(name='Men')
    print(mens)
    products = Product.objects.filter(category__name=mens)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    
    return render(request, 'shop/men.html', context)

@login_required
def women(request):
    womens= Categories.objects.get(name='Women')
    products = Product.objects.filter(category__name=womens)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    
    return render(request, 'shop/women.html', context)

@login_required
def access(request):
    bags= Categories.objects.get(name='Bags')
    products = Product.objects.filter(category__name=bags)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    
    return render(request, 'shop/access.html', context)

@login_required
def products(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    return render(request, 'shop/products.html', context)


@login_required
def shoes(request):
    shoes= Categories.objects.get(name='Shoes')
    products = Product.objects.filter(category__name=shoes)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    
    return render(request, 'shop/shoes.html', context)



@login_required
def watches(request):
    watch= Categories.objects.get(name='Watches')
    products = Product.objects.filter(category__name=watch)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    
    return render(request, 'shop/watches.html', context)


@login_required
def watches(request, pk):
    
    products = Product.objects.get(id=pk)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartitems = order['get_cart_items']
    context = {
        'products':products,
        'cartitems':cartitems
    }
    
    return render(request, 'shop/detail.html', context)