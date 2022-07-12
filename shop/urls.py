from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('bags/', views.access, name='access'),
    path('watches/', views.watches, name='watches'),
    path('shoes/', views.shoes, name='shoes'),
    path('all-products/', views.products, name='products'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
]
