from cloudinary.models import CloudinaryField
from django.db import models
from users.models import Customer


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)
    image3 = CloudinaryField('image', blank=True, null=True)
    image4 = CloudinaryField('image', blank=True, null=True)
    price= models.FloatField()
    previousp = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    digit = models.BooleanField(default=False, null=True, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orders = self.orderitem_set.all()
        total = sum([item.get_total for item in orders])
        return total
    
    @property
    def get_cart_items(self):
        orders = self.orderitem_set.all()
        total = sum([item.quantity for item in orders])
        return total
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    