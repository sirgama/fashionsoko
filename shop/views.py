from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def store(request):
    
    
    context = {
        
    }
    return render(request, 'shop/store.html', context)



def cart(request):
    
    
    context = {
        
    }
    return render(request, 'shop/cart.html', context)

def checkout(request):
    
    
    context = {
        
    }
    return render(request, 'shop/checkout.html', context)